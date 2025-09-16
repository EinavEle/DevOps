In Unix-like operating systems, every command that is executed returns an exit status to the shell that invoked it. The exit status is a numeric value that indicates the success or failure of the command. A value of 0 indicates success, while a non-zero value indicates failure.

The exit status of the most recently executed command can be accessed via the `$?` variable in Bash.
```bash
[myuser@hostname]~$ ls /non-existing-dir
ls: cannot access '/non-existing-dir': No such file or directory
[myuser@hostname]~$ echo $?
2
```
In the above example, if you run a command like `ls /non-existing-dir`, you will receive an error message saying that the directory does not exist, and the exit status will be non-zero. You can access the exit status of this command by typing `echo $?`. The output will be the exit status of the previous command (in this case, the value is 2).
Some common non-zero exit status values include:
- 1: General catch-all error code
- 2: Misuse of shell built-ins (e.g. incorrect number of arguments)
- 126: Command found but not executable
- 127: Command not found
- 128+: Exit status of a program that was terminated due to a signal