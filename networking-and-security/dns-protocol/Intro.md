IP addresses are somewhat hard to remember. Names are much easier. google.com is much easier to remember than 16.42.0.9 but there must be some mechanism to convert the network names into an IP address.

When an application attempts to **resolve** an address to its IP address (using the `gethostbyname()` syscall), there are generally two resources available:
- The address can be statically specified in the `/etc/hosts` file (take a look at it).
- When the local `/etc/hosts` file cannot provide the answer, the DNS service takes over. The client sends a message over the network to a publicly available DNS server, which resolves the address in response. All DNS query and reply messages are sent within **UDP** datagrams to port **53**.