# Exercise 1 - Read-only Environment Variable for all Shells
Create a read-only environment variable that is accessible to all users and all shells on the system. Under `/etc/profile.d` dir, create your script that defines the variable (any var name and value you wish). Then, use the `readonly` command to make the variable read-only so that it cannot be modified by any user or process on the system. Finally, verify that the variable is read-only by attempting to modify its value from your user shell (re-login is needed).
<details>
  <summary>
     Solution
  </summary>

```bash
myuser@hostname:~$ sudo nano /etc/profile.d/myvar.sh
…
```
The file content should be:
```bash
#!/bin/bash
readonly MYVAR="Don't even try to change me"
```
Then, exit the current terminal session and create a new one:
```bash
myuser@hostname:~$ exit
...
myuser@hostname:~$ echo $MYVAR
Don't even try to change me
myuser@hostname:~$ MYVAR=5
-bash: MYVAR: readonly variable
myuser@hostname:~$ sh
-bash: MYVAR: readonly variable
```

</details>

# Exercise 2 - Bad /etc/profile
Create a syntax error in the `/etc/profile` file that prevents it from being executed correctly when a user logs in. Re-login and observe the error message that is displayed. Then, use a backup copy of the `/etc/profile` file (you have an original backup somewhere in your system…) to replace the broken file. 
<details>
  <summary>
     Solution
  </summary>

```bash
myuser@hostname:~$ sudo nano /etc/profile 
# introduce some error... 

myuser@hostname:~$ exit

# relogin the observe the error
-bash: /etc/profile: line 4: syntax error near unexpected token `then'
-bash: /etc/profile: line 4: `f [ "${PS1-}" ]; then'
myuser@hostname:~$ sudo cp /usr/share/base-files/profile /etc/profile
```

</details>

# Exercise 3 - Connect to User-friendly Users
Attempt to log in to the `daemon` user on an **Ubuntu system** (the root account is able to connect to every user without providing the users’ password). Observe the message that is displayed and identify the reason for it. Which shell does the `daemon` user use?

Repeat the exercise for the `nobody` user.
<details>
  <summary>
     Solution
  </summary>

```bash
myuser@hostname:~$ sudo su -l daemon
This account is currently not available.
myuser@hostname:~$ cat /etc/passwd | grep daemon
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

</details>

# Exercise 4 - The root User Command Prompt in sh Shell
1. Open a terminal and start a `sh` session as the root user:  `sudo sh`.
1. Note that the prompt is “#”. Exit the session.
1. Open a terminal and start a `sh` session as your user (assuming you are not root): `sh`.
1. How does the prompt look like? It should be different from the root’s prompt. 

Take a look in the content of `/etc/profile` and search (even if you’re still not familiar with all the code elements there) for the code that defines the shell prompt for root and non-root users. 

Which env var defines the shell prompt? Try to change this variable in your current terminal session and see what happens.
<details>
  <summary>
     Solution
  </summary>

```bash
myuser@hostname:~$ cat /etc/profile | grep -C 1 PS
if [ "${PS1-}" ]; then
  if [ "${BASH-}" ] && [ "$BASH" != "/bin/sh" ]; then
	# The file bash.bashrc already sets the default PS1.
	# PS1='\h:\w\$ '
	if [ -f /etc/bash.bashrc ]; then
--
	if [ "$(id -u)" -eq 0 ]; then
  	PS1='# '
	else
  	PS1='$ '
	fi
myuser@hostname:~$ PS1='prompt '
prompt echo hi
hi
prompt
prompt
prompt
```

</details>
