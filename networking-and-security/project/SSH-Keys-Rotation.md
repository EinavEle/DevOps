**Key rotation** is a security practice that involves regularly replacing cryptographic keys used for encryption, authentication, or authorization to mitigate the risk of compromise. It helps to ensure that compromised keys are not used to gain unauthorized access and that any data that has been encrypted with the old keys is no longer accessible. Key rotation is typically used in many security-related systems such as SSH, SSL/TLS, and various forms of encryption, and is a key component of maintaining a secure environment.

In your public EC2 instance, create a bash script under `~/ssh_keys_rotation.sh` that automatically rotates the keys of the **private instance**.

Here is how your script will be tested:

**Case 1** - rotate keys

```console
ubuntu@<public-ip-host>:~$ export KEY_PATH=~/key.pem
ubuntu@<public-ip-host>:~$ ./ssh_keys_rotation.sh <private-instance-ip>
...
ubuntu@<public-ip-host>:~$ ls
new_key
new_key.pub
```

At the end of the run, there are 2 files in the instance home directory:

- `new_key` is the new private key that you should be used to connect to the private instance.
- `new_key.pub` is the new public key that its value was stored in ~/.ssh/authorized_keys file in the private instance.

Make sure you are able to connect to the machine after the rotation:

```console
ubuntu@<public-ip-host>:~$ ssh -i <new_key> ubuntu@<private-ip-host>
ubuntu@<private-ip-host>:~$
```

You should not be able to connect using the old SSH key:

```console
ubuntu@<public-ip-host>:~$ ssh -i <old_key> ubuntu@<private-ip-host>
ubuntu@<private-ip-host>: Permission denied (publickey).
```

**Case 2** - bad usage

```console
ubuntu@<public-ip-host>:~$ ./ssh_keys_rotation.sh
Please provide IP address
```

**Note**: Make sure the rotation process doesn't break the `bastion_connect.sh` script from the previous question. The script should work fluently after rotation.

In any case that you break the private instance, feel free to delete your EC2 instance and create a new one instead.