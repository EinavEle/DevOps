Command substitution allows users to run arbitrary commands in a subshell and incorporate the results into the command line. The modern syntax supported by the bash shell is: 
```bash
$(subcommand)
```
As an example of command substitution, `myuser` would like to create a directory that contains the date in its name. After examining the `date(1)` man page, he devises a format string to generate the date in a compact format.
```bash
[prince@station prince]$ date +%d%b%Y
04May2023
```
He now runs the mkdir command, using command substitution.
```bash
[prince@station prince]$ mkdir reports.$(date +%d%b%Y)
[prince@station prince]$ ls
reports.04May2003
```
The bash shell implements command substitution by spawning a new subshell, running the command, recording the output, and exiting the subshell. The text used to invoke the command substitution is then replaced with the recorded output from the command.