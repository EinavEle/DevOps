# Exercise 1 - Navigate the system

1. Open the terminal, go to `/dev`
1. Change back into your home directory.
1. Make subdirectories called `work` and `play`.
1. Delete the subdirectory called `work`.
1. Copy the file `/etc/passwd` into your home directory, keep the original filename.
1. Move it into the subdirectory `play`.
1. Change into subdirectory `play` and create a symbolic link called `terminal` that points to your tty device (`/dev/tty` - read some information on tty devices). What happens if you try to make a hard link to the tty device?
1. What is the output of the command: `echo {con,pre}{sent,fer}{s,ed}`? Now, from your home directory, copy `/etc/passwd` and `/etc/group` into your home directory in one command given that you can only type `/etc` once.
1. From your current working directory, copy the entire directory play to a directory called `work`, preserving the symbolic link.
1. Describe three different ways of setting the permissions of passwd to `r--r--r--`.

<details>
  <summary>
    Solution
  </summary>

```bash
myuser@hostname:~$ cd /dev
myuser@hostname:/dev$ cd ~
myuser@hostname:~$ mkdir work play
myuser@hostname:~$ rmdir work
myuser@hostname:~$ cp /etc/passwd .
myuser@hostname:~$ mv passwd play
myuser@hostname:~$ cd play
myuser@hostname:~/play$ ln -s /dev/tty terminal
myuser@hostname:~/play$ ln /dev/tty terminal2
ln: failed to create hard link 'terminal2' => '/dev/tty': Invalid cross-device link
myuser@hostname:~/play$ cp /etc/{passwd,group} .
myuser@hostname:~/play$ cp -a . ../work
myuser@hostname:~/play$ chmod 444 passwd
myuser@hostname:~/play$ chmod a+r passwd
myuser@hostname:~/play$ chmod u+r,g+r,o+r passwd
```

</details>

# Exercise 2 - Your neighbors home directory

By default, believe it or not, different linux users on the same OS can read each others’ home directory. 

Modify the permissions on your home directory to make it completely private. Create a new Linux user called `foreign` and login into it. Check that `foreign` can't access your directory. Put the permissions back to how they were.

<details>
  <summary>
    Solution
  </summary>

```bash
cd ~

# change the permissions of current work dir (home)
chmod 700 .

# check that the permissions were applied
ls -ld ~

# create the user foreign
sudo adduser foreign

# login to foreign user 
su -l foreign

# go to foreign’s home dir - expect error
cd /home/<your-original-user>

# exit foreign’s terminal
exit

# change permissions back 
chmod 755 .
```

</details>

# Exercise 3 - Files archive

Archive the contents of your home directory (including any subdirectories) using `tar`. Now extract the contents into backup directory.

<details>
  <summary>
    Solution
  </summary>

```bash
cd ~
tar -czf my_home_dir.tar.gz *
mkdir backup && cd backup
tar -xzf my_home_dir.tar.gz -C mkdir backup
```

</details>

# Exercise 4 - Broken Symlink

Uber has an automated daily backup system. Every day another backup file is being created in the file system according to the following format: 
`backup-YYYY-MM-DD.obj`.  e.g. `backup-2023-03-01.obj`.
To be able to restore the system from a backup copy in a convenient way, they want to point to the last generated backup file using a static file named backup.obj. To do so, they create a symbolic link pointing to the last generated backup file.  
1. Let's create the daily backup file:
    ```bash
    FILENAME=backup-$(date +"%Y-%m-%d").obj
    touch $FILENAME
    echo "backup data..." >> $FILENAME
    ```
1. Then, create a symlink (soft link) to the daily backup file:
    ```bash
    ln -s $FILENAME backup.obj
    ```
At some point in the development lifecycle of the product, the DevOps team has decided to organize all backup links in a directory called `backups`. They moved the link `backup.obj` into `backups` directory:
```bash
mkdir backups
mv backup.obj backups/
```
<details>
  <summary>
    Solution
  </summary>

The problem in the ln command (step 2): a relative path for the target file was used, then the target file location has been changed.  

`FILENAME` variable should be an absolute path, e.g.

`FILENAME=$(pwd)/backup-$(date +"%Y-%m-%d").obj`

</details>