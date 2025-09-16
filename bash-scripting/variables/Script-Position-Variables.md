Positional arguments are arguments passed to a command or script in a specific order, usually separated by spaces. Positional arguments can be accessed, within a bash script file, using special variables such as `$1`, `$2`, `$3`, and so on, where `$1` refers to the first argument, `$2` refers to the second argument, and so on.

Let's see them in action... create a file called `BarackObama.sh` as follows:
```bash
#!/bin/bash

# This script reads 3 positional parameters and prints them out.

echo "$0 invoked with the following arguments: $@"

POSPAR1="$1"
POSPAR2="$2"
POSPAR3="$3"

echo "$1 is the first positional parameter, \$1."
echo "$2 is the second positional parameter, \$2."
echo "$3 is the third positional parameter, \$3."
echo
echo "The total number of positional parameters is $#."

if [ -n "${10}" ]               # Parameters > $9 must be enclosed in {brackets}.
then
  echo "Parameter #10 is ${10}"
fi
```
Execute the script by:
```bash
bash positional.sh Yes We Can 
bash positional.sh Yes We Can bla bla 1 2 3
```
Investigate the script output and make sure you understand each variable. 