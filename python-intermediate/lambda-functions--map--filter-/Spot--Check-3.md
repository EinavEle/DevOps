Given this list:


```python
things = ["tree", "leaves", "green", "letter",
          "envelope", "cost", "money", "check"]
```

Use `map` and a lambda function to create a list of the lengths of each string.

If you do it right, this should be your output:


```
[4, 6, 5, 6, 8, 4, 5, 5]
```

See this code for a working solution after you try.

<details>
<summary>Solution</summary>
<div> 

```python

things = ["tree", "leaves", "green", "letter",
          "envelope", "cost", "money", "check"]

print(list(map(lambda t: len(t), things)))
```
</div>
</details>
