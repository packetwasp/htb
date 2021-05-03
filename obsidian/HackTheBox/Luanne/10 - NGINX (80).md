# ODD Behavior
* / asks for auth no other endpoint does
* Robots.txt says weather exists

```Bash
curl -v http://10.10.10.218/robots.txt
User-agent: *
Disallow: /weather  #returning 404 but still harvesting cities 
* Connection #0 to host 10.10.10.218 left intact
```

# FFUF /weather/
* Looked for api Endpoints underneath /weather based upon robots.txt and supervisord 
## Fuzzing files API
```Bash
┌─[user@parrot-virtual]─[~/htb/luanne]
└──╼ $ffuf -u http://10.10.10.218/weather/FUZZ -w /opt/SecLists/Discovery/Web-Content/raft-small-words.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.10.218/weather/FUZZ
 :: Wordlist         : FUZZ: /opt/SecLists/Discovery/Web-Content/raft-small-words.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

forecast                [Status: 200, Size: 90, Words: 12, Lines: 2]
:: Progress: [43003/43003] :: Job [1/1] :: 417 req/sec :: Duration: [0:01:44] :: Errors: 0 ::
```
## Fuzzing using FW 5
``` Bash
┌─[user@parrot-virtual]─[~/htb/luanne]
└──╼ $ffuf -u http://10.10.10.218/weather/forecast?city=FUZZ -w /opt/SecLists/Fuzzing/special-chars.txt -mc 200,500 -fw 5

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.10.218/weather/forecast?city=FUZZ
 :: Wordlist         : FUZZ: /opt/SecLists/Fuzzing/special-chars.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,500
 :: Filter           : Response words: 5
________________________________________________

+                       [Status: 500, Size: 40, Words: 6, Lines: 1]
'                       [Status: 500, Size: 77, Words: 9, Lines: 2]
%                       [Status: 200, Size: 90, Words: 12, Lines: 2]
:: Progress: [32/32] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```


Identifying valid injection payload, by trying to get ' to not error the application
```Bash
└──╼ $ffuf -u http://10.10.10.218/weather/forecast?city=\'FUZZ-- -w /opt/SecLists/Fuzzing/special-chars.txt  -mc 200,500 -fw 9$
$
        /'___\  /'___\           /'___\+++++++$
       /\ \__/ /\ \__/  __  __  /\ \__/+++++++$
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\++++++$
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/++++++$
         \ \_\   \ \_\  \ \____/  \ \_\+++++++$
          \/_/    \/_/   \/___/    \/_/+++++++$
$
       v1.3.0 Kali Exclusive <3$
________________________________________________$
$
 :: Method           : GET$
 :: URL              : http://10.10.10.218/weather/forecast?city='FUZZ--$
 :: Wordlist         : FUZZ: /opt/SecLists/Fuzzing/special-chars.txt$
 :: Follow redirects : false$
 :: Calibration      : false$
 :: Timeout          : 10$
 :: Threads          : 40$
 :: Matcher          : Response status: 200,500$
 :: Filter           : Response words: 9$
________________________________________________$
$
)                       [Status: 500, Size: 37, Words: 5, Lines: 1]$
:: Progress: [32/32] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::$
```