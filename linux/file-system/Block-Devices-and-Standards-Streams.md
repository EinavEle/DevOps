Let’s take a closer look on the `/dev` directory:
```bash
myuser@hostname:~$ ls -l /dev
brw-rw----  1 root disk    	8,   0 Apr  1 18:30 sda
brw-rw----  1 root disk    	8,   1 Apr  1 18:30 sda1
brw-rw----  1 root disk    	8,   2 Apr  1 18:30 sda2
…
lrwxrwxrwx  1 root root     	15 Apr  1 18:29 stderr -> /proc/self/fd/2
lrwxrwxrwx  1 root root      	15 Apr  1 18:29 stdin -> /proc/self/fd/0
lrwxrwxrwx  1 root root       	15 Apr  1 18:29 stdout -> /proc/self/fd/1
```
We will discuss some important files - block devices.

Note the files `sda`, `sda1`, `sda2`. Those are block device file type (the first dash is `b`).

Device files do not contain data in the same way that regular files, or even directories. Instead, the job of a device node is to act as an interface to a particular device driver within the kernel.

When a user writes to a device node, the device node transfers the information to the appropriate device driver in the kernel. When a user would like to collect information from a particular device, they read from that device's associated device node, just as reading from a file.

Block devices are devices that read and write information a chunk ("block") at a time. Block devices customarily allow random access, meaning that a block of data could be read from anywhere on the device, in any order.

In Linux, "sda," "sda1," and "sda2" are devices that refer to different **partitions** of a storage device, such as a hard drive or SSD.
The "sda" device refers to the entire storage device, while "sda1" and "sda2" are partitions of that device.
- "sda1" is the first partition on the "sda" device
- "sda2" is the second partition on the "sda" device
- etc…
```bash
myuser@hostname:~$ lsblk
sda                   	8:0	0 465.8G  0 disk  
├─sda1                	8:1	0   487M  0 part  /boot
└─sda2                	8:5	0 465.3G  0 part
```

We will now discuss other important files: `stdin`, `stdout`, `stderr`. 
Those are the standard input/output streams that are used by programs to read input (from your keyboard) and write output (to your screen).
Here's what each stream does:
1. **Standard Input (stdin)**: This is the stream that carries input to a program. By default, it is associated with the keyboard, so when a user types something into the terminal, it is sent to the program via the standard input file.
1. **Standard Output (stdout)**: This is the stream that carries normal output from a program. By default, it is associated with the terminal, so when a program prints something to the console, it is sent to the standard output file.
1. **Standard Error (stderr)**: This is the stream that carries error messages and other diagnostic output from a program. By default, it is also associated with the terminal, so when a program encounters an error or warning, it prints a message to standard error.

By default, these streams are connected to the terminal, but they can be redirected to files or other streams as well. This is a powerful feature of the Unix shell that allows programs to be combined and orchestrated in powerful ways.

Do you see how **"On a Linux system, everything is a file"**. Keep in mind this statement, it’ll help you to understand linux’s behavior.