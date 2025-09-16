Since the essence of SSH is communication between two machines, you will be running a Docker container on your local machine, and communicating with this container from your local machine. If you are not familiar with containers, don’t worry, they will be taught later on. For now, think about Docker containers as a small, lightweight OS running within your real OS  (but you shouldn't believe that…Docker containers are **far away** from being small OS!).

Pre-requisites:
1. Install Docker on your machine if you don’t have it yet. 
1. Generate RSA key pair using the `ssh-keygen` command. **Important**: usually the default directory to store keys is the `~/.ssh`. But in this exercise set, you must store the generated key outside the `~/.ssh` directory. 
1. Run the container by:
    ```bash
    docker run --rm --name=ssh-server -p 2222:2222 -e USER_NAME=elvis -e PUBLIC_KEY="$(cat /path/to/your/public-key-file)" lscr.io/linuxserver/openssh-server:latest

    docker run --rm --name=ssh-server -p 2222:2222 -e USER_NAME=elvis -e PUBLIC_KEY="$(cat /home/alon/.ssh/id_rsa.pub)" -e SUDO_ACCESS=ture lscr.io/linuxserver/openssh-server:latest bash -c "sed -i 's/AllowTcpForwarding no/AllowTcpForwarding yes/g' /etc/ssh/sshd_config &&  nc -l -k 8087"
    ```
1. In another terminal session, execute the below command to extract the IP address of your container:
    ```bash
    docker inspect ssh-server | jq -r '.[0].NetworkSettings.IPAddress'
    ```

Solve the below exercises while the container is running. The IP address you just extracted is the “remote” machine IP that should be used to connect to the machine, the port is 2222, the user is `elvis`.

# Exercise 1 - Simple Connection
Use the `ssh` command to  connect to your machine. 
<details>
  <summary>
    Solution
  </summary>

```bash
ssh -i /path/to/your/private-key-file -p 2222 
elvis@<ssh-server-ip>
```

</details>

# Exercise 2 - Change Fingerprint
Stop the docker container process (you can do it by CTRL+c), and start again, try to connect again to the remote machine using the ssh command from the previous exercise. What happened, why? How can you fix it? 
<details>
  <summary>
    Solution
  </summary>

You were unable to connect to an SSH server and received an error related to the `known_hosts` file and `fingerprint`. The SSH client is failing to establish a connection because the remote server's fingerprint has changed when you stopped and re-run the Docker container again.
There are a few way to deal with it, one of them it so clean the known_hosts file:
```bash
cat /dev/null > ~/.ssh/known_hosts
```

</details>

# Exercise 3 - Port Forward
SSH port forwarding allows you to securely tunnel traffic between a local and a remote machine over an encrypted SSH connection, enabling access to remote services as if they were running on the local machine.

Connect to the remote server while forwarding port 8087 from the remote into port 8085 in the local machine. 
<details>
  <summary>
    Solution
  </summary>

`ssh -i /path/to/your/private-key-file -p 2222 -L 8085:localhost:8087 elvis@<ssh-server-ip>`
Check successful forwarding by running the below command from your local machine:
```bash
$ netstat -tuna | grep 8085
tcp    	0  	0 127.0.0.1:8085      	0.0.0.0:*           	LISTEN
tcp6   	0  	0 ::1:8085            	:::*                	LISTEN
```

</details>

# Exercise 4 - Add New keys
Generate another RSA key-pair. Allow ssh connection using this new key-pair. The `authorized_keys` file is located in the remote machine under `/config/.ssh/`.
<details>
  <summary>
    Solution
  </summary>

1. Generate new key-pair using ssh-keygen, copy the public key content to the clipboard.
1. Connect to the remote machine using the old identity
1. Perform `echo "<your-public-key>" >> /config/.ssh/authorized_keys`
1. `exit` the remote host.
1. Connect using your new identity, e.g. `ssh -p 2222 -i new_private_key elvis@172.17.0.2`

</details>

# Exercise 5 - Password auth
Password authentication in SSH is the ability to authenticate with a username and password pair. It is not recommended to use password authentication because it is vulnerable to brute-force attacks, where an attacker can repeatedly guess passwords until they gain access to the system. It is safer to use key-based authentication, which is more secure and allows for automated access without exposing passwords.

You know that the password for elvis username is a 4 digit number. Simply trying all possible passwords (1000-9999) is the sure way to discover elvis’ password. It will take no more than 10 minutes. 
1. Try to authenticate without your key-pair. You should see the Password prompt, asking you to insert the password. Try your luck...
1. Install `sshpass` if you don’t have one.
1. Execute the below bash script until you find the correct password.
```bash
for i in $(seq 1000 3000); do
echo trying $i
sshpass -p $i ssh -o StrictHostKeyChecking=no -p 2222 elvis@172.17.0.2
done
```
# Exercise 5 - Change the ssh Daemon
To change the SSH daemon configuration, you can modify the `sshd_config` file on the server. This file typically resides in the `/etc/ssh/` directory. You can edit this file with `nano` to change various settings such as the port number, authentication methods, and allowed users/groups. After making changes to the `sshd_config` file, you'll need to restart the SSH daemon for the changes to take effect. Usually it’s done by `systemctl restart sshd`, but since you are working on a Docker container, it’s done by running the following command **from within the machine**:
```bash
kill -HUP $(cat /config/sshd.pid)
```
Your goal is to configure the sshd to not allow password authentication at all!
<details>
  <summary>
    Solution
  </summary>

In `/etc/ssh/sshd_config` you should change:
```bash
PasswordAuthentication yes
```
to 
```bash
PasswordAuthentication no
```

</details>