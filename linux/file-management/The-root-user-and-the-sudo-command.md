Sometimes, you need to execute a command as another user. For example:
```bash
myuser@hostname:~$ ls -l
-rw-------  1   john  johnsfriends 5 Jan 23 12:39 phone
myuser@hostname:~$ cat phone
cat: phone: Permission denied
```
In the above example, your personal user is `myuser` (according to the name in the prompt), but the file `phone` is owned by the user `john`. Not only it is owned by `john`, according to the file’s permissions, only john (or users under the group `johnsfriends`) can read/write to the file.

The `sudo` command is short for “**switch user and do**”. In a single command, you can switch to a specific user, perform a command on behalf of that user, and “return” to your user. Here is an example:
```bash
myuser@hostname:~$ sudo -u john cat phone
+972524869328
```
In the above example, we under the hood switched to the user `john`, executed `cat phone` on his behalf, then back to our user, `myuser`. In a single command, quite useful.

According to `sudo`’s help page, if you don’t specify a user (using the `-u` flag), the default user that you are switching to is `root`. 

In Ubuntu, the `root` user is disabled by default for security reasons. Instead, administrative tasks are typically performed using the `sudo` command.  How does it work? 

Every user that is a member of a special group called `sudo` (to be confused with the sudo command, there is also a group called sudo), can use the `sudo` command to execute commands on behalf of the root user, without actually login to this strong user. Your default linux user is a member of the group sudo.  

It's important to exercise caution when using the root user account, as any command or operation executed with root privileges has the potential to cause significant damage to the system if performed incorrectly. It's recommended to use the root user account only when necessary and to carefully consider the potential consequences of each action before executing it.