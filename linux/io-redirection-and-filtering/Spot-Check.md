1. Create a file called `fruits.txt` with the contents "apple banana cherry".
1. Use `>` to write the contents of `fruits.txt` to a new file called `output.txt`.
1. Use `>>` to append the contents of `fruits.txt` again to `output.txt`.
1. Use `|` to pipe the output of `cat output.txt` to `grep banana`. How many times does `banana` appear? 
1. Use `grep -i` to search for `APPLE` (upper cases) in `output.txt`. Did the search succeed?
1.  Use `grep -v` to display all lines in `output.txt` that don't contain banana.
<details>
  <summary>
    Solution
  </summary>

1. `echo "apple banana cherry" > fruits.txt`
1. `cat fruits.txt > output.txt`
1. `cat fruits.txt >> output.txt`
1. `cat output.txt | grep banana`
1. `grep -i "APPLE" output.txt`
1. `grep -v "banana" output.txt`

</details>