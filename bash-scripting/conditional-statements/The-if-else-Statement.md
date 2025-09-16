Sometimes you need to specify different courses of action to be taken in a shell script, depending on the success or failure of a command. The if construction allows you to specify such conditions.

The most common syntax of the if command is:
```bash
if TEST-COMMAND
then
  POSITIVE-CONSEQUENT-COMMANDS
else
  NEGATIVE-CONSEQUENT-COMMANDS
fi
```
This is a conditional statement in Bash that consists of a `TEST-COMMAND`, followed by a positive consequent command block (`POSITIVE-CONSEQUENT-COMMANDS`), and an optional negative consequent command block (`NEGATIVE-CONSEQUENT-COMMANDS`). If the `TEST-COMMAND` is successful (returns an exit status of 0), then the positive consequent commands are executed, otherwise, the negative consequent commands (if provided) are executed. The `if` statement is terminated with the `fi` command.

### *Testing files*
**Before you start, review the man page of the test command.**

The first example checks for the existence of a file:
```bash
echo "This script checks the existence of the messages file."
echo "Checking..."
if [ -f /var/log/messages ]
then
  echo "/var/log/messages exists."
fi
echo
echo "...done."
```

### *Spot Check*
What is the relation between the `test` command and `[`
<details>
  <summary>
     Solution
  </summary>

The [ command is actually a synonym for the test command in Linux. They both provide similar functionality, allowing you to perform various tests and evaluations in shell scripts.

</details>

### *Testing Exit Status*
Recall that the $? variable holds the exit status of the previously executed command. The following example utilizes this variable to make a decision according to the success or failure of the previous command:
```bash
curl google.com &> /dev/null

if [ $? -eq 0 ]
then
  echo "Request succeeded"
else
  echo "Request failed, trying again..."
fi
```

### *Numeric Comparisons*
The below example demonstrates numeric comparison between a variable and 20. Don’t worry is it doesn’t work, you’ll fix it soon 🙂
```bashnum=$(wc -l /etc/passwd)
echo $num

if [ "$num" -gt "20" ]; then
  echo "Too many users in the system."
fi
```

### *Spot Check*
Copy the above script to a .sh file, and execute. Debug the script until you understand why the script fails. Use the `awk` command to fix the problem. Tip: using the `-x` flag can help you debug your bash run: `bash -x myscript.sh`
<details>
  <summary>
     Solution
  </summary>

```bash
num=$(wc -l /etc/passwd | awk '{ print $1 }')

echo $num

if [ "$num" -gt "20" ]; then
  echo "Too many users in the system."
fi
```

</details>

### *String Comparisons*
```bash
if [[ "$(whoami)" != 'root' ]]; then
  echo "You have no permission to run $0 as non-root user."
  exit 1;
fi
```

### *if-grep Construct*
```bash
echo "Bash is ok" > file

if grep -q Bash file
then
  echo "File contains at least one occurrence of Bash."
fi
```
Another example:
```bash
word=Linux
letter_sequence=inu

if echo "$word" | grep -q "$letter_sequence"
# The "-q" option to grep suppresses output.
then
  echo "$letter_sequence found in $word"
else
  echo "$letter_sequence not found in $word"
fi
```

### `[...]` vs `[[...]]`
With version 2.02, Bash introduced the `[[ ... ]]` extended test command, which performs comparisons in a manner more familiar to programmers from other languages. The `[[...]]` construct is the more versatile Bash version of `[...]`. Using the `[[...]]` test construct, rather than `[...]` can prevent many logic errors in scripts.