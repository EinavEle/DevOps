The file system under linux has an hierarchical structure. At the very top of the structure is what's called the **root directory**. It is denoted by a single slash (`/`). It has subdirectories, they have subdirectories and so on. Files may reside in any of these directories.
A **path** is the reference of a particular file or directory on the system.
There are 2 types of paths we can use, **Absolute** and **Relative**. We can refer to a given file either by its Absolute or Relative path, to our choice.
- Absolute paths specify a location (file or directory) in relation to the root directory, they always begin with a forward slash (`/`).
- Relative paths specify a location in relation to the current working directory.
```bash
myuser@hostname:~$ pwd
/home/myuser
myuser@hostname:~$ ls Documents
file1.txt file2.txt file3.txt
...
myuser@hostname:~$ ls /home/myuser/Documents
file1.txt file2.txt file3.txt
...
```
The above example shows two different ways to reference the `Documents` dir. The first is relatively the current working directory (which is `~`), the second is using absolute path.
A few notes regarding paths:
- `~` (tilde) - is a shortcut for your home dir. e.g. if your home directory is `/home/myuser` then you could refer to the directory Documents with the path `/home/myuser/Documents` or `~/Documents.`
- `.` (dot) - is a reference to your current working directory. e.g. in the example above we could also refer to Documents by `./Documents`.
- `..` (dotdot) - is a reference to the parent directory.

Let's see it in action:
```bash
myuser@hostname:~$ pwd
/home/myuser
myuser@hostname:~$ ls ~/Documents
file1.txt file2.txt file3.txt
...
myuser@hostname:~$ ls ./Documents
file1.txt file2.txt file3.txt
...
myuser@hostname:~$ ls /home/myuser/Documents
file1.txt file2.txt file3.txt
...
myuser@hostname:~$ ls ../../
bin boot dev etc home lib var
...
myuser@hostname:~$ ls /
bin boot dev etc home lib var
...
```