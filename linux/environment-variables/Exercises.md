# Exercise 1 - Manipulate env vars
In your current terminal session, type `printenv` to list your environment variables. Find specific env vars to manipulate, such that the command `cd ~` will actually change to the `/tmp` directory, instead of to your regular home directory.

This hack should work for any child process spawned from your current terminal session.  

<details>
  <summary>
     Solution
  </summary>

```bash
export HOME=/tmp
```

</details>

# Exercise 2 - Elvis custom ls command
The PATH variable on elvis’ machine looks like:
```bash
[elvis@station elvis]$ echo $PATH 
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```
`elvis` created a custom program called `ls`. The program is located in `/home/elvis/custom` directory.
1. What is the command that `elvis` should execute such that **his** version of `ls` would be executed in the current terminal session only? 
1. What is the command that `elvis` should execute such that **Ubuntu**’s version of `ls` would be executed in the current and child terminal sessions? 

<details>
  <summary>
     Solution
  </summary>

```bash
PATH="/home/elvis/custom":$PATH
```
```bash
export PATH=$PATH:"/home/elvis/custom"
```

</details>