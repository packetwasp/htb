# Supervisord
Default Creds:
* user:123 (on [readthedocs]https://supervisord.readthedocs.io/en/latest/configuration.html?highlight=password#unix-http-server-section-values)
 ![[Pasted image 20210412170104.png]]
```Bash
/python3.8 /usr/pkg/bin/supervisord-3.8 
root        348  0.0  0.0  71348  2928 ?     Is    5:06PM 0:00.00 /usr/sbin/sshd 
\_httpd      376  0.0  0.0  34952  1996 ?     Is    5:06PM 0:00.01 /usr/libexec/httpd -u -X -s -i 127.0.0.1 -I 3000 -L weather /usr/local/webapi/weather.lua -U \_httpd -b /var/www 
root        402  0.0  0.0  20216  1648 ?     Ss    5:06PM 0:00.03 /usr/sbin/cron 
\_httpd     9230  0.0  0.0  17684  1416 ?     O     8:19PM 0:00.00 /usr/bin/egrep ^USER| \\\\\[system\\\\\] \*$| init \*$| /usr/sbin/sshd \*$| /usr/sbin/syslogd -s \*$| /usr/pkg/bin/python3.8 /usr/pkg/bin/supervisord-3.8 \*$| /usr/sbin/cron \*$| /usr/sbin/powerd \*$| /usr/libexec/httpd -u -X -s.\*$|^root.\* login \*$| /usr/libexec/getty Pc ttyE.\*$| nginx.\*process.\*$ 
root        421  0.0  0.0  23072  1576 ttyE1 Is+   5:06PM 0:00.00 /usr/libexec/getty Pc ttyE1 
root        388  0.0  0.0  19924  1584 ttyE2 Is+   5:06PM 0:00.00 /usr/libexec/getty Pc ttyE2 
root        433  0.0  0.0  19780  1576 ttyE3 Is+   5:06PM 0:00.00 /usr/libexec/getty Pc ttyE3
```

## Two Interesting Processes... had to tail stdout in supervisord
```Bash
/usr/libexec/httpd -u -X -s -i 127.0.0.1 -I 3001 -L weather /home/r.michaels/devel/webapi/weather.lua -P /var/run/httpd\_devel.pid -U r.michaels -b /home/r.michaels/devel/www
```

```bash
/usr/libexec/httpd -u -X -s -i 127.0.0.1 -I 3000 -L weather /usr/local/webapi/weather.lua -U \_httpd -b /var/www
```
## HTTPD: Arguement Descriptions
* -u, Enables ~user dir
* -X enables DIR indexing
* -s logging to stderr
* -l Port is diff
* Location of lua
* -P PID
* -U, Switch to User
* -b background