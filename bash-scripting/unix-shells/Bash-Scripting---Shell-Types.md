Let's recall the 2 main shells we usually work with in Linux system:
- `sh` or Bourne Shell: the original shell still used on UNIX systems.
- `bash` or Bourne Again shell: the standard GNU shell, intuitive and flexible. Probably most advisable for beginner users, while at the same time a powerful tool for the advanced and professional user. On Linux, bash is the standard shell for common users.

The file /etc/shells gives an overview of known shells on a Linux system:
```bash
cat /etc/shells
```
Here is an example of a shell called [Restricted Bash](https://tldp.org/LDP/abs/html/restricted-sh.html):
```bash
rbash 	# this command creates a new terminal session of restricted bash which may be looked exactly like bash terminal
cd /var
```
Was the last command successful? What can you conclude about `rbash`?

Your default shell is set in the `/etc/passwd` file for each user.
```bash
# to know your current Linux user, echo the following environment variable
echo $USER
cat /etc/passwd | grep $USER
```