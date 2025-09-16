A hash function is a mathematical function that takes in data of any size and produces a fixed-size output. A simple example of a hash function is the MD5 algorithm, which generates a 128-bit hash value. `md5sum` is a Linux command line utility used to generate and verify MD5 checksums of files.
```bash
myuser@hostname:~$ echo "hello world" | md5sum
6f5902ac237024bdd0c176cb93063dc4
myuser@hostname:~$ echo "let it be" | md5sum
90b1d29ca90dac03f168407e4cd8fc15
myuser@hostname:~$ cat 5GB_file | md5sum
b638d7f49a67fe9b4c982ca3bc70066d
```
The hash function is designed to be a one-way function, which means that it is easy to compute the hash of a given input, but it is **computationally infeasible** to compute the input given its hash. Hash functions are **deterministic**, which means that the same input data will always produce the same hash output:
```bash
myuser@hostname:~$ X=$(echo "hello world" | md5sum)
myuser@hostname:~$ Y=$(echo "hello world" | md5sum)
myuser@hostname:~$ test "$X" = "$Y"
myuser@hostname:~$ echo $?
0
```
The distribution of hashed values is designed to be **uniform**, which means that different input values should produce very different hash values. Even small changes in the input should produce significant changes in the output hash value:
```bash
myuser@hostname:~$ echo "hello world" | md5sum
6f5902ac237024bdd0c176cb93063dc4
myuser@hostname:~$ echo "hello worln" | md5sum
a10a0af8e9b486a707aaccb7a752d37e
```
However, it is possible for different input values to produce the same hash value, which is called a **hash collision**.

Hash functions are commonly used to store passwords securely. Instead of storing the actual passwords, the hash of the password is stored in the database. When a user attempts to log in, the password entered is hashed and compared to the hashed password in the database. If they match, the user is granted access.