Wildcards are a set of elements that allow you to create a pattern defining a set of files or directories.
Here is the basic set of wildcards:
- `*` represents zero or more characters.
- `?` - represents a single character.
- `[]` - represents a range of characters.

```bash
myuser@hostname:~$ cd /etc
myuser@hostname:/etc$ ls  
total 1664
drwxr-xr-x  3 root     root            4096 ינו  4 14:54 acpi
-rw-r--r--  1 root     root            3028 אוג  1  2017 adduser.conf
drwxr-xr-x  3 root     root            4096 ינו  4 13:29 alsa
drwxr-xr-x  2 root     root           36864 ינו  4 15:40 alternatives
...
myuser@hostname:/etc$ ls b*  
-rw-r--r-- 1 root root  2320 פבר  4  2021 bash.bashrc
-rw-r--r-- 1 root root    45 אוג 12  2015 bash_completion
-rw-r--r-- 1 root root   367 ינו 27  2016 bindresvport.blacklist
...
```
The above example prints all files starting with b.