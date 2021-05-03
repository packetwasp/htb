# Docker Security relative path
```Bash
dexter@laboratory:~$ ltrace /usr/local/bin/docker-security 
setuid(0)                                                                            = -1
setgid(0)                                                                            = -1
system("chmod 700 /usr/bin/docker"chmod: changing permissions of '/usr/bin/docker': Operation not permitted
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                               = 256
system("chmod 660 /var/run/docker.sock"chmod: changing permissions of '/var/run/docker.sock': Operation not permitted
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                               = 256
+++ exited (status 0) +++
```
* By editing the path we can force setuid binary to execute and give a root shell