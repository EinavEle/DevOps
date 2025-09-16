The `scp` command uses a syntax almost identical to the `cp` command, but either the source file(s) or the destination file can be on a remote machine.

When referring to a file on a remote machine, the following syntax is used:
```bash 
user@host:path
```
As an example, the following command line would transfer the `/etc/services` file from `server1` into the `~/cfg/server1/etc/` directory in `myuser`'s home directory:
```bash
[myuser@hostname]$ scp ec2-user@server1:/etc/services cfg/server1/etc/
services    100% |*****************************| 19936      00:00
```
The `-r` command line switch (for "recursive") must be specified when copying an entire directory (and its subdirectories). In the following, `myuser` recursively copies the `/etc/sysconfig` directory from his local machine to the machine `server1`'s `/tmp` directory:
```bash
[myuser@hostname]$ scp -r /etc/sysconfig ec2-user@server1:/tmp
ifup-aliases    100% |*****************************| 13137  00:00
ifcfg-lo        100% |*****************************| 254    00:00
ifdown          100% |*****************************| 3676   00:00
ifdown-ippp     100% |*****************************| 820    00:00
ifdown-ipv6     100% |*****************************| 4076   00:00
```