This exercise will demonstrate client-server communication over a TCP socket. The server should run on a different machine than the client.
1. In our shared repo, lightly review the code in `simple_linux_socket/server.c`, especially the system calls `socket()`, `accept()`, `bind()`, `listen()`, `recv()`.
1. From your bash terminal, compile the code by `gcc -o server server.c`.
1. Run by `./server`.
1. From **another host**, use the `nc <server ip> <server port>` command to establish a TCP connection and send data to the server.

We will now use some important linux networking tools to investigate what happens.

The `netstat` command can be used to display a variety of networking information, including open ports. When a port is used by a socket, it is referred to as an **open port**.

As the `./server` process is started, it first allocates a `socket`, `binds` it to the port 9999, and begins `listen`ing for connections. At some point later, the `nc` process in some other host is started. It also allocates a socket, and requests to connect to port 9999 of the server host. Because `nc` did not request a particular port number, the kernel provides a random one (52038 in the below output). As the client requests the connection, it provides its own IP address and the (randomly assigned) port number to the server.

The server chooses to `accept` the connection. The established socket is now identified by the combined IP address and port number of both the client and server.

Below is an output example **from the client machine** that currently holds an `ESTABLISHED` connection with the server:
```bash
myuser@hostname:~$ netstat -tuna
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
...
tcp        0      0 172.16.17.74:52038      13.51.197.134:9999      ESTABLISHED    <=====
udp        0      0 127.0.0.53:53           0.0.0.0:*                          
udp        0      0 0.0.0.0:67              0.0.0.0:*                          
...
```
Below is an output example from the server machine, while the server is running and connected to the above mentioned client:
```bash
ubuntu@13.51.197.134:~$ netstat -tuna
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:9999            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 172.31.46.24:22         212.50.96.83:39152      ESTABLISHED
tcp        0      0 52 172.31.46.24:22      212.50.96.83:58894      ESTABLISHED
tcp        0      0 172.31.46.24:9999       212.50.96.83:52038      ESTABLISHED     <=====
tcp        0      0 172.31.46.24:38150      54.229.116.227:80       TIME_WAIT  
tcp6       0      0 :::22                   :::*                    LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
udp        0      0 127.0.0.1:323           0.0.0.0:*                          
udp        0      0 127.0.0.53:53           0.0.0.0:*                          
udp        0      0 172.31.46.24:68         0.0.0.0:*                          
udp6       0      0 ::1:323                 :::*
```
Once the socket is established, the `nc` process and the `./server` process can read information from and write information to one another as easily as reading and writing from a file.