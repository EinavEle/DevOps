When you want the system to execute a command, you almost never have to give the full path to that command. For example, we know that the `ls` command is actually an executable file, located in the `/bin` directory (check with `which ls`), yet we don't have to enter the command `/bin/ls` for the computer to list the content of the current directory.

The `$PATH` environment variable is a list of directories separated by colons (`:`) that the shell searches when you enter a command. When you enter a command in the shell, the shell looks for an executable file with that name in each directory listed in the `$PATH` variable, in order. If it finds an executable file with that name, it runs it.

System commands are normal programs that exist in compiled form (e.g. `ls`, `mkdir`, etc...).
```bash
myuser@hostname:~$ which ls
/bin/ls
myuser@hostname:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:.....
```
The above example shows that `ls` is actually an executable file located under `/bin/ls`. The `/bin` path is part of the PATH env var, thus we are able to type `ls` shortly.