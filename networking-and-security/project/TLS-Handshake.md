![.guides/img/alice-bob-eve](./alice-bob-eve.png)


As you may know, the communication in HTTP protocol is insecure, and since Eve is listening on the channel between you (Alice) and the web server (Bob), you are required to create a secure channel. This is what HTTP does, using TLS protocol. The process of establishing a secure TLS connection involves several steps, known as the TLS Handshake.

TLS security protocols use a combination of **asymmetric** and **symmetric** encryption:

**Step 1 - Client Hello (Client -> Server)**

First, the client sends a **Client Hello** message to the server. The message includes:
- The client's TLS version
- A list of supported ciphers

**Step 2 - Server Hello (Server -> Client)**

The server replies with a **Server Hello**. A Server Hello includes the following information:
- Server Version - a confirmation for the version specified in the client hello.
- Session ID - used to identify the current communication session between the server and the client.
- Server digital certificate - the certificate contains some details about the server, as well as a public key with which the client can encrypt messages to the server. The certificate itself is signed by Certificate Authority (CA).

**Step 3 - Server Certificate Verification**

Alice needs to verify that she's talking with Bob, the real Bob. Why should she suspect? Since Eve is controlling every message that Bob sends to Alice, Eve can impersonate Bob and talk with Alice on behalf of Bob without Alice to knowing that.

Here the CA comes into the picture. The CA is an entity (e.g. Amazon Web Services, Microsoft, etc...) trusted by both sides (client and server) that issues and signs digital certificates, so the ownership of a public key can be easily verified.

In this step the client verifies the server's digital certificate. Which means, Alice verifies Bob's certificate.

**Step 4 - Client-Server master-key exchange**

Cert was verified successfully? Great, we can move on...

Now, the client and the server should agree on a **symmetric key** (called a **master key**) with which they will communicate during the session. The client generates a 32-bytes random master-key, encrypts it using the server's certificate and sends the encrypted message in the channel.

In addition to the encrypted master-key, the client sends a sample message to verify that the symmetric key encryption works.

**Note**: The real TLS protocol doesn't use the master key for direct communication. Instead, other different session keys are generated and used to communicate symmetrically. Both the client and the server generate the keys each in his own machine.

**Step 5 - Server verification message**

The server decrypts the encrypted master-key. From now on, every message between both sides will be symmetrically encrypted by the master-key. The server encrypts the sample message and sends it to the client.

**Step 6 - Client verification message**

The Client verifies that the sample message was encrypted successfully.

#### Let's get started...

Use the `scp` command to copy the directory `tls_webserver` into your home directory of your public EC2. This Python code implements an HTTP web server that represents Bob's side. You will communicate with this server (as Alice), and implement a handshake process manually, over an insecure HTTP channel.

Before you run the server on your public EC2 instance, you should install some Python packages:

```bash
sudo apt update && sudo apt install python3-pip
pip install aiohttp
```

The server can be run by:

```bash
python3 app.py
```

Note that the server is listening on port `8080`, but by default, the only allowed inbound traffic to an EC2 instance is port 22 (why?). [Take a look here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html#add-rule-authorize-access) how to open port `8080` on your public EC2 instance.

After the server is running and port 8080 is allowed, you can test the server by executing the below command from your local machine:

```bash
myuser@hostname:~$ curl <public-ec2-instance-ip>:8080/status
Hi! I'm available, let's start the TLS handshake
```

Your goal is to perform the above 6 steps using bash script, and establish a secure channel with the server.

Below are some helpful instructions you may utilize in each step. Eventually, all your code should be written in `tlsHandshake.sh`.

Make your script robust and clean, use variables, and in every step, check if the commands have succeeded and print informational messages accordingly.

Use `curl` to send the following Client Hello HTTP request to the server:

```json
POST /clienthello
{
   "version": "1.3",
   "ciphersSuites": [
      "TLS_AES_128_GCM_SHA256",
      "TLS_CHACHA20_POLY1305_SHA256"
    ], 
   "message": "Client Hello"
}
```

`POST` is the request method, `/clienthello` is the endpoint, and the json is the body.

**Server Hello** response will be in the form:

```json
{
   "version": "1.3",
   "cipherSuite": "TLS_AES_128_GCM_SHA256", 
   "sessionID": "......",
   "serverCert": "......"
}
```

The response is in json format. You may want to keep the `sessionID` in a variable, and the server cert in a file called for later usage. Use the `jq` command to parse and save specific keys from the JSON response.

Assuming the server certificate was stored in `cert.pem` file, you can verify the certificate by:

```bash
openssl verify -CAfile cert-ca-aws.pem cert.pem
```

While `cert-ca-aws.pem` is a file belonging to the Certificate Authority (in our case, Amazon Web Services), who issued and signed the server cert, you can safely download it from https://raw.githubusercontent.com/alonitac/atech-devops-june-2023/main/networking_project/tls_webserver/cert-ca-aws.pem (`wget`...).

Upon a valid certificate validation, the following output will be printed to stdout:

```text
cert.pem: OK
```

If the verification fails, `exit` the program with exit code `5`, and print informational message:

```text
Server Certificate is invalid.
```

Given a valid cert, generate 32 random bytes base64 string (use `openssl rand`). This string will be used as the master-key, so save it somewhere for later usage.

Got tired? Refresh yourself with some [interesting reading](https://www.bleepingcomputer.com/news/security/russia-creates-its-own-tls-certificate-authority-to-bypass-sanctions/amp/).

This line can help you to encrypt the generated master-key secret with the server certificate:

```bash
openssl smime -encrypt -aes-256-cbc -in <file-contains-the-generated-master-key> -outform DER <file-contains-the-server-certificate> | base64 -w 0
```

When you are ready to send the encrypted master-key to the server, `curl` again an HTTP POST request to the server endpoint `/keyexchange`, with the following body:

```bash
POST /keyexchange
{
    "sessionID": "'$SESSION_ID'",
    "masterKey": "'$MASTER_KEY'",
    "sampleMessage": "Hi server, please encrypt me and send to client!"
}
```

Note that `$SESSION_ID` is a variable containing the session ID you've got from the server's hello response, you need to create this variable once you have the sessions ID from the server. Also, `$MASTER_KEY` is your **encrypted** master key, again, you need to create this variable.

The response for the above request would be in the form:

```json
{
  "sessionID": ".....",
  "encryptedSampleMessage": "....."
}
```

All you have to do now is to decrypt the sample message and verify that it's equal to the original sample message. This will indicate that the server successfully used the master-key.

Please note that the `encryptedSampleMessage` is encoded in base64, before you decrypt it, encode it to binary, as such:

```bash
echo <encryptedSampleMessage-variable> | base64 -d > encSampleMsgReady.txt

#file encSampleMsgReady.txt is ready now to be used in "openssl enc...." command
```

Recall the symmetric encryption demo the **networking and security** tutorial, see how to decrypt a message.

You should `exit` the program upon an invalid decryption with exit code 6, and print informational message:

```text
Server symmetric encryption using the exchanged master-key has failed.
```

If everything is ok, print a positive message:

```text
Client-Server TLS handshake has been completed successfully
```

Well Done! you've manually implemented a secure communication over HTTP! Thank god we have TLS in real life :-)
