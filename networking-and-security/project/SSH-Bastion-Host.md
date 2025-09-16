Before you answer the below two sections, please read the tutorial about the **SSH protocol**.

SSH jump host (also known as SSH **bastion** host or SSH gateway) is a special type of server that allows users to access other servers in a private network through it. It acts as an intermediary host between the client and the target server. By using a jump host, users can securely connect to remote servers that are not directly accessible from the internet or from their local machine. The jump host acts as a secure entry point to the private network, enforcing authentication and access controls, and reducing the attack surface of the servers behind it.

Implement a bash script in `bastion_connect.sh` that connects to the private instance using the public instance. Your script should not use an explicit path to the `.pem` ssh key file, instead, it reads an environment variable called `KEY_PATH`. If the variable doesn't exist, print an error message and exit with code `5`.

Here is how your script will be tested:

**Case 1** - connect to the private instance from your local machine

```console
myuser@hostname:~$ export KEY_PATH=~/key.pem
myuser@hostname:~$ ./bastion_connect.sh <public-instance-ip> <private-instance-ip>
ubuntu@private-instance-ip:~$
```

**Case 2** - connect to the public instance

```console
myuser@hostname:~$ export KEY_PATH=~/key.pem
myuser@hostname:~$ ./bastion_connect.sh <public-instance-ip>
ubuntu@public-instance-ip:~$
```

**Case 3** - run a command in the private machine

```console
myuser@hostname:~$ export KEY_PATH=~/key.pem
myuser@hostname:~$ ./bastion_connect.sh <public-instance-ip> <private-instance-ip> ls
some-file-in-private-ec2.txt
```

**Case 4** - bad usage

```bash
myuser@hostname:~$ ./bastion_connect.sh <ip>
KEY_PATH env var is expected
myuser@hostname:~$ echo $?
5
myuser@hostname:~$ export KEY_PATH=~/key.pem
myuser@hostname:~$ ./bastion_connect.sh
Please provide bastion IP address
myuser@hostname:~$ echo $?
5
```