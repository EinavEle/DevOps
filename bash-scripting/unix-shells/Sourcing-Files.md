The `source` command allows you to “import” the content of a shell script to another file. It is commonly used to load shell configuration files or execute scripts that define functions, variables, or aliases that should be available in the current shell session. For example, if you have a script named `myscript.sh` that defines some variables and aliases, you could use the `source` command to load it in the `~/.bashrc` file like this:
```bash
source ~/path/to/myscript.sh
```
Here is another simple example. Consider the below two files, `a.sh` and `b.sh`:
```bash
# file a.sh

NAME=John
```
Now we want to use the variable defined in `a.sh` within the `b.sh` file. We can achieve that using the `source` command:
```bash
# file b.sh

source a.sh

echo Hello $NAME
```
Under the hood, The `source` command runs the commands in the specified file in the `same process` that is currently running, rather than spawning a new process to execute the commands. This means that any changes made to the shell environment by the commands in the file will persist in the current shell session after the `source` command completes. You will often see the `.` (dot) command for file sourcing instead of `source`, both commands achieve the same thing.