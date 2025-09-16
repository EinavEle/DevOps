Variables are how programming and scripting languages represent data. A variable is nothing more than a **label**, a name assigned to a location or set of locations in computer memory holding an item of data. As seen in previous examples, shell variables are in uppercase characters by convention.

Let us carefully distinguish between the name of a variable and its value. If `variable1` is the name of a variable, then `$variable1` is a reference to its value, the data item it contains.
```bash
variable1=23
echo variable1
echo $variable1
```
No space permitted on either side of = sign when initializing variables. What happens if there is a space?
```bash
VARIABLE =value
VARIABLE= value
VARIABLE = value
```
# Spot Check
Execute each one of the above mistaken examples, explain the reason for each error.
<details>
  <summary>
     Solution
  </summary>

1. `VARIABLE =value`: Bash interprets the `VARIABLE` statement as a command (which does not exist), and the `=value` as an argument which was sent to the VARIABLE command. Hence the “VARIABLE: command not found” output. 
1. `VARIABLE= value`: Bash defines the variable `VARIABLE` to be equal to nothing (empty string), then tries to execute the command `value`, which does not exist. 
1. `VARIABLE = value`: Bash interprets the `VARIABLE` statement as a command (which does not exist), and the `=` and `value` as two arguments which were sent to the `VARIABLE` command. Hence the “VARIABLE: command not found” output. 

</details>