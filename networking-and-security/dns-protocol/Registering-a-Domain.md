New domains can be registered by a **Domain Name Registrar**. A registrar is a commercial entity that verifies the uniqueness of the domain name, enters the domain name into the DNS database. The Internet Corporation for Assigned Names and Numbers (ICANN) accredits the various registrars.

When you register your domain name with some registrar, you also need to provide the registrar with the names and IP addresses of your primary and secondary authoritative DNS servers (why are two servers needed?). For each of these two authoritative DNS servers, the registrar would then make sure that a **Type NS** and a **Type A** record are entered into the TLD servers.

For example: for domain `networkutopia.com`, the registrar would insert the following two resource records into the TLD servers of `.com`:
```bash
(networkutopia.com, dns1.networkutopia.com, NS)
(dns1.networkutopia.com, 212.212.212.1, A)
```
You’ll also have to make sure that the Type A record for your web server `www.networkutopia.com` is entered into your authoritative DNS servers:
```bash
(networkutopia.com, 69.6.1.47, A)
```
Specific domain name information can be queried using the `whois` command:
```bash
myuser@hostname:~$ whois google.com
   Domain Name: GOOGLE.COM
   Registry Domain ID: 2138514_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2019-09-09T15:39:04Z
   Creation Date: 1997-09-15T04:00:00Z
   Registry Expiry Date: 2028-09-14T04:00:00Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2086851750
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: NS1.GOOGLE.COM
   Name Server: NS2.GOOGLE.COM
   Name Server: NS3.GOOGLE.COM
   Name Server: NS4.GOOGLE.COM
...
```