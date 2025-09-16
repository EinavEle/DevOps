For times when we want to have "intermediary" conditions (i.e, not everything is black and white), we have another keyword: `elif`

Think of a self-driving car that's making a decision about what to do when it sees a traffic light's color:


```
color = "orange"

if color == "green":
	print("Go")
elif color == "orange":
	print("Release breaks")
else:
	print("Stop now.")
```

Note a few things about the above, and conditionals in general:

- Again, **only one block will ever execute** - that's just how conditional statements work
- We didn't have to check for "red" specifically because it's the default
  - More generally, **the `else` block will always execute if none of the previous conditions are met**
- Like `else`, `elif` must come after an `if`
- The final `else` is still not required
- If you do have an `else`, it **must be the last block**