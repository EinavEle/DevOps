Sometimes you will want to put the output of a command in a file, instead of printing it to the screen. You can do so with the `>` operator:
```bash
myuser@hostname:~$ echo Hi
Hi
myuser@hostname:~$ echo Hi > myfile
myuser@hostname:~$ cat myfile
Hi
```
The `>` operator overwrites the file if it already contains some content. If you want to append to the end of the file,  use the `>>` operator:
```bash
myuser@hostname:~$ echo Hi again >> myfile
myuser@hostname:~$ cat myfile
Hi
Hi again
myuser@hostname:~$ date >> myfile
myuser@hostname:~$ cat myfile
Hi
Hi again
IST 10:06:02 2020 Jan 01
```