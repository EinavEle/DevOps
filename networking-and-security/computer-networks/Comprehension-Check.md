{Check It!|assessment}(multiple-choice-983482178)
{Check It!|assessment}(multiple-choice-1129864935)
Use the following transcript to answer the next 4 questions.
```bash
[madonna@station madonna]$ ip address
eth0    	Link encap:Ethernet HWaddr 00:00:86:4D:F0:0C
        	inet addr:118.45.92.51 Bcast:118.45.92.255 Mask:255.255.255.0
        	UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
        	RX packets:242939 errors:0 dropped:0 overruns:0 frame:0
        	TX packets:302515 errors:0 dropped:0 overruns:1 carrier:1
        	collisions:0 txqueuelen:100
        	RX bytes:24308852 (23.1 Mb) TX bytes:166603272 (158.8 Mb)
        	Interrupt:11 Base address:0xd400

lo      	Link encap:Local Loopback
        	inet addr:127.0.0.1 Mask:255.0.0.0
        	UP LOOPBACK RUNNING MTU:16436 Metric:1
        	RX packets:29291 errors:0 dropped:0 overruns:0 frame:0
        	TX packets:29291 errors:0 dropped:0 overruns:0 carrier:0
        	collisions:0 txqueuelen:0
        	RX bytes:2661822 (2.5 Mb) TX bytes:2661822 (2.5 Mb)
       	 
[madonna@station madonna]$ route -n
Kernel IP routing table
Destination 	Gateway 	Genmask     	Flags Metric Ref Use Iface
118.45.92.0 	0.0.0.0 	255.255.255.0   U   0   0 0 eth0
```
{Check It!|assessment}(multiple-choice-2241714012)
{Check It!|assessment}(multiple-choice-2725554929)
{Check It!|assessment}(multiple-choice-1400274022)
{Check It!|assessment}(multiple-choice-2709589669)
{Check It!|assessment}(multiple-choice-4035301120)
{Check It!|assessment}(multiple-choice-3884474997)
{Check It!|assessment}(multiple-choice-1634004782)
Consider the below network, described by `156.1.0.0/16`.
```bash
                    +--------------+
                    |  Subnet A    |
                    | 127 hosts    |
                    | 156.1.1.0/24 |
                    +--------------+
                           |
                           |
                           |
          +-----------------------------+
          |                             |
+-----------------+                   +----------------+
|    Subnet B     |                   |    Subnet C    |
|    58 hosts     |                   |    29 hosts    |
|   156.1.45.0/24 |                   | 156.1.5.0/24   |
+-----------------+                   +----------------+
```
Answer the following 4 questions:
{Check It!|assessment}(multiple-choice-2197163896)
{Check It!|assessment}(multiple-choice-742210541)
{Check It!|assessment}(multiple-choice-4010137345)
{Check It!|assessment}(multiple-choice-2842938123)
Suppose the following route table of host Y:
```bash
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    100    0        0 eth0
10.0.0.0        10.0.0.1        255.255.255.0   UG    0      0        0 eth1
192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eth0
```
Answer the following 4 questions:
{Check It!|assessment}(multiple-choice-3926978570)
{Check It!|assessment}(multiple-choice-861412235)
{Check It!|assessment}(multiple-choice-1962967024)
{Check It!|assessment}(multiple-choice-1173033613)