A **list**, as the name suggests, is a collection of elements. While we can store a single piece of information in a variable (a string, an integer, a boolean..), we can store many pieces of information in a list.



We use the `[...]` (square brackets) notation to denote a list in Python, and it looks like this:


```
modern_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
```

Aside from the `[` that starts a list, the commas that separate list items, and the `]` that closes a list - everything else is the same.

You can create a list with any type of data, and you can even mix different types of data in a list; though that is uncommon.


<hr/>


If at any point you want to know how many items are in a list, you can use the `len` operation:


```
number_of_billionaires = len(modern_billionaires)
print(number_of_billionaires) # outputs: 4
```

You could, of course, do the same directly in the `print`:


```
print( len(modern_billionaires) ) # outputs: 4
```

We'll see soon when the length of a list can be interesting to us.

<hr/>



We can also create what's known as **empty lists**, which looks like this:


```
friends = []
```

All this is saying is that now we have a variable named `friends`, which is a list, and there is nothing in the list yet.



Not surprisingly, if you execute `len(friends)`, it will output 0. Sad.