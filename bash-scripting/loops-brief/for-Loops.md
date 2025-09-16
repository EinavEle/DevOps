`for` loops in Bash are used to iterate over a set of values. Here is the basic syntax of a `for` loop:
```bash
for var in values
do
    # commands
done
```
`var` is a variable that will be set to each value in `values` in turn. `values` can be a list of words separated by spaces, or a command that generates a list of values. Here is an example that prints out the numbers from 1 to 5:
```bash
for i in 1 2 3 4 5
do
    echo $i
done
```
You can also use the `seq` command to generate a sequence of numbers:
```bash
for i in $(seq 1 5)
do
    echo $i
done
```