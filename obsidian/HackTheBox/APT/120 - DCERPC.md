┌─[user@parrot-virtual]─[~/htb/apt/nmap]
└──╼ $sudo msfdb run
[i] Database already started
                                                  
     ,           ,
    /             \
   ((__---,,,---__))
      (_) O O (_)_________
         \ _ /            |\
          o_o \   M S F   | \
               \   _____  |  *
                |||   WW|||
                |||     |||


       =[ metasploit v6.0.38-dev                          ]
+ -- --=[ 2114 exploits - 1138 auxiliary - 358 post       ]
+ -- --=[ 592 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 8 evasion                                       ]

Metasploit tip: View advanced module options with 
advanced

msf6 > search dcerpc

Matching Modules
================

   #   Name                                                    Disclosure Date  Rank     Check  Description
   -   ----                                                    ---------------  ----     -----  -----------
   0   exploit/windows/scada/advantech_webaccess_webvrpcs_bof  2017-11-02       good     No     Advantech WebAccess Webvrpcs Service Opcode 80061 Stack Buffer Overflow
   1   exploit/windows/brightstor/tape_engine_0x8a             2010-10-04       average  No     CA BrightStor ARCserve Tape Engine 0x8A Buffer Overflow
   2   exploit/windows/brightstor/tape_engine                  2006-11-21       average  No     CA BrightStor ARCserve Tape Engine Buffer Overflow
   3   auxiliary/scanner/dcerpc/tcp_dcerpc_auditor                              normal   No     DCERPC TCP Service Auditor
   4   auxiliary/scanner/dcerpc/endpoint_mapper                                 normal   No     Endpoint Mapper Service Discovery
   5   auxiliary/scanner/dcerpc/hidden                                          normal   No     Hidden DCERPC Service Discovery
   6   exploit/windows/dcerpc/ms03_026_dcom                    2003-07-16       great    No     MS03-026 Microsoft RPC DCOM Interface Overflow
   7   exploit/windows/smb/ms04_011_lsass                      2004-04-13       good     No     MS04-011 Microsoft LSASS Service DsRolerUpgradeDownlevelServer Overflow
   8   exploit/windows/dcerpc/ms05_017_msmq                    2005-04-12       good     No     MS05-017 Microsoft Message Queueing Service Path Overflow
   9   exploit/windows/dcerpc/ms07_029_msdns_zonename          2007-04-12       great    No     MS07-029 Microsoft DNS RPC Service extractQuotedChar() Overflow (TCP)
   10  exploit/windows/dcerpc/ms07_065_msmq                    2007-12-11       good     No     MS07-065 Microsoft Message Queueing Service DNS Name Path Overflow
   11  exploit/windows/smb/ms08_067_netapi                     2008-10-28       great    Yes    MS08-067 Microsoft Server Service Relative Path Stack Corruption
   12  auxiliary/gather/windows_deployment_services_shares                      normal   No     Microsoft Windows Deployment Services Unattend Gatherer
   13  auxiliary/scanner/dcerpc/windows_deployment_services                     normal   No     Microsoft Windows Deployment Services Unattend Retrieval
   14  exploit/windows/smb/smb_rras_erraticgopher              2017-06-13       average  Yes    Microsoft Windows RRAS Service MIBEntryGet Overflow
   15  auxiliary/admin/dcerpc/cve_2020_1472_zerologon                           normal   Yes    Netlogon Weak Cryptographic Authentication
   16  auxiliary/scanner/dcerpc/management                                      normal   No     Remote Management Interface Discovery
   17  auxiliary/scanner/smb/smb_enumusers_domain                               normal   No     SMB Domain User Enumeration
   18  auxiliary/scanner/smb/pipe_dcerpc_auditor                                normal   No     SMB Session Pipe DCERPC Auditor
   19  exploit/multi/ids/snort_dce_rpc                         2007-02-19       good     No     Snort 2 DCE/RPC Preprocessor Buffer Overflow


Interact with a module by name or index. For example info 19, use 19 or use exploit/multi/ids/snort_dce_rpc

msf6 > use auxiliary/scanner/dcerpc/endpoint_mapper
msf6 auxiliary(scanner/dcerpc/endpoint_mapper) > options

Module options (auxiliary/scanner/dcerpc/endpoint_mapper):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS                    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT    135              yes       The target port (TCP)
   THREADS  1                yes       The number of concurrent threads (max one per host)

msf6 auxiliary(scanner/dcerpc/endpoint_mapper) > set rhost 10.10.10.213
rhost => 10.10.10.213
msf6 auxiliary(scanner/dcerpc/endpoint_mapper) > run

[*] 10.10.10.213:135      - Connecting to the endpoint mapper service...
[*] 10.10.10.213:135      - d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 TCP (49664) 10.10.10.213 
[*] 10.10.10.213:135      - 897e2e5f-93f3-4376-9c9c-fd2277495c27 v1.0 LRPC (OLEE6A12C80846966ABEECE4BB5361E) [Frs2 Service]
[*] 10.10.10.213:135      - 897e2e5f-93f3-4376-9c9c-fd2277495c27 v1.0 TCP (49691) 10.10.10.213 [Frs2 Service]
[*] 10.10.10.213:135      - 50abc2a4-574d-40b3-9d66-ee4fd5fba076 v5.0 TCP (49685) 10.10.10.213 
[*] 10.10.10.213:135      - 906b0ce0-c70b-1067-b317-00dd010662da v1.0 LRPC (LRPC-106e0d51f354a25788) 
[*] 10.10.10.213:135      - 906b0ce0-c70b-1067-b317-00dd010662da v1.0 LRPC (LRPC-106e0d51f354a25788) 
[*] 10.10.10.213:135      - 906b0ce0-c70b-1067-b317-00dd010662da v1.0 LRPC (LRPC-106e0d51f354a25788) 
[*] 10.10.10.213:135      - 76f226c3-ec14-4325-8a99-6a46348418af v1.0 LRPC (WMsgKRpc06D961) 
[*] 10.10.10.213:135      - 12e65dd8-887f-41ef-91bf-8d816c42c2e7 v1.0 LRPC (WMsgKRpc06D961) [Secure Desktop LRPC interface]
[*] 10.10.10.213:135      - 906b0ce0-c70b-1067-b317-00dd010662da v1.0 LRPC (OLE17DAAE0B09F0E70FAF508B534071) 
[*] 10.10.10.213:135      - 906b0ce0-c70b-1067-b317-00dd010662da v1.0 LRPC (LRPC-de53eb5f929516a520) 
[*] 10.10.10.213:135      - 367abb81-9844-35f1-ad32-98f038001003 v2.0 TCP (49673) 10.10.10.213 
[*] 10.10.10.213:135      - 4c9dbf19-d39e-4bb9-90ee-8f7179b20283 v1.0 LRPC (LRPC-c2786dfd692a1c5611) 
[*] 10.10.10.213:135      - e38f5360-8572-473e-b696-1b46873beeab v1.0 LRPC (LRPC-c2786dfd692a1c5611) 
[*] 10.10.10.213:135      - 98716d03-89ac-44c7-bb8c-285824e51c4a v1.0 LRPC (LRPC-f179adc4d857ba9fab) [XactSrv service]
[*] 10.10.10.213:135      - 1a0d010f-1c33-432c-b0f5-8cf4e8053099 v1.0 LRPC (LRPC-f179adc4d857ba9fab) [IdSegSrv service]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 PIPE (\pipe\lsass) \\APT [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (audit) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (securityevent) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (LSARPC_ENDPOINT) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (lsacap) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (LSA_EAS_ENDPOINT) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (lsapolicylookup) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (lsasspirpc) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (protected_storage) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (SidKey Local End Point) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (samss lpc) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 TCP (49667) 10.10.10.213 [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (OLE9990FF348637ECD49955C8BF8191) [Impl friendly name]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 PIPE (\pipe\lsass) \\APT [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (audit) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (securityevent) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (LSARPC_ENDPOINT) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (lsacap) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (LSA_EAS_ENDPOINT) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (lsapolicylookup) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (lsasspirpc) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (protected_storage) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (SidKey Local End Point) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (samss lpc) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 TCP (49667) 10.10.10.213 [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (OLE9990FF348637ECD49955C8BF8191) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 LRPC (NTDS_LPC) [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 HTTP (49669) 10.10.10.213 [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - e3514235-4b06-11d1-ab04-00c04fc2dcd2 v4.0 PIPE (\pipe\833db8ba75fe444b) \\APT [MS NT Directory DRS Interface]
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 PIPE (\pipe\lsass) \\APT 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (audit) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (securityevent) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (LSARPC_ENDPOINT) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (lsacap) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (LSA_EAS_ENDPOINT) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (lsapolicylookup) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (lsasspirpc) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (protected_storage) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (SidKey Local End Point) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (samss lpc) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 TCP (49667) 10.10.10.213 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (OLE9990FF348637ECD49955C8BF8191) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 LRPC (NTDS_LPC) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 HTTP (49669) 10.10.10.213 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ab v0.0 PIPE (\pipe\833db8ba75fe444b) \\APT 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 PIPE (\pipe\lsass) \\APT 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (audit) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (securityevent) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (LSARPC_ENDPOINT) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (lsacap) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (LSA_EAS_ENDPOINT) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (lsapolicylookup) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (lsasspirpc) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (protected_storage) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (SidKey Local End Point) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (samss lpc) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 TCP (49667) 10.10.10.213 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (OLE9990FF348637ECD49955C8BF8191) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 LRPC (NTDS_LPC) 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 HTTP (49669) 10.10.10.213 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 PIPE (\pipe\833db8ba75fe444b) \\APT 
[*] 10.10.10.213:135      - 12345778-1234-abcd-ef00-0123456789ac v1.0 TCP (49670) 10.10.10.213 
[*] 10.10.10.213:135      - df1941c5-fe89-4e79-bf10-463657acf44d v1.0 LRPC (LRPC-5cb2537647826dca73) [EFS RPC Interface]
[*] 10.10.10.213:135      - df1941c5-fe89-4e79-bf10-463657acf44d v1.0 PIPE (\pipe\efsrpc) \\APT [EFS RPC Interface]
[*] 10.10.10.213:135      - 04eeb297-cbf4-466b-8a2a-bfd6a2f10bba v1.0 LRPC (LRPC-5cb2537647826dca73) [EFSK RPC Interface]
[*] 10.10.10.213:135      - 04eeb297-cbf4-466b-8a2a-bfd6a2f10bba v1.0 PIPE (\pipe\efsrpc) \\APT [EFSK RPC Interface]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 PIPE (\pipe\lsass) \\APT [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (audit) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (securityevent) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (LSARPC_ENDPOINT) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (lsacap) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (LSA_EAS_ENDPOINT) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (lsapolicylookup) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (lsasspirpc) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (protected_storage) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (SidKey Local End Point) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (samss lpc) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 TCP (49667) 10.10.10.213 [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (OLE9990FF348637ECD49955C8BF8191) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (NTDS_LPC) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 HTTP (49669) 10.10.10.213 [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 PIPE (\pipe\833db8ba75fe444b) \\APT [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 TCP (49670) 10.10.10.213 [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (NETLOGON_LRPC) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 PIPE (\pipe\lsass) \\APT [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (audit) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (securityevent) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (LSARPC_ENDPOINT) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (lsacap) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (LSA_EAS_ENDPOINT) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (lsapolicylookup) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (lsasspirpc) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (protected_storage) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (SidKey Local End Point) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (samss lpc) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 TCP (49667) 10.10.10.213 [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (OLE9990FF348637ECD49955C8BF8191) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (NTDS_LPC) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 HTTP (49669) 10.10.10.213 [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 PIPE (\pipe\833db8ba75fe444b) \\APT [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 TCP (49670) 10.10.10.213 [RemoteAccessCheck]
[*] 10.10.10.213:135      - 0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7 v0.0 LRPC (NETLOGON_LRPC) [RemoteAccessCheck]
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 PIPE (\pipe\lsass) \\APT 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (audit) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (securityevent) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (LSARPC_ENDPOINT) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (lsacap) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (LSA_EAS_ENDPOINT) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (lsapolicylookup) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (lsasspirpc) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (protected_storage) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (SidKey Local End Point) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (samss lpc) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 TCP (49667) 10.10.10.213 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (OLE9990FF348637ECD49955C8BF8191) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (NTDS_LPC) 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 HTTP (49669) 10.10.10.213 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 PIPE (\pipe\833db8ba75fe444b) \\APT 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 TCP (49670) 10.10.10.213 
[*] 10.10.10.213:135      - 12345678-1234-abcd-ef00-01234567cffb v1.0 LRPC (NETLOGON_LRPC) 
[*] 10.10.10.213:135      - dd490425-5325-4565-b774-7e27d6c09c24 v1.0 LRPC (LRPC-7f732ade2de43d46e8) [Base Firewall Engine API]
[*] 10.10.10.213:135      - 7f9d11bf-7fb9-436b-a812-b2d50c5d4c03 v1.0 LRPC (LRPC-7f732ade2de43d46e8) [Fw APIs]
[*] 10.10.10.213:135      - 7f9d11bf-7fb9-436b-a812-b2d50c5d4c03 v1.0 LRPC (LRPC-d6b9913f0cab646169) [Fw APIs]
[*] 10.10.10.213:135      - f47433c3-3e9d-4157-aad4-83aa1f5c2d4c v1.0 LRPC (LRPC-7f732ade2de43d46e8) [Fw APIs]
[*] 10.10.10.213:135      - f47433c3-3e9d-4157-aad4-83aa1f5c2d4c v1.0 LRPC (LRPC-d6b9913f0cab646169) [Fw APIs]
[*] 10.10.10.213:135      - 2fb92682-6599-42dc-ae13-bd2ca89bd11c v1.0 LRPC (LRPC-7f732ade2de43d46e8) [Fw APIs]
[*] 10.10.10.213:135      - 2fb92682-6599-42dc-ae13-bd2ca89bd11c v1.0 LRPC (LRPC-d6b9913f0cab646169) [Fw APIs]
[*] 10.10.10.213:135      - df4df73a-c52d-4e3a-8003-8437fdf8302a v0.0 LRPC (LRPC-7f732ade2de43d46e8) [WM_WindowManagerRPC\Server]
[*] 10.10.10.213:135      - df4df73a-c52d-4e3a-8003-8437fdf8302a v0.0 LRPC (LRPC-d6b9913f0cab646169) [WM_WindowManagerRPC\Server]
[*] 10.10.10.213:135      - df4df73a-c52d-4e3a-8003-8437fdf8302a v0.0 LRPC (LRPC-ba8bb5d74d6ab96a2a) [WM_WindowManagerRPC\Server]
[*] 10.10.10.213:135      - f2c9b409-c1c9-4100-8639-d8ab1486694a v1.0 LRPC (LRPC-813377c6c2b56de5c9) [Witness Client Upcall Server]
[*] 10.10.10.213:135      - eb081a0d-10ee-478a-a1dd-50995283e7a8 v3.0 LRPC (LRPC-813377c6c2b56de5c9) [Witness Client Test Interface]
[*] 10.10.10.213:135      - 7f1343fe-50a9-4927-a778-0c5859517bac v1.0 LRPC (LRPC-813377c6c2b56de5c9) [DfsDs service]
[*] 10.10.10.213:135      - 7f1343fe-50a9-4927-a778-0c5859517bac v1.0 LRPC (DNSResolver) [DfsDs service]
[*] 10.10.10.213:135      - 7f1343fe-50a9-4927-a778-0c5859517bac v1.0 PIPE (\PIPE\wkssvc) \\APT [DfsDs service]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (IUserProfile2) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (IUserProfile2) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (senssvc) [Impl friendly name]
[*] 10.10.10.213:135      - 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53 v1.0 LRPC (IUserProfile2) 
[*] 10.10.10.213:135      - 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53 v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) 
[*] 10.10.10.213:135      - 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53 v1.0 LRPC (senssvc) 
[*] 10.10.10.213:135      - 1ff70682-0a51-30e8-076d-740be8cee98b v1.0 LRPC (IUserProfile2) 
[*] 10.10.10.213:135      - 1ff70682-0a51-30e8-076d-740be8cee98b v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) 
[*] 10.10.10.213:135      - 1ff70682-0a51-30e8-076d-740be8cee98b v1.0 LRPC (senssvc) 
[*] 10.10.10.213:135      - 1ff70682-0a51-30e8-076d-740be8cee98b v1.0 PIPE (\PIPE\atsvc) \\APT 
[*] 10.10.10.213:135      - 378e52b0-c0a9-11cf-822d-00aa0051e40f v1.0 LRPC (IUserProfile2) 
[*] 10.10.10.213:135      - 378e52b0-c0a9-11cf-822d-00aa0051e40f v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) 
[*] 10.10.10.213:135      - 378e52b0-c0a9-11cf-822d-00aa0051e40f v1.0 LRPC (senssvc) 
[*] 10.10.10.213:135      - 378e52b0-c0a9-11cf-822d-00aa0051e40f v1.0 PIPE (\PIPE\atsvc) \\APT 
[*] 10.10.10.213:135      - 86d35949-83c9-4044-b424-db363231fd0c v1.0 LRPC (IUserProfile2) 
[*] 10.10.10.213:135      - 86d35949-83c9-4044-b424-db363231fd0c v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) 
[*] 10.10.10.213:135      - 86d35949-83c9-4044-b424-db363231fd0c v1.0 LRPC (senssvc) 
[*] 10.10.10.213:135      - 86d35949-83c9-4044-b424-db363231fd0c v1.0 PIPE (\PIPE\atsvc) \\APT 
[*] 10.10.10.213:135      - 86d35949-83c9-4044-b424-db363231fd0c v1.0 LRPC (ubpmtaskhostchannel) 
[*] 10.10.10.213:135      - 86d35949-83c9-4044-b424-db363231fd0c v1.0 TCP (49666) 10.10.10.213 
[*] 10.10.10.213:135      - 3a9ef155-691d-4449-8d05-09ad57031823 v1.0 LRPC (IUserProfile2) 
[*] 10.10.10.213:135      - 3a9ef155-691d-4449-8d05-09ad57031823 v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) 
[*] 10.10.10.213:135      - 3a9ef155-691d-4449-8d05-09ad57031823 v1.0 LRPC (senssvc) 
[*] 10.10.10.213:135      - 3a9ef155-691d-4449-8d05-09ad57031823 v1.0 PIPE (\PIPE\atsvc) \\APT 
[*] 10.10.10.213:135      - 3a9ef155-691d-4449-8d05-09ad57031823 v1.0 LRPC (ubpmtaskhostchannel) 
[*] 10.10.10.213:135      - 3a9ef155-691d-4449-8d05-09ad57031823 v1.0 TCP (49666) 10.10.10.213 
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 LRPC (IUserProfile2) [UserMgrCli]
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) [UserMgrCli]
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 LRPC (senssvc) [UserMgrCli]
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 PIPE (\PIPE\atsvc) \\APT [UserMgrCli]
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 LRPC (ubpmtaskhostchannel) [UserMgrCli]
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 TCP (49666) 10.10.10.213 [UserMgrCli]
[*] 10.10.10.213:135      - b18fbab6-56f8-4702-84e0-41053293a869 v1.0 LRPC (LRPC-e1358c9f2b31415438) [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 LRPC (IUserProfile2) [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 LRPC (senssvc) [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 PIPE (\PIPE\atsvc) \\APT [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 LRPC (ubpmtaskhostchannel) [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 TCP (49666) 10.10.10.213 [UserMgrCli]
[*] 10.10.10.213:135      - 0d3c7f20-1c8d-4654-a1b3-51563b298bda v1.0 LRPC (LRPC-e1358c9f2b31415438) [UserMgrCli]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 LRPC (IUserProfile2) [IKE/Authip API]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 LRPC (OLE502A2A4A713113A10FE56E32D49D) [IKE/Authip API]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 LRPC (senssvc) [IKE/Authip API]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 PIPE (\PIPE\atsvc) \\APT [IKE/Authip API]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 LRPC (ubpmtaskhostchannel) [IKE/Authip API]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 TCP (49666) 10.10.10.213 [IKE/Authip API]
[*] 10.10.10.213:135      - a398e520-d59a-4bdd-aa7a-3c1e0303a511 v1.0 LRPC (LRPC-e1358c9f2b31415438) [IKE/Authip API]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (LRPC-826a6da6d868ccdb50) [Impl friendly name]
[*] 10.10.10.213:135      - 2eb08e3e-639f-4fba-97b1-14f878961076 v1.0 LRPC (LRPC-4f10d21a14e0fd2a1a) [Group Policy RPC Interface]
[*] 10.10.10.213:135      - 7ea70bcf-48af-4f6a-8968-6a440754d5fa v1.0 LRPC (LRPC-9614d2626e7b56620b) [NSI server endpoint]
[*] 10.10.10.213:135      - 30adc50c-5cbc-46ce-9a0e-91914789e23c v1.0 LRPC (LRPC-e562956f20890d7c2d) [NRP server endpoint]
[*] 10.10.10.213:135      - f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 LRPC (LRPC-e562956f20890d7c2d) [Event log TCPIP]
[*] 10.10.10.213:135      - f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 LRPC (eventlog) [Event log TCPIP]
[*] 10.10.10.213:135      - f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 PIPE (\pipe\eventlog) \\APT [Event log TCPIP]
[*] 10.10.10.213:135      - f6beaff7-1e19-4fbb-9f8f-b89e2018337c v1.0 TCP (49665) 10.10.10.213 [Event log TCPIP]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 LRPC (LRPC-e562956f20890d7c2d) [DHCP Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 LRPC (eventlog) [DHCP Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 PIPE (\pipe\eventlog) \\APT [DHCP Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 TCP (49665) 10.10.10.213 [DHCP Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5 v1.0 LRPC (dhcpcsvc) [DHCP Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 LRPC (LRPC-e562956f20890d7c2d) [DHCPv6 Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 LRPC (eventlog) [DHCPv6 Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 PIPE (\pipe\eventlog) \\APT [DHCPv6 Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 TCP (49665) 10.10.10.213 [DHCPv6 Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 LRPC (dhcpcsvc) [DHCPv6 Client LRPC Endpoint]
[*] 10.10.10.213:135      - 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6 v1.0 LRPC (dhcpcsvc6) [DHCPv6 Client LRPC Endpoint]
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-e562956f20890d7c2d) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (eventlog) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 PIPE (\pipe\eventlog) \\APT 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 TCP (49665) 10.10.10.213 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (dhcpcsvc) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (dhcpcsvc6) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-33794889515a34ced5) 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 LRPC (LRPC-e562956f20890d7c2d) 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 LRPC (eventlog) 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 PIPE (\pipe\eventlog) \\APT 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 TCP (49665) 10.10.10.213 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 LRPC (dhcpcsvc) 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 LRPC (dhcpcsvc6) 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 LRPC (LRPC-33794889515a34ced5) 
[*] 10.10.10.213:135      - a500d4c6-0dd1-4543-bc0c-d5f93486eaf8 v1.0 LRPC (LRPC-e62548870ae76f1fa2) 
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (umpo) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (actkernel) [Impl friendly name]
[*] 10.10.10.213:135      - c9ac6db5-82b7-4e55-ae8a-e464ed7b4277 v1.0 LRPC (LRPC-981bb3ba975cbae85b) [Impl friendly name]
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (umpo) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (actkernel) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-981bb3ba975cbae85b) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LSMApi) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 PIPE (\pipe\LSM_API_service) \\APT 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-144e00b1bf2a8b116a) 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 LRPC (umpo) 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 LRPC (actkernel) 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 LRPC (LRPC-981bb3ba975cbae85b) 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 LRPC (LSMApi) 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 PIPE (\pipe\LSM_API_service) \\APT 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 LRPC (LRPC-144e00b1bf2a8b116a) 
[*] 10.10.10.213:135      - 697dcda9-3ba9-4eb2-9247-e11f1901b0d2 v1.0 LRPC (LRPC-f0a0a45ab64d57716b) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (umpo) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (actkernel) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-981bb3ba975cbae85b) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LSMApi) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 PIPE (\pipe\LSM_API_service) \\APT 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-144e00b1bf2a8b116a) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (LRPC-f0a0a45ab64d57716b) 
[*] 10.10.10.213:135      - d09bdeb5-6171-4a34-bfe2-06fa82652568 v1.0 LRPC (csebpub) 
[*] 10.10.10.213:135      - 76f226c3-ec14-4325-8a99-6a46348418af v1.0 LRPC (WMsgKRpc069F90) 
[*] 10.10.10.213:135      - 76f226c3-ec14-4325-8a99-6a46348418af v1.0 PIPE (\PIPE\InitShutdown) \\APT 
[*] 10.10.10.213:135      - 76f226c3-ec14-4325-8a99-6a46348418af v1.0 LRPC (WindowsShutdown) 
[*] 10.10.10.213:135      - d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 LRPC (WMsgKRpc069F90) 
[*] 10.10.10.213:135      - d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 PIPE (\PIPE\InitShutdown) \\APT 
[*] 10.10.10.213:135      - d95afe70-a6d5-4259-822e-2c84da1ddb0d v1.0 LRPC (WindowsShutdown) 
[*] 10.10.10.213:135      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed