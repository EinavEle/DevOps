1. Type `cd ~` to change the current working dir to your home directory.
1. Use the `cat` command to print the content of `/etc/passwd` in 2 ways - using absolute path, and relative path.  
1. Try to think about a general principle regarding when to use absolute or relative paths.

<details>
  <summary>
    Solution
  </summary>

```bash
cat ../../etc/passwd
cat /etc/passwd
```

Use absolute paths when you need to refer to a file or directory from anywhere in the file system, when you are not sure what will be the current working directory where the command is executed from. 

Use relative paths when you need to refer to a file or directory that is located in the same directory or a subdirectory of the current working directory.
</details>