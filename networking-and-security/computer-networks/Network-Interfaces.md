In the OSI model, we've seen that every bit of data being sent over the network must pass through the lower layer - the Network Interface layer, which provides the physical and electrical interface between the networking hardware and the data being transmitted. Linux represents every networking device attached to a machine (such as an Ethernet card, wireless card, etc...) as a **network interface**.
In linux, the `ip` command can show/manipulate network interfaces, and more...
```bash
myuser@hostname:~$ ip address
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 0a:5c:36:18:fe:82 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.1/24 metric 100 brd 10.1.1.255 scope global dynamic eth0
       valid_lft 3559sec preferred_lft 3559sec
    inet6 fe80::85c:36ff:fe18:fe82/64 scope link 
       valid_lft forever preferred_lft forever
```
The above output shows 2 available network interfaces in the machine.
1. `lo` (loopback) is being used to facilitate communication between processes running on the same host (internal communication).
1. `eth0` is being used to connect a computer to a wired Ethernet network.

Before an interface can be used to send or receive traffic, it must be configured with an IP address which serves as the interface's identity. In the above output, the interface `eth0` is assigned an IP address `10.1.1.1`, which is the IP address of the "machine" (in reality, a "machine" does not have an IP address, a machine's network interfaces do).

Linux names interfaces according to the type of device it represents. The following table lists some of the more commonly encountered interface names used in Linux.
| Interface | Device  |
|---------|----------|
| `eth`n (sometimes `ens`n) | Ethernet Card  |
| `lo` | Loopback Device  |
| `wlp`n | Wireless Device  |
| `virbr`n | Virtual Bridge  |
| `enp0s`n | VirtualBox VM running Ubuntu  |
How does the kernel know the correct network interface for which to route packets? Take a closer look at the above route table…