In order to communicate with machines outside of your local subnet, your machine must know the identity of a nearby router. The router used to route packets outside of your local subnet is commonly called a **default gateway**.

In the above network figure, `10.1.1.4` is the default gateway IP of the leftmost subnet, while `10.1.2.31` is the default gateway IP of the rightmost subnet.

The Linux kernel maintains an internal table which defines which machines should be considered local, and what gateway should be used to help communicate with those machines which are not. This table is called the **routing table**.

The `route` command can be used to display the system's routing table (`ip route` is a more modern command).
```bash
myuser@10.1.1.1:~$ route -n
Kernel IP routing table
Destination    Gateway        Genmask         Flags Metric Ref    Use Iface
0.0.0.0        10.1.1.4       0.0.0.0         UG    100    0        0 eth0
10.1.1.0       0.0.0.0        255.255.255.0   U     100    0        0 eth0
```
We will start with the second route. The second route specifies that traffic destined for the `10.1.1.0/24` network should remain in the subnet, there is no need to route the traffic to any nearby router, since sent traffic is destined for a machine in the same subnet. The `0.0.0.0` appearing in the Gateway column indicates that the gateway to reach the corresponding destination subnet is unspecified. 

The first route specifies that traffic destined for the `0.0.0.0/0` is routed to `10.1.1.4`, which is the IP address of the default gateway in this subnet (take a look at the above diagram). Note that a destination of `0.0.0.0/0` means “all the internet”, since any IP address will match this CIDR.

Is there any issue here? Doesn’t the IP range defined by the two destinations overlap? For example, the IP `10.1.1.5` matches both the first and the second routes.

In order to overcome the problem of routing ambiguity, where a single destination can be reached through multiple gateways, the route table uses the **longest prefix match** method to match IP traffic to the correct destination. This method compares the longest matching prefix of an IP address in the routing table with the destination IP address of the incoming packet, allowing the router to determine the most specific route to the destination.

### Spot Check
Given the above route table of host 10.1.1.1, where will the traffic 10.1.2.2 be routed? 
<details>
  <summary>
    Solution
  </summary>

To `10.1.1.4`

Let’s recall our original motivation, `10.1.1.1` is trying to talk with `10.1.2.2`. And now after we’ve seen the IP table of `10.1.1.1`, we know that the traffic will be routed to the default gateway (`10.1.1.4`).


</details>