**"On a Linux system, everything is a file; if something is not a file, it is a process."**

In linux, under the hood, everything is actually a **file**. A text file is a file, a directory is a file, your keyboard is a file (one that the system reads from only), your monitor is a file (one that the system writes to only), when you want to send data over the internet, you write it to a unique file, etc.

How could that statement be true? because there are **special files** that are more than just files (e.g. sockets, devices etc.).

```bash
myuser@hostname:~$ ls -l
total 80
-rw-rw-r--  1 myuser     myuser   31744 Feb 21 17:56 intro Linux.doc
-rw-rw-r--  1 myuser     myuser   41472 Feb 21 17:56 Linux.doc
drwxrwxr-x  2 myuser     myuser   4096  Feb 25 11:50 course
```

In the above output, the first dash (`-`) represents the file type. We can notice that `course` is a directory, since the first dash is d: `drwxrwxr-x`, while  `Linux.doc` is a regular file, since it starts with -. 
Here are a few common types in Linux OS:
| Symbol | Meaning |
|---------|----------|
| - | Regular file |
| d |Directory|
| l | Link |
| c | Character device |
| s | Socket |
| p | Named pipe |
| b | Block device |

In this course, we will deal with plain files, executable files, directories, links, and a bit of sockets.

Another important feature of the linux file system (**fs**): filename is Case Sensitive, and files has no extension, use the `file` command to know the content type:

```bash 
myuser@hostname:~$ touch file1.png
myuser@hostname:~$ echo "hi" > file1.png
myuser@hostname:~$ ls
file1.png
...
myuser@hostname:~$ file file1.png
file1.png: ASCII text
myuser@hostname:~$ file File1.png
File1: ERROR: cannot open 'File1.png' (No such file or directory)
```

In the above example, we used the `touch` command to create an empty file called `file1.png`, and the text "hi" was written into it (this command uses the > operator which will be discussed later on). Then we use the `file` command to inspect the type of the file. We can see that even though the file extension is `.png` (which is known for images), linux recognizes the file type as a regular text file, which is the correct type. In linux OS, file extensions are meaningless.