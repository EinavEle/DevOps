A **certificate**, simply put, is the server's public key, accompanied by some other attributes such as Organization name, Locality, Country name etc...

The certificate is **digitally signed by Certificate Authority** (CA), an entity that stores, signs, and issues digital certificates. CA acts as a trusted 3rd party both by the client and the server.

Common CA are [DigiCert](https://en.wikipedia.org/wiki/DigiCert), [Let's Encrypt](https://en.wikipedia.org/wiki/Let%27s_Encrypt), AWS and the public cloud providers.

Why do we need that?

When Alice first sends her public key to Bob, there is real risk that Bob will receive Eve's public key, but when Alice first sends her public key to Bob, Bob wants to be sure that the key actually belongs to Alice and has not been tampered with or replaced by Eve.

In a typical scenario, Alice would generate a public-private key pair and send her public key to a trusted CA along with some identifying information, such as her name or email address. The CA would then verify Alice's identity and issue a digital certificate that contains Alice's public key and identifying information, as well as the CA's own digital signature. This certificate serves as proof that Alice's public key belongs to her and has not been tampered with.

Bob can then verify the certificate using the CA's public key (which is typically included in his web browser or operating system) and be reasonably sure that the key actually belongs to Alice and has not been tampered with.