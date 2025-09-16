If the file or directory name begins with a `.` (full stop) then it is considered to be hidden.
```bash
myuser@hostname:~$ cd ~
myuser@hostname:~$ ls -l 
drwxrwxr-x   4 myuser myuser       4096 Jul 25  2022  aa
-rw-rw-r--   1 myuser myuser     191005 Feb  7  2022  aaa.pdf
-rw-rw-r--   1 myuser myuser   60085406 Oct 23 11:05  adobe.deb
...
myuser@hostname:~$ ls -la 
drwxrwxr-x   4 myuser myuser       4096 Jul 25  2022  aa
-rw-rw-r--   1 myuser myuser     191005 Feb  7  2022  aaa.pdf
drwx------   3 myuser myuser       4096 Oct 23 11:21  .adobe
-rw-rw-r--   1 myuser myuser   60085406 Oct 23 11:05  adobe.deb
...
```
The above example uses the `ls` command with the `-a` flag to include hidden files in the list. Note the directory `.adobe`, which is hidden. By default, `ls` doesn’t print hidden files.
**Tip!** You can combine multiple options on the same flag: `ls -l -a` is equivalent to `ls -la`.