When running a script in a subshell, you should define which shell should run the script. The shell type in which you wrote the script might not be the default on your system, so commands you entered might result in errors when executed by the wrong shell.

The **sha-bang (#!)** at the head of a script tells your system that this file is a set of commands to be fed to the command interpreter indicated.

Note that the path given at the "sha-bang" must be correct, otherwise an error message -- usually "Command not found." -- will be the only result of running the script.

Copy and execute the following snippet to a `myscript.sh` file in your local Linux machine.
```bash
#!/bin/bash

ls
cd /var
```
Test the above script with `/bin/sh` as the sha-bang shell. Add an `echo` command to print some environment variable that will indicate the shell that is currently running the program.