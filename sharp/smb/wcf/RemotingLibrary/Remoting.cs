using System;
using System.Collections.ObjectModel;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.ServiceModel;
using System.Text;

namespace RemotingSample
{
    [ServiceContract]
    public interface IWcfService
    {
        [OperationContract]
        string GetUsers();

        [OperationContract]
        string GetDiskInfo();

        [OperationContract]
        string GetCpuInfo();

        [OperationContract]
        string GetRamInfo();

        [OperationContract]
        string InvokePowerShell(string scriptText);
    }

    public class RemotingMethods
    {
        public string GetCpuInfo()
        {
            throw new NotImplementedException();
        }

        public string GetDiskInfo()
        {
            throw new NotImplementedException();
        }

        public string GetRamInfo()
        {
            throw new NotImplementedException();
        }

        public string GetUsers()
        {
            throw new NotImplementedException();
        }

        public string InvokePowerShell(string str)
        {
            throw new NotImplementedException();
        }
    }

    public class Remoting : IWcfService
    {
        public string GetDiskInfo()
        {
            Runspace runspace = RunspaceFactory.CreateRunspace();
            runspace.Open();
            Pipeline pipeline = runspace.CreatePipeline();
            pipeline.Commands.AddScript("Get-WmiObject -Class win32_logicaldisk | ft DeviceID, @{Name='Free(GB)';e={$_.FreeSpace /1GB}}, @{Name='Total(GB)';e={$_.Size /1GB}} -AutoSize");
            pipeline.Commands.Add("Out-String");
            Collection<PSObject> results = pipeline.Invoke();
            runspace.Close();
            StringBuilder stringBuilder = new StringBuilder();
            foreach (PSObject obj in results)
            {
                stringBuilder.AppendLine(obj.ToString());
            }
            return stringBuilder.ToString();
        }

        public string GetCpuInfo()
        {
            Runspace runspace = RunspaceFactory.CreateRunspace();
            runspace.Open();
            Pipeline pipeline = runspace.CreatePipeline();
            pipeline.Commands.AddScript("Get-WmiObject -Class win32_computersystem | fl @{Name='Physical Processors';e={$_.NumberofProcessors}} ,@{Name='Logical Processors';e={$_.NumberOfLogicalProcessors}}");
            pipeline.Commands.Add("Out-String");
            Collection<PSObject> results = pipeline.Invoke();
            runspace.Close();
            StringBuilder stringBuilder = new StringBuilder();
            foreach (PSObject obj in results)
            {
                stringBuilder.AppendLine(obj.ToString());
            }
            return stringBuilder.ToString();
        }

        public string GetRamInfo()
        {
            Runspace runspace = RunspaceFactory.CreateRunspace();
            runspace.Open();
            Pipeline pipeline = runspace.CreatePipeline();
            pipeline.Commands.AddScript("Get-WmiObject -Class win32_operatingsystem | fl @{Name='Total Memory(GB)';e={[math]::truncate($_.TotalVisibleMemorySize /1MB)}}, @{Name='Free Memory(GB)';e={[math]::truncate($_.FreePhysicalMemory /1MB)}}");
            pipeline.Commands.Add("Out-String");
            Collection<PSObject> results = pipeline.Invoke();
            runspace.Close();
            StringBuilder stringBuilder = new StringBuilder();
            foreach (PSObject obj in results)
            {
                stringBuilder.AppendLine(obj.ToString());
            }
            return stringBuilder.ToString();
        }

        public string GetUsers()
        {
            Runspace runspace = RunspaceFactory.CreateRunspace();
            runspace.Open();
            Pipeline pipeline = runspace.CreatePipeline();
            pipeline.Commands.AddScript("(Get-LocalUser).name");
            pipeline.Commands.Add("Out-String");
            Collection<PSObject> results = pipeline.Invoke();
            runspace.Close();
            StringBuilder stringBuilder = new StringBuilder();
            foreach (PSObject obj in results)
            {
                stringBuilder.AppendLine(obj.ToString());
            }
            return stringBuilder.ToString();
        }

        public string InvokePowerShell(string scriptText)
        {
            Runspace runspace = RunspaceFactory.CreateRunspace();
            runspace.Open();
            Pipeline pipeline = runspace.CreatePipeline();
            pipeline.Commands.AddScript(scriptText);
            pipeline.Commands.Add("Out-String");
            Collection <PSObject> results = pipeline.Invoke();
            runspace.Close();
            StringBuilder stringBuilder = new StringBuilder();
            foreach (PSObject obj in results)
            {
                stringBuilder.AppendLine(obj.ToString());
            }
            return stringBuilder.ToString();
        }
    }
}
