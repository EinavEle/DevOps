The basic usage of the `ssh` command is as follows:
```bash
ssh [user@]hostname [command]
```
- `user`: The username to use for the remote connection (optional).
- `hostname`: The hostname or IP address of the remote system.
- `command`: The command to execute on the remote system (optional). If you omit the command, ssh will open a shell session on the remote system, allowing you to interact with it as if you were physically sitting in front of it.

If you are connecting to the system for the first time, ssh will ask you to verify the authenticity of the remote host by displaying the fingerprint of the remote system's public key.
```bash
[myuser@hostname]$ ssh ec2-user@server1
The authenticity of host 'server1 (192.168.0.254)' can't be established.
RSA key fingerprint is fc:c8:87:90:f0:39:af:4f:de:99:cc:30:ce:64:b2:8e.
Are you sure you want to continue connecting (yes/no)?
```
Once you have verified the fingerprint, ssh will establish a secure connection to the remote system and open a shell session. Verified server's fingerprints are stored in the client's machine under `~/.ssh/known_hosts`.

On subsequent connections to the same server, the SSH client will check the fingerprint of the server's public key against the fingerprints stored in the `known_hosts` file. If the fingerprint of the server's public key has changed, the SSH client will display a warning message and refuse to connect to the server. This helps to protect against man-in-the-middle attacks.