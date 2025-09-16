# Exercise 1 - Playing with Symmetric Encryption
1. Encrypt some file using `openssl`.
1. Try to decrypt the encrypted file using a different secret you've used to encrypt. What happened?
1. Add some text to the encrypted file, then try to decrypt it. What happened? [Read here](https://security.stackexchange.com/questions/9437/does-symmetric-encryption-provide-data-integrity) about how `openssl` provides data integrity in symmetric encryption.
1. Encrypt the same file, but using a different key. Make sure different encryption is generated for different keys.
<details>
  <summary>
    Solution
  </summary>

```bash
openssl enc -e -aes-256-cbc -salt -in message.txt -out encrypted_message.txt -pass file:.secret_key

openssl enc -d -aes-256-cbc -salt -in encrypted_message.txt -out original_message.txt -pass file:wrongkey
```
This command tries to decrypt the "encrypted.txt" file using a different secret key "wrongkey". The decryption process will fail and produce an error message.
```bash
echo "New text" >> encrypted.txt
openssl enc -d -aes-256-cbc -in encrypted.txt -out decrypted.txt -k secretkey
```
This command adds the text "New text" to the end of the "encrypted.txt" file and then tries to decrypt it using the original secret key "secretkey". The decryption process will fail and produce an error message because the added text has corrupted the encrypted file and it no longer matches the original ciphertext.
```bash
openssl enc -e -aes-256-cbc -salt -in message.txt -out encrypted_message.txt -pass file:.different_secret_key
```

</details>

# Exercise 2 - Self-signed Certificate
In this exercise you will generate an SSL certificate. In real life, a trusted authority (like Amazon, DigiCert) should sign on your certificates, which gives them validity. But just for the learning, you will generate a certificate and sign it yourself (a.k.a. self-signed certificate). In the public Internet, there is no value for self-signed certificates, but organizations do sign their own certificates for internal usage. We will be using, right guess, `openssl`:
```bash
openssl req -x509 -newkey rsa:1024 -keyout key.pem -out cert.pem -sha256 -days 365
```
The program will ask you some identifiable information: who are you? What is the organization you belong to? Your country, your mail etc... All these details, including a public key, will be encoded into a file called `cert.pem`. Note that this certificate has an expiration time of 365 days.

`cat cert.pem` to see how a certificate may look like. In the simplified TLS handshake model you’ve learned, the server's certificate is the first thing that was sent to the client.
<details>
  <summary>
    Solution
  </summary>

Since this is a simple follow up exercise, solution is not provided

</details>

# Exercise 3 - Authenticity Verification
Under `signature_verification` in our shared repo, you are given 5 signatures and the corresponding messages. Determine which of the signatures are authentic.
<details>
  <summary>
    Solution 
  </summary>

```bash
openssl dgst -sha256 -verify public.key -signature sig1.txt msg1.txt
openssl dgst -sha256 -verify public.key -signature sig2.txt msg2.txt
openssl dgst -sha256 -verify public.key -signature sig3.txt msg3.txt
openssl dgst -sha256 -verify public.key -signature sig4.txt msg4.txt
openssl dgst -sha256 -verify public.key -signature sig5.txt msg5.txt
```

</details>

# Exercise 4 - Verify the Integrity of Apt-get Packages
Debian package verification works by checking the cryptographic hash of the package against the expected value in the package metadata. The package metadata includes the SHA-256 hash of the package contents and is signed by the package maintainer's GPG key.

In our shared repo, under `package_integrity_verification/Packages`, you are given the metadata of 2 Debian packages, visit the docker binaries server: https://download.docker.com/linux/ubuntu/, download the binaries (the .deb file) to your machine according to the path specified in `Filename:`, and verify the package integrity using the `SHA512` value. 
<details>
  <summary>
    Solution
  </summary>

```bash
wget https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/containerd.io_1.2.13-2_amd64.deb

DESIRED_SHA="ab86f4e14362b2eef2173b08c71e5d553a3c9621c2732b0c6261b290bdd0804d7dc80625d73fd6de0c43c0fa915d4482e4fb35a5275403c70b293da18ea86c23"
REAL_SHA=$(sha512sum containerd.io_1.2.13-2_amd64.deb)

test "$DESIRED_SHA  containerd.io_1.2.13-2_amd64.deb" = "$REAL_SHA"
```

</details>