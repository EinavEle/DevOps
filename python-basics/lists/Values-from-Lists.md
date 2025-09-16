Just like we can create a variable from combining other variables/values, we can also create new variables from a list. For example:


```
modern_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
richest_human = modern_billionaires[0]

print(modern_billionaires)
print(richest_human)
```

If you run the code above you'll note that the `modern_billionaires` list does not change, but we have created a new variable - richest_man whose value is now the same as the first item in the list.



Now `richest_man` is a normal string variable as if we had written


```
richest_man = "Jeff Bezos"
```

It would be exactly the same.