Variable expansion is a feature in Bash that allows you to manipulate a variable’s value when referencing it. Here are a few basic examples:

**Default error message**
```bash
${VAR:?word}
```
If `VAR` is null or unset, the expansion of `word` is written to the standard error and the shell, if it is not interactive, exits.

```bash
myuser@hostname:~$ VAR=
myuser@hostname:~$ echo ${VAR:?VAR is unset or null}
myuser@hostname:~$ echo $?
```

**Default assignment**
```bash
${VAR:-word}
```
If `VAR` is unset or null, the expansion of `word` is substituted.  Otherwise, the value of `VAR` is used.
```bash
myuser@hostname:~$ VAR=123
myuser@hostname:~$ echo ${VAR:-undefinedValue}
123
myuser@hostname:~$ unset VAR
myuser@hostname:~$ echo ${VAR:-undefinedValue}
undefinedValue
myuser@hostname:~$ echo $VAR
undefinedValue
```
**Variable substring**
```bash
${parameter:offset}
${parameter:offset:length}
```
This expansion allows you to extract a portion of a string variable based on a specified index and length.
```bash
$ string=01234567890abcdefgh
$ echo ${string:7}
7890abcdefgh
$ echo ${string:7:0}

$ echo ${string:7:2}
78
$ echo ${string:7:-2}
7890abcdef
$ echo ${string: -7}
bcdefgh
$ echo ${string: -7:0}

$ echo ${string: -7:2}
bc
```
**String length**
```bash
${#parameter}
```
The length of characters of the expanded value of `parameter` is substituted.

There are [many more](https://tldp.org/LDP/abs/html/parameter-substitution.html) of them!