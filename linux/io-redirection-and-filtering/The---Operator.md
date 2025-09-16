Sometimes you may want to issue another command on the output of one command. You can do so with the `|` (pipe) operator:
```bash
myuser@hostname:~$ cat myfile | grep again
Hi again
```
In the above command, the output of the `cat` command is the input to the `grep` command.

`>`, `>>`, and `|` are all called IO (Input and Output) redirection operators. There are [more operators](https://tldp.org/LDP/abs/html/io-redirection.html)... but the above 3 are the most common.