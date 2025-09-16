# Exercise 1 - Run processes in the background
"Interactive processes" are processes that are initialized and controlled through a Linux terminal session. These processes can run in the foreground, occupying the terminal. Alternatively, they can run in the background. The terminal can accept new commands while the program is running.
1. Open a nes terminal session and execute `sleep 600` which initiates a process that "sleeps" 10 minutes and ends.
1. Stop the process and send it into the background by `CTRL+Z`.
1. Bring the process to the foreground by `fg`.
1. Now run the same command while sending the process to the background by the `&` operator: `sleep 600 &`.
1. Bring the process to the foreground.
1. Kill the process by `CTRL+C`.

# Exercise 2 - Run your own service
Follow [Pratham Patel](https://linuxhandbook.com/create-systemd-services/)'s great tutorial to create your own Linux service

# Exercise 3 - Resource Lock and Process State
**Resource locking** is a technique used in computer systems to prevent multiple processes (or users) from simultaneously accessing a shared resource such as a file, database, or piece of memory.

The general idea behind resource locking is to ensure that only one person can access the resource at any given time, to prevent **race conditions** and other synchronization issues that could lead to data corruption or inconsistencies.

As a real life example, in an airline online check-in system, resource locking may be used to prevent multiple users from simultaneously booking the same seat. Only one user should be able to book a certain seat in the aircraft at any given time, to prevent conflicts and ensure data consistency.

Throughout the course, we will encounter resource locking in many cases.

Generally speaking, in Linux systems, two different processes cannot write to the same file concurrently (exactly at the same moment). Each process needs to obtain an exclusive **write lock** for the file. That implies that all the other processes that want to write to this file will have to wait while one process writes its data into it. The more I/O intensive processes you have, the longer the wait time.

In this question we will create processes which are competing on the same resource (same file), and see how some of them are changing their state from Running to Waiting.

Create a file under `~/write_to_file_sequentially.sh` contains the following code, and give it executable (`x`) permissions:
```bash
#!/bin/bash

for i in $(seq 1000); do
  echo "hello world" > overloaded_file
done
```
This script writes the string "hello world" to a file called "overloaded_file". It does so 1000 times **sequentially**, and so will never be competing for access to the file (why?).

Now, because we need multiple processes competing over the same resource, create the following script as well:
```bash
#!/bin/bash

for i in $(seq 1000); do
  ./write_to_file_sequentially.sh &
done
```
Name it `~/multi_process_file_writing.sh` and make it executable. Make sure you understand what this script does.

Run the following commands, in **3 different terminal sessions**:
1. First, in terminal 1, run the program by `./multi_process_file_writing.sh`.
2. Next, run the `top` command in terminal 2. Observe the `multi_process_file_writing` process in top's view.

In the last terminal you will try to catch processes of your program in different states.
In the `ps` [man page](https://man7.org/linux/man-pages/man1/ps.1.html#PROCESS_STATE_CODES), read what each process state code means.

3. In terminal 3, run the `ps -aux` multiple times until you'll see indications that some processes are waiting (sleeping due to IO operation), and some others are running.
&ensp;  While you'll find many processes in a waiting state (`D`), it may be hard to catch a process in a running state (`R`)... Use the `grep` command to filter only relevant lines.