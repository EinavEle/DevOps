The bash shell allows users to join multiple commands on a single command line by separating the commands with a `;` (semicolon).
```bash
[myuser@hostname]~$ cd /etc/ssh; ls
moduli  	ssh_config.d  sshd_config.d   	ssh_host_ecdsa_key.pub  ssh_host_ed25519_key.pub  ssh_host_rsa_key.pub
ssh_config  sshd_config   ssh_host_ecdsa_key  ssh_host_ed25519_key	ssh_host_rsa_key      	ssh_import_id
[myuser@hostname]/etc/ssh$
```
Nothing special in the above example… just two commands that were executed one after the other. 

The bash shell uses `&&` and `||` to join two commands conditionally. When commands are conditionally joined, the first will always execute. The second command may execute or not, depending on the return value (exit code) of the first command. For example, a user may want to create a directory, and then move a new file into that directory. If the creation of the directory fails, then there is no reason to move the file. The two commands can be coupled as follows:
```bash
[myuser@hostname]~$ echo "one two three" > numbers.txt
[myuser@hostname]~$ mkdir /tmp/boring && mv numbers.txt /tmp/boring
```
By coupling two commands with `&&`, the second command will only run if the first command succeeded (i.e., had a return value of 0).

What if the `mkdir` command failed?

Similarly, multiple commands can be combined with `||`. In this case, bash will execute the second command only if the first command "fails" (has a non zero exit code). This is similar to the "or" operator found in programming languages. In the following example, myuser attempts to change the permissions on a file. If the command fails, a message to that effect is echoed to the screen.
```bash
[myuser@hostname]~$ chmod 600 /tmp/boring/numbers.txt || echo "chmod failed."
[myuser@hostname]~$ chmod 600 /tmp/mostly/boring/primes.txt || echo "chmod failed"
chmod: failed to get attributes of /tmp/mostly/boring/primes.txt': No such file or directory
chmod failed
```