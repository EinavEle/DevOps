On the Internet, there are well-known services, such as a web server, ftp , or SMTP (email) server. On Linux machines, a catalog of well known services, and the ports assigned to them, is maintained in the file `/etc/services`. Notice that both the client and server need to agree on the appropriate port number, so the `/etc/services` file is just as important on the client's machine as on the server's.

Unlike clients, processes implementing servers generally request which port they would like to bind to. Only one process may bind to a port at any given time (why?). Ports less than 1024 are known as **privileged ports**, and treated specially by the kernel. Only processes running as the `root` user may bind to privileged ports.
We now analyze a few extracted lines from the above output of the `netstat -tuna` command
```bash
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp   0      0      0.0.0.0:9999            0.0.0.0:*               LISTEN
```
This socket is bound to all interfaces (`0.0.0.0` means "all IP addresses") in the `LISTENING` state, one on port 9999. This can be recognized as the process of our server actively listening for client connections.
The next example is listening for connections as well, but only on the loopback address:
```bash
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp   0      0      127.0.0.1:631           0.0.0.0:*               LISTEN
```
It must belong to services expecting to receive connections from other processes on the local machine only. To determine what services these ports belong to, we do some greping from the `/etc/services` file.
```bash
ubuntu@13.51.197.134:~$ cat /etc/services | grep 631
ipp		631/tcp				# Internet Printing Protocol
```
Apparently, the process listening on port 631 is listening for print clients. This is probably the `cupsd` printing daemon.

Last example:
```bash
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp   0      0      127.0.0.1:631           127.0.0.1:59330         ESTABLISHED     
tcp   0      0      127.0.0.1:59330         127.0.0.1:631           ESTABLISHED
```

These lines reflect both halves of an established connection between two processes, both on the local machine. The first is bound to port 59330 (probably a randomly assigned client port), and the second to port 631. Some process on the local machine must be communicating with the `cupsd` daemon.