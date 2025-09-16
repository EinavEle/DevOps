# Exercise 1 - grep on file
Create the file ~/bashusers.txt, which contains lines from the /etc/passwd file which contain the text “/bin/bash”.
<details>
  <summary>
    Solution
  </summary>

```bash
grep '/bin/bash' /etc/passwd > ~/bashusers.txt
```

</details>

# Exercise 2 - grep on file
Create the file `~/rules.txt`, which contains every line from the `/etc/rsyslog.conf` file which contains the text “file”, using a case insensitive search. (In other words, file, File, and files would all count as matches).
<details>
  <summary>
    Solution
  </summary>

```bash
grep -i 'file' /etc/rsyslog.conf > ~/rules.txt
```

</details>

# Exercise 3 - grep with regex
Find the number of words in /usr/share/dict/words that contain at least three “a”s. E.g. traumata, takeaways, salaam
<details>
  <summary>
    Solution
  </summary>

```bash
grep -E 'a.*a.*a' /usr/share/dict/words
```

</details>

# Exercise 4 - regex
Create a file containing some lines that you think would match the regular expression: `(^[0-9]{1,5}[a-zA-Z ]+$)|none` and some lines that you think would not match. Use `grep` to see if your intuition is correct.
<details>
  <summary>
    Solution
  </summary>

```bash
echo "123abc" >> words
echo "45A abcd" >> words
echo "none" >> words
grep -E '(^[0-9]{1,5}[a-zA-Z ]+$)|none' words
```

</details>

# Exercise 5 - regex
Using grep command and regular expressions, list all files in your home directory that others can read or write to.
<details>
  <summary>
    Solution
  </summary>

```bash
ls -la ~ | grep -P '^.{7}(r..|.w.)'
```

</details>

# Exercise 6 0 grep with line number and pipe
Use the grep command and pipes only! 

Create the file ~/mayhemnum.txt, which contains only the line number of the word “mayhem” from the file /usr/share/dict/words.
<details>
  <summary>
    Solution
  </summary>

```bash
grep -n "^mayhem$" /usr/share/dict/words | grep -o -P '\d+'
```

</details>