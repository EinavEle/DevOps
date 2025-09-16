Permissions specify what a particular user may or may not do to a given file or directory. On a Linux system, every file is owned by a **user**, a **group** and “**others**”.
```bash
  myuser@hostname:~$ ls -l
-rw-rw-r--  1   myuser  users 5 Jan 15 12:39 To_Do
-rwxr-xr-x  1   root    root 45948 Aug 9 15:01 /bin/ls*
```
In the above example, the first file is a regular file (first dash). Users with username `myuser` or users belonging to the group `users` can read and write (change/move/delete) the file, but they can't execute it (second and third dash). All other users are only allowed to read this file, but they can't write or execute it (fourth and fifth dash).
The second example is an executable file, the difference: everybody can run this program, but you need to be `root` to change it.
On a Linux system there are only 2 people usually who may change the permissions of a file or directory. The owner of the file or directory and the root user. The root user is a superuser who is allowed to do anything and everything on the system.
Linux permissions dictate 3 things you may do with a file, read (`r`), write (`w`) and execute (`x`). They are referred to in Linux by a single letter each.
For every file we define 3 sets of people for whom we may specify permissions.
- user (`u`) - a single person who owns the file. (typically the person who created the file but ownership may be granted to someone else by certain users)
- group (`g`) - every file belongs to a single group.
- others (`o`) - everyone else who is not in the group or the owner.

Use the `chmod` command to change file’s permissions:
```bash
myuser@hostname:~$ ls -l
-rw-rw-r--  1   myuser  users 5 Jan 15 12:39 hello
myuser@hostname:~$ chmod u+x hello
myuser@hostname:~$ ls -l
-rwxrw-r--  1   myuser  users 5 Jan 15 12:39 hello
```
The logic behind the command:
1. Who are we changing the permission for? [`ugoa`] - user (or owner), group, others, all
1. Are we granting or revoking the permission - indicated with either a plus (`+`) or minus (`-`)
1. Which permission are we setting? - read (`r`), write (`w`) or execute (`x`)

**File permissions in octal form**
In Unix-like operating systems, file permissions can be represented in octal form, which is `XXX`, when X is a number between 0 and 7. To calculate the octal value of file permissions, look at every `3-tuple` (the one for the user, group and others) as a binary number. e.g.
- `rwx` - 111
- `r--` - 100
- `rw-` - 110

Now convert this number to 10-bases number:
- `rwx` - 111 = 7
- `r--` - 100 = 4
- `rw-` - 110 = 6

Now simply add up the values for each permission that is granted, and use that as the digit in the corresponding position. For example:
`rwxrw-rw-` would be represented as 766 in octal notation. 7 for `rwx` of the user, 6 for `rw-` of the group, 6 again of `rw-` for others.

**Default permissions**
- The standard file permission is determined by the mask for new file creation. The value of this mask can be displayed using the `umask` command. Before the mask is applied, a directory has permissions `777` or `rwxrwxrwx`, a plain file `666` or `rw-rw-rw-`. The umask value is subtracted from these default permissions after the function has created the new file or directory.
- A directory gets more permissions by default: it always has the execute permission. If it didn't have that, it would not be accessible. Try this out by chmodding a directory to 644!