Python gives us a simple way to determine whether an item exists inside of a list:


```
current_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]

print("Bill Gates" in current_billionaires) # outputs: True
print("You" in current_billionaires) # outputs: False (for now..)
```

The `in` keyword is reserved in Python and has a few uses, and checking if an item is inside a list is one of them.


<hr/>


Of course, we can use the `in` keyword in conditional statements as well. 
For example:


```
if "You" not in current_billionaires:
	print("Work harder")
else:
	print("Give back to society")
```

This is one example of Python's elegance and readability - you can read it almost like plain English and understand intuitively what the code does.



If the above code seems confusing, remember that `"You" not in current_billionaires` is the same as writing `True`, because:



- The `in` keyword returns `True`/`False` depending on whether the value exists in the list
  - The string "You" is not in the list (hence: `False`)
- The keyword not flips the `False` to a `True`