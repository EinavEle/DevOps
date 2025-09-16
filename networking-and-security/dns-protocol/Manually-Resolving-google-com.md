We will resolve `google.com` step by step using the `dig` command.
1. First, get the list of the root-level DNS servers. You can get it too by:
    ```bash
    dig . NS
    ```
1. Pick one of the root-level domain names. We will query this server to get the hostname of the *com* top-level domain by:
    ```bash
    dig @<your-chosen-root-level-hostname> com NS
    ```
1. Now that we have a list of *.com* TLD servers, pick one of them to query the hostname of the authoritative DNS of *google.com*:
    ```bash
    dig @<your-chosen-TLD-hostname> google.com NS
    ```
1. Finally, as we know the hostname of the authoritative DNS servers of *google.com*, we can query one of them to retrieve the IP address of *google.com*:
    ```bash
    dig @<your-chosen-authoritative-hostname> google.com A
    ```

# Spot Check
Repeat the above process yourself with `wikipedia.org`. Using the figure below (The local DNS server), make sure you understand every step in the hierarchy. How many TLD servers does `.org` have? How many authoritative servers does `wikipedia.org` have?  
<details>
  <summary>
    Solution
  </summary>

```bash
dig . NS
dig @c.root-servers.net. org NS
dig @a0.org.afilias-nst.info. wikipedia.org NS
dig @ns1.wikimedia.org. wikipedia.org A
```
There are 6 `.org` TLD servers.
There are 3 authoritative servers for `wikipedia.org`

</details>