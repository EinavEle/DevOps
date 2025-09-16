Processes are communicating with each other and with the kernel using **signals**. There are multiple signals that you can send to a process. Use the `kill` command to send a signal to a process.
| Signal Name | Signal Number  | Meaning  |
|---------|----------|----------|
| SIGTERM | 15  | Terminate the process in orderly way  |
| SIGINT | 2  | Interrupt the process, the process can ignore this signal  |
| SIGKILL | 9  | Interrupt the process, the process can't ignore this  |
| SIGHUP | 1  | The parent process was terminated  |
Use `man 7 signal` for a comprehensive list of linux signals.
Let's kill a process by send it a KILL signal:
```bash
myuser@hostname:~$ sleep 600
```
The above command initiates a process that just sleeps 600 seconds, and ends.

In **another terminal**, use `ps` to get the PID of the process running the `sleep` command:
```bash
myuser@hostname:~$ ps -a
PID TTY          TIME CMD
46214 pts/1    00:00:00 sleep
46445 pts/3    00:00:00 ps
  ...
myuser@hostname:~$ kill -9 46214
```
Observe how the process running the sleep command is terminated.
##
In bash, you can use keyboard shortcuts to send signals to process:
| Shortcut | Signal  | Meaning  |
|---------|----------|----------|
| CTRL+C | SIGINT  | Terminate the process in an orderly way  |
| CTRL+Z | SIGSTOP  | Suspend the process in the background  |

##### *Graceful Termination*
We will now demonstrate a very important idea called **Graceful Termination**.

Graceful termination refers to the process of shutting down a program (a process) in a way that allows it to complete its current tasks and close down all processes in a safe and controlled manner. This ensures that no data is lost, and all system resources are properly released.

In our shared repo, under `graceful_term_simulate/server.py` you are given a dummy Python "Server". Run this server by:
```bash
# You might try 'python' instead 'python3' command
myuser@hostname:~$ python3 graceful_term_simulate/server.py
Server is running, PID=47098
```
Obviously, we can send SIGKILL (9) to the server and kill it aggressively. But we want the server to be terminated gracefully. To do so, we will first send SIGINT, which indicates to the server "you are going to be terminated soon, so take some **grace period** to terminate yourself gracefully".

The server finishes the process clients requests, closes the connection to the database, and performs some cleanup tasks. Finally, the server terminates itself, while everything is healthy.