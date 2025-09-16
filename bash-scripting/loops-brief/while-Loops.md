`while` loops in Bash are used to repeat a block of commands as long as a certain condition is true (ends with exit code 0). Here is the basic syntax of a `while` loop:
```bash
while condition
do
    # commands
done
````
`condition` is a command or expression that returns either 0 (true) or non-zero (false). Here is an example that prints out the numbers from 1 to 5 using a `while` loop:
```bash
i=1
while [ $i -le 5 ]
do
    echo $i
    let i=$i+1
done
```
In this example, `i` is initialized to 1, and the loop continues as long as `i` is less than or equal to 5. `i` is incremented by 1 using the expression `let i=$i+1`.