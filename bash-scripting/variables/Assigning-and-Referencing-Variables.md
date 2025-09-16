Below are a few examples of variable referencing. Try them out and make sure you understand each one of the cases. 
```bash
A=375
HELLO=$A

echo HELLO      # HELLO
echo $HELLO     # 375
echo ${HELLO}   # 375
echo "$HELLO"   # 375
echo "${HELLO}" # 375
echo "Oh, I like them squishy" >> ode_to_$A.txt # ode_to_375.txt was created
              
# Variable referencing disabled (escaped) by single quotes
echo '$HELLO'
```
There are [MUCH more](https://tldp.org/LDP/abs/html/parameter-substitution.html#PARAMSUBREF) functionalities.

# *Bash variables are untyped*
Unlike many other programming languages, Bash does not segregate its variables by "type." Essentially, Bash variables are character strings, but, depending on context, Bash permits arithmetic operations and comparisons on variables. The determining factor is whether the value of a variable contains only digits.
```bash
a=879
echo "The value of \"a\" is $a."

a=16+5
echo "The value of \"a\" is now $a."
```
# *Assignment using `let`*
```bash
let a=16+5
echo "The value of \"a\" is now $a."
```
# *Variable assignment using the commands substitution - `$(...)`*
```bash
R=$(cat /etc/profile)
arch=$(uname -m)
echo $R
echo $arch
```
# *Variable reference using curly braces - `${...}`*
Consider the below example:
```bash
myuser@hostname:~$ ls
hello_world.txt
myuser@hostname:~$ echo $A
hola
myuser@hostname:~$ echo "filename language changed!" > $A_world.txt
myuser@hostname:~$ ls
hello_world.txt
myuser@hostname:~$ ls -a
hello_world.txt        .txt
```
Where is the file `hola_world.txt`? A couple of things have been mistakenly done by myuser! First, the bash shell dereferenced the correct variable name, but not the one that myuser intended. The bash shell resolved the (uninitialized) variable A_world (to nothing), and created the resulting file `.txt`. Secondly, because `.txt` starts with a `.`, it is a "hidden file", as the ls -a command reveals.

Let’s utilize the curly braces reference syntax to resolve myuser’s problems: 
```bash
myuser@hostname:~$ echo "filename language changed!" > ${A}_world.txt
myuser@hostname:~$ ls
hello_world.txt       hola_world.txt       .txt
```
When finished with a variable, the variable may be unbound from its value with the `unset` command.
```bash
myuser@hostname:~$ unset A
myuser@hostname:~$ echo $A

myuser@hostname:~$
```