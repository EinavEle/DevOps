Use `filter` and a lambda function to filter this list. You should only keep the vegetarian meals:


```python
menu = [
    {"name": "Beef stew", "vegetarian": False},
    {"name": "Beef sandwhich", "vegetarian": False},
    {"name": "Carrot on a stick", "vegetarian": True},
    {"name": "Beef eggroll", "vegetarian": False},
]
```

You should only have to use one line of code.

Work this out, then check the  solution.

<details>
<summary>Solution</summary>
<div> 

```python
menu = [
    {"name": "Beef stew", "vegetarian": False},
    {"name": "Beef sandwhich", "vegetarian": False},
    {"name": "Carrot on a stick", "vegetarian": True},
    {"name": "Beef eggroll", "vegetarian": False},
]

#                 --------function--------  -list-
print(list(filter(lambda m: m["vegetarian"], menu)))
```
</div>
</details>
