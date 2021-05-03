# NMAP
## IPv4
```bash
# Nmap 7.91 scan initiated Sat Apr 10 19:46:29 2021 as: nmap -sC -sV -oA apt 10.10.10.213
Nmap scan report for 10.10.10.213
Host is up (0.091s latency).
Not shown: 998 filtered ports
PORT    STATE SERVICE VERSION
80/tcp  open  http    Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Gigantic Hosting | Home
135/tcp open  msrpc   Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Apr 10 19:46:48 2021 -- 1 IP address (1 host up) scanned in 19.31 seconds
```

## IPv6
Details on getting IPv6 name: [[15 - IPv6]]
```sql
# Nmap 7.91 scan initiated Sat Apr 10 22:14:05 2021 as: nmap -6 -sV -sC -oA apt apt
Nmap scan report for apt (dead:beef::b885:d62a:d679:573f)
Host is up (0.095s latency).
Not shown: 991 filtered ports
PORT    STATE SERVICE      VERSION
53/tcp  open  domain       Simple DNS Plus
80/tcp  open  http         Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Gigantic Hosting | Home
88/tcp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2021-04-11 05:17:05Z)
135/tcp open  msrpc        Microsoft Windows RPC
389/tcp open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=apt.htb.local
| Subject Alternative Name: DNS:apt.htb.local
| Not valid before: 2020-09-24T07:07:18
|_Not valid after:  2050-09-24T07:17:18
|_ssl-date: 2021-04-11T05:17:27+00:00; +2m47s from scanner time.
445/tcp open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp open  kpasswd5?
593/tcp open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
636/tcp open  ssl/ldap     Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=apt.htb.local
| Subject Alternative Name: DNS:apt.htb.local
| Not valid before: 2020-09-24T07:07:18
|_Not valid after:  2050-09-24T07:17:18
|_ssl-date: 2021-04-11T05:17:27+00:00; +2m47s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -9m12s, deviation: 26m48s, median: 2m46s
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: apt
|   NetBIOS computer name: APT\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: apt.htb.local
|_  System time: 2021-04-11T06:17:15+01:00
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-04-11T05:17:14
|_  start_date: 2021-04-10T15:56:54

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Apr 10 22:14:41 2021 -- 1 IP address (1 host up) scanned in 35.98 seconds
```