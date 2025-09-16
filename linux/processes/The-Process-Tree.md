A new process is created because an existing one makes an exact copy of itself (forking). This implies a tree structure of processes:
```bash
myuser@hostname:~$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager───2*[{NetworkManager}]
        ├─2*[SACSrv───3*[{SACSrv}]]
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─acpid
        ├─atd
        ├─avahi-daemon───avahi-daemon
        .
        .
        .
```
This child process has the same environment as its parent, only a different process id (PID). When a process ends normally (it is not killed or otherwise unexpectedly interrupted), the program returns its **exit code** (a number) to the parent. Only an exit status of 0 means success.

A process has a series of characteristics, which can be viewed with the `ps` command:
```bash
myuser@hostname:~$ ps -aux
USER     	PID %CPU %MEM	VSZ   RSS TTY  	STAT START   TIME COMMAND
root       	1  0.0  0.1 172752  9440 ?    	Ss   13 Feb  7:21 /sbin/init splash
root       	2  0.0  0.0  	0 	0 ?    	S	13 Feb  0:00 [kthreadd]
```
The `ps` command can display a lot of information about processes, including their PID, state (STAT column), CPU and memory usage, the user owning this process, and the command that initiated the process.