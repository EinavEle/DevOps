Dicts in Python are reference types.



This means that when we "copy" a dict into another variable, what we're really doing is creating a reference to the original dict.

Here's an example:


```
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

other_data = data
other_data["d"] = 4

print(data) # outputs a dict with keys a, b, c, and d
print(other_data) # outputs the same dict!
```

Even though we've only added the key-value pair `"d"` and 4 to `other_data`, it gets added to `data` as well!

That's because these two variables are not separate - Python is referencing the same dict from both `data` and `other_data` - hence **reference type**.



There are ways to get around this, but that is outside the scope of this lesson. For now, just be aware of this.