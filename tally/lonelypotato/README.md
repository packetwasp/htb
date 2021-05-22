# christiancoleman's (small) contribution
Providing 32-bit and 64-bit binary in repo. Also, added a bit of clarification for how the builds were accomplished so that you can build them yourself. Here are the settings you need to ensure are set for the x32 version:

![](/images/01-vstudio-win32-release-general.png?raw=true "1 of 2")

![](/images/02-vstudio-win32-release-linker.png?raw=true "2 of 2")

***

# lonelypotato (from https://github.com/foxglovesec/RottenPotatoNG)
Modified version of RottenPotatoNG C++ (https://github.com/foxglovesec/RottenPotatoNG). Only exe branch.
This version includes the API calls to CreateProcesAsUser() and CreateProcessWithTokenW() in order to execute a 
process passed from command line.
Command line args are:
1) Type of API Call (u) = CreateProcesAsUser, (t) = CreateProcessWithTokenW , (*) = both
2) program to execute (typically a reverse shell via bat file)

I also included a Thread impersonating SYSTEM. See MSFRottenpotato.cpp for more details

Visit also my blog: https://decoder.cloud

***

# RottenPotatoNG (from https://github.com/foxglovesec/RottenPotatoNG)
New version of RottenPotato as a C++ DLL and standalone C++ binary - no need for meterpreter or other tools.

## RottenPotatoDLL
This project generates a DLL and EXE file. The DLL contains all the code necessary to perform the RottenPotato attack and get a handle to a privileged token. The MSFRottenPotatoTestHarness project simply shows example usage for the DLL. For more examples, see https://github.com/hatRiot/token-priv/tree/master/poptoke/poptoke, specifically the SeAssignPrimaryTokenPrivilege.cpp and SeImpersonatePrivilege.cpp files. 

## RottenPotatoEXE
This project is identical to the above, except the code is all wrapped into a single project/binary. This may be more useful for some penetration testing scenarios.