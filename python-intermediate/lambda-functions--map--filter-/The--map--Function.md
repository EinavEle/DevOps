Using `map` is nearly identical to using `filter`, except instead of filtering a list we are going to map or **transform** it:



Using the same menu from before:


```python
menu = [
    {"name": "Beef stew", "vegetarian": False},
    {"name": "Beef sandwhich", "vegetarian": False},
    {"name": "Carrot on a stick", "vegetarian": True},
    {"name": "Beef eggroll", "vegetarian": False},
]
```

Here we are creating a list with only the menu item names, without the entire dict:


```python
print(list(map(lambda m: m["name"], menu))) 
# outputs: ['Beef stew', 'Beef Sandwhich', ...]
```

The principles are exactly the same:

- The lambda function receives each item in the `menu` list
- We tell it how we want it to transform each item
  - in this case, simply extract the value from the `name` key


If we reverse engineer the above to use a normal function instead of lambda, it would look like this:


```python
def extract_name(menu_item):
    return menu_item["name"]

print(list(map(extract_name, menu)))
```

But that's less cool.