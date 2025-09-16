Use command substitution `$()` and write a `for` loop that iterates over the files in your home directory.
<details>
  <summary>
     Solution
  </summary>

```bash
for i in $(ls ~)
do
    echo $i
done
```

</details>