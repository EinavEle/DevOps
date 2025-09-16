# Exercise - Code SImplification Using Logical Operators
```bash
ls -l /home/user/mydir
if [ $? -eq 0 ]; then
    echo "Directory exists."
else
    echo "Directory does not exist."
fi
```
The above code executes the `ls` command, then uses the `$?` variable along with [if statement](https://tldp.org/LDP/abs/html/fto.html) to test if the directory exists and prints corresponding messages.  
Use `&&` and `||` operators to simplify the script. The simplified code should achieve the same functionality in **one command**!
<details>
  <summary>
     Solution
  </summary>

```bash
ls -l /home/user/mydir && echo "Directory exists." || echo "Directory does not exist."
```

</details>