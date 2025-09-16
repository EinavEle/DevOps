Given this list:


```
clients = ["Bethany", "Clarissa", "Derek", "Evan", "Felicity"]
```

Write an `in range(...)`` loop that outputs the following:
- `1. Bethany`
- `2. Clarissa`
- . . .
- `5. Felicity`


Remember - you cannot concatenate strings and numbers directly - you have to use `str`!

See here for a solution once you're done.

<details>
<summary>Solution</summary>
<div> 

```python
clients = ["Bethany", "Clarissa", "Derek", "Evan", "Felicity"]

for i in range(0, len(clients)):
    print(str(i + 1) + ". " + clients[i])
```
</div>
</details>
