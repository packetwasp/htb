using RemotingSample;
using System;
using System.ServiceModel;

namespace Client {

    public class Client
    {
        public static void Main() {
            ChannelFactory<IWcfService> channelFactory = new ChannelFactory<IWcfService>(
                new NetTcpBinding(SecurityMode.Transport),"net.tcp://localhost:8889/wcf/NewSecretWcfEndpoint"
            );
            IWcfService client = channelFactory.CreateChannel();
            Console.WriteLine(client.GetDiskInfo());
            Console.WriteLine(client.GetCpuInfo());
            Console.WriteLine(client.GetRamInfo());
        }
    }
}