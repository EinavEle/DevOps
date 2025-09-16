# Exercise 1 - Playing More With the `dig` Command
Use `dig` to answer the following questions:
1. Resolve the IP address of `stanford.edu`. 
1. How much did it take to resolve the query?
1. Resolve `stanford.edu` again, how much did it take now? Why?
1. How can you measure the time passed **between** the first resolution to the second one? 
1. How many authoritative servers does `stanford.edu` have?
1. Does the above answer come from the cache of some server rather than from an authoritative Stanford DNS server?
<details>
  <summary>
    Solution
  </summary>

1. `dig stanford.edu`
1. ;; Query time: 515 msec
1. ;; Query time: 0 msec (it’s cached)
1. Using the TTL value of the queries (if the two queries were executed within an interval of 5 minutes).
1. 6 servers (`dig stanford.edu NS`)
1. To check if a DNS result is cached or not using the dig command, you can look for the "flags" section in the output. If the "flags" section contains the "aa" flag, it means that the response is authoritative and came directly from an authoritative DNS server. If the "aa" flag is not present, but the "rd" flag (recursion desired) is present, it means that the response came from the cache of a DNS resolver.

</details>

# Exercise 2 - `systemd-resolve`
`systemd-resolve` is a system-level service provided by the `systemd` init system on Linux systems, responsible for providing name resolution services to applications running on the system. Ubuntu, like many other modern Linux distributions, uses `systemd` to manage system services, including the `systemd-resolve` service, which provides the name resolution functionality.
1. Explore `/etc/resolv.conf` and find your ISP primary and secondary local DNS server.

    `systemd-resolve` stores recently resolved DNS queries and their corresponding responses in memory, which can reduce the number of DNS queries sent to remote DNS servers and improve the performance of DNS resolution on Linux systems. The `systemd-resolve --statistics` command can display cache statistics. Try it.
1. What does **cache hit** mean?  
1. Wait 3-5 minutes and execute `systemd-resolve --statistics` again, why did the value of “Current Cache Size” decrease?
<details>
  <summary>
    Solution
  </summary>

1. 127.0.0.53 is **NOT** your ISP local DNS server (this is a local address). You should read carefully the content of this page, and execute: 
    ```bash
    systemd-resolve --status
    ```
    This will discover your true local DNS server IP. 
1. A cache hit refers to when the requested data is found in the cache memory and can be retrieved quickly without accessing the original source.
It's likely that the value of "Current Cache Size" will decrease because some of the DNS cache entries may have expired or been evicted due to limited cache space. DNS cache entries typically have a time-to-live (TTL) value that specifies how long they can be stored in the cache before they expire and are removed.

</details>