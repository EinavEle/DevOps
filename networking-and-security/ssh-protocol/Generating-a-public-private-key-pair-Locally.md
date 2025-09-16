When using ssh, a user's public-private key pair can be generated with the `ssh-keygen` command.
```bash
[myuser@station myuser]$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/myuser/.ssh/id_rsa): ENTER
Enter passphrase (empty for no passphrase): ENTER
Enter same passphrase again: ENTER
Your identification has been saved in /home/myuser/.ssh/id_rsa.
Your public key has been saved in /home/myuser/.ssh/id_rsa.pub.
The key fingerprint is:
e0:71:43:df:ed:40:01:0b:44:54:db:c2:80:f2:33:aa myuser@station
```
The user `myuser` was first prompted for the new (private) key's filename, to which `myuser` simply hit ENTER to accept the default filename: `~/.ssh/id_rsa`. **Make sure that you don't override important existing keys when you are playing with `ssh-keygen`.**

Next, `myuser` was given the opportunity to attach a passphrase to his private key. By hitting ENTER again (twice), `myuser` chose not to.

The private key was generated under `/home/myuser/.ssh/id_rsa`, while the public key under `/home/myuser/.ssh/id_rsa.pub`.

You should **NEVER** send your private key, not even on a secured channel.

# Spot check

Generate an SSH key-pair on your local machine. Take a look at the public and private keys. What are the permissions of the public and private keys? Does it make sense? 

What is the most restrictive permission you can give to your public key file? To your private key file?
<details>
  <summary>
    Solution
  </summary>

Generating keys using ssh-keygen was explained step-by-step in the above section.

The permissions of the public and private keys are typically set to 600 (read and write permissions for the owner only) by default. This makes sense because the private key should be kept confidential and not shared with anyone else, while the public key can be freely distributed to remote servers.

The most restrictive permission that can be given to the private key file is read-only permission for the owner, which is represented by the permission code 400. This permission allows the owner to read the contents of the file but not modify it or execute it.

</details>