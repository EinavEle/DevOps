##### *Regex*
Regular expressions (Regex) allow us to create and match a pattern in a given string. Regex are used to replace text in a string, validate string format, extract a substring from a string based on a pattern match, and much more!

Regex is out of this course’s scope, but you are **highly encouraged** to learn regex yourself. There are so many systems and configurations that are required for regex skills!

Learn Regex: https://regexone.com/

##### `grep` - *Global Regular Expression Print*

A simple but powerful program, `grep` is used for filtering files content or input lines, and prints certain regex patterns.
Let's print the content of `/var/log/auth.log`. This file is a log file that records information about system authentication events. The below commands create some authentication event (by creating the `/test` directory and file in it), then printing the content of `auth.log`.
```bash
myuser@hostname:~$ sudo mkdir /test
myuser@hostname:~$ sudo touch /test/aaa
myuser@hostname:~$ cd /var/log
myuser@hostname:/var/log$ cat auth.log
...
Mar  7 19:17:01 hostname CRON[2076]: pam_unix(cron:session): session closed for user root
Mar  7 19:33:10 hostname sudo:   myuser : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/mkdir /test
```
The above output shows information regarding the executed `sudo` command. `myuser` is the user who performed the `sudo command, the working dir is `/var/log` `and the command coming after sudo was `mkdir /test`. Now let's demonstrate the power of the `grep` command.
Print all lines containing the word "sudo":
```bash
myuser@hostname:/var/log$ grep sudo auth.log
Mar  7 19:17:01 hostname CRON[2076]: pam_unix(cron:session): session closed for user root
Mar  7 19:33:10 hostname sudo:   myuser : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/mkdir /test
...
```
But what if we want to print all "sudo" events while the command coming after sudo is `mkdir`? We can do it using regular expressions:
```bash
myuser@hostname:/var/log$ grep -E "sudo: .*COMMAND=.*mkdir" auth.log
Mar  7 19:33:10 hostname sudo:   myuser : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/mkdir /test
```
The above example uses the `.*` match pattern to catch what we want. `.` means "any single character except a line break", `*` means "0 or more repetitions of the preceding symbol".

Another example - list all users that executed commands using `sudo`:
```bash
# first (bad) try - the second output line is unwanted
myuser@hostname:/var/log$ grep -Eo "sudo:.*:" auth.log
sudo:   myuser :
sudo: pam_unix(sudo:session):
...

# second (success) try
myuser@hostname:/var/log$ grep -Eo "sudo:\s+\w+\s+:" auth.log
sudo:   myuser :
```