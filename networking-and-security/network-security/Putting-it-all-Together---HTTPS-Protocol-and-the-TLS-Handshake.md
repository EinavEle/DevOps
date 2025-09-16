**Although we will be focusing on the HTTPS and TLS protocols, the discussed security techniques are widely used in many other protocols and systems.**

HTTPS (HyperText Transfer Protocol Secure) is an encrypted version of the HTTP protocol usually running on **port 443**. It uses SSL or TLS protocol to encrypt all communication between a client and a server. This secure connection allows clients to safely exchange sensitive data with a server, such as when performing banking activities or online shopping.

Consider the above mentioned banking scenario: Bob sends to his bank website (represented by Alice) an HTTP request which essentially says "I'm Bob, want to transfer 500$ to John using the following credit card number....". If no security measures are taken, Bob could be surprised in a few ways, as detailed below:
- If no **encryption** is used, an intruder (man-in-the-middle) could intercept Bob’s request and use Bob's credit card details.
- If no **data integrity** is used, an intruder could modify Bob’s transaction (e.g. change "John" to "Eve").
- Finally, if no **server authentication** is used, Bob may believe that that server he is talking with, is the original Bank website, while actually he talks with a fake website maintained by Eve, who is impersonating the bank website. After receiving Bob’s transaction, Eve could take and use Bob’s information.

We now want to build security mechanisms that provide: Privacy (encryption), Data Integrity, and Authenticity.

TLS handshake is the initial process that occurs between a client and a server when establishing a secure connection using the Transport Layer Security (TLS) protocol. It involves a series of steps including encryption negotiation, authentication, and key exchange. As detailed below:
1. **Client hello**: The "Client hello" message is a request to the server to begin a TLS handshake. This message includes the TLS version supported by the client, a random value known as the client random, and a list of supported cipher suites and compression methods.
1. **Server Hello**: The server responds with a Server Hello message, which includes the TLS version selected for the connection, a random value known as the server random, and the chosen cipher suite and compression method from the client's list.
1. **Certificate**: The server sends its digital certificate, which includes its public key and other identifying information, to the client.
1. **Client Key Exchange**: The client generates a secret key (called pre-master key), encrypts it using the server's public key from the certificate, and sends the encrypted pre-master key to the server.
1. **Finished**: Both the client and server exchange "Finished" messages to confirm that they have successfully completed the handshake process. These messages include a hash of all the previous handshake messages, encrypted using the secret key.
1. **Secure Communication**: Once the handshake is complete, the client and server use a shared session key to symmetrically encrypt and decrypt data transmitted between them. The session key(s) were derived from the pre-master key.

This process is a **simplified version** of what is called the *TLS Handshake*.