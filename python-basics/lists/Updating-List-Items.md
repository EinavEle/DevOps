Just like you can update instead of overwrite a variable, you can also update an array item:


```
modern_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
modern_billionaires[0] += " - Amazon"
modern_billionaires[1] += " - Microsoft"

print(modern_billionaires)
```

Running the above code will output the following array: `["Jeff Bezos - Amazon", "Bill Gates - Microsoft", "Mark Zuckerberg", "Warren Buffett"]`

Now instead of erasing the old value, we're only adding on to it.


<hr/>


This can also be done with numbers, of course:


```
class_grades = [80, 72, 91, 64]
class_grades[3] += 12

print(class_grades) # outputs: [80, 72, 91, 76]
```

Now we can update everyone's grades without losing any information.