## Spot Check #1
### Instructions

What is the value of the following? Please don't run the code before answering

```
 chr(ord("M")) 
```
<details>
<Summary>Answer</Summary>
"M"
</details>

---

```
 ord(chr(22)) 
```

<details>
<Summary>Answer</Summary>
22
</details>

---

```
chr(ord("4") + 3) 
```

<details>
<Summary>Answer</Summary>
7
</details>

---


## Unicode Table
### Instructions

1. Write a program to display a Unicode table for the characters with codes between 200 and 1000.
2. Improve your code by handling any valid range.

Give this a few minutes, and see the solution when you're done.


<details>
  <summary>
     Solution
  </summary>

```Python
    def print_unicode_table(start, end):
      for i in range(start, end + 1):
        print(f"{i}: {chr(i)}")

    print_unicode_table(200, 1000) 
```
</details>


