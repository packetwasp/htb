using RemotingSample;
using System;
using System.Net.Security;
using System.ServiceModel;
using System.ServiceProcess;

namespace Server
{
    public class WcfService : ServiceBase
    {
        public ServiceHost serviceHost = null;

        public WcfService()
        {
            ServiceName = "WCFService";
        }

        public static void Main()
        {
            ServiceBase.Run(new WcfService());
        }

        protected override void OnStart(string[] args)
        {

            if (serviceHost != null)
            {
                serviceHost.Close();
            }

            Uri baseAddress = new Uri("net.tcp://0.0.0.0:8889/wcf/NewSecretWcfEndpoint");
            serviceHost = new ServiceHost(typeof(Remoting), baseAddress);
            NetTcpBinding binding = new NetTcpBinding();
            binding.Security.Mode = SecurityMode.Transport;
            binding.Security.Transport.ClientCredentialType = TcpClientCredentialType.Windows;
            binding.Security.Transport.ProtectionLevel      = ProtectionLevel.EncryptAndSign;
            binding.Security.Message.ClientCredentialType   = MessageCredentialType.Windows;

            try
            {
                serviceHost.AddServiceEndpoint(typeof(IWcfService), binding, baseAddress);
                serviceHost.Open();
            }
            catch (CommunicationException ce)
            {
                serviceHost.Abort();
            }

        }

        protected override void OnStop()
        {
            if (serviceHost != null)
            {
                serviceHost.Close();
                serviceHost = null;
            }
        }
    }
}