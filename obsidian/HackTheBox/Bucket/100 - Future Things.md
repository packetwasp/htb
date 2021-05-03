### AWS Creds 
Need root for this
``` Bash
www-data@bucket:/$ ls -la .aws
total 16
drwxr-xr-x  2 root root 4096 Sep 23  2020 .
drwxr-xr-x 21 root root 4096 Feb 10 12:49 ..
-rw-------  1 root root   22 Sep 16  2020 config
-rw-------  1 root root   64 Sep 16  2020 credentials
```

```Bash
root@bucket:/.aws# cat credentials 
[default]
aws_access_key_id = test
aws_secret_access_key = test
```

### Unknown Socket
```Bash
root@bucket:/.aws# ss -lntp | column -t
State   Recv-Q  Send-Q  Local             Address:Port  Peer                                                                                                                                                                                                                                                                                                   Address:Port  Process
LISTEN  0       4096    127.0.0.1:37553   0.0.0.0:*     users:(("containerd",pid=983,fd=8))
LISTEN  0       4096    127.0.0.53%lo:53  0.0.0.0:*     users:(("systemd-resolve",pid=641,fd=13))
LISTEN  0       4096    127.0.0.1:4566    0.0.0.0:*     users:(("docker-proxy",pid=1386,fd=4))
LISTEN  0       128     0.0.0.0:22        0.0.0.0:*     users:(("sshd",pid=1002,fd=3))
LISTEN  0       511     127.0.0.1:8000    0.0.0.0:*     users:(("apache2",pid=5666,fd=5),("apache2",pid=5664,fd=5),("apache2",pid=5444,fd=5),("apache2",pid=3177,fd=5),("apache2",pid=3176,fd=5),("apache2",pid=3169,fd=5),("apache2",pid=3167,fd=5),("apache2",pid=3163,fd=5),("apache2",pid=1732,fd=5),("apache2",pid=1047,fd=5),("apache2",pid=1042,fd=5))
LISTEN  0       511     *:80              *:*           users:(("apache2",pid=5666,fd=4),("apache2",pid=5664,fd=4),("apache2",pid=5444,fd=4),("apache2",pid=3177,fd=4),("apache2",pid=3176,fd=4),("apache2",pid=3169,fd=4),("apache2",pid=3167,fd=4),("apache2",pid=3163,fd=4),("apache2",pid=1732,fd=4),("apache2",pid=1047,fd=4),("apache2",pid=1042,fd=4))
LISTEN  0       128     [::]:22           [::]:*        users:(("sshd",pid=1002,fd=4))
```
