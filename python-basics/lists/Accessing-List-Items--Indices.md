Because a list represents more than one value, we need a way to access different items in a list. We do this using the concept of **indices**.



An **index** is the numeric position of an element inside a list, starting at 0.



For example, in this list:


```
modern_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
```

The index of `"Bill Gates"` is `1`, because we start counting at 0.



This is useful to know, because if we want to output the third name in the list, we would write this code:


```
print(modern_billionaires[2])
```

If that doesn't make sense, you can think of the list like this:


```
["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
#     0             1                2                 3 
```

So even though "Mark Zuckerberg" is the third item in the list, his index is 2.


<hr/>


There is a common "trick" in programming to access the last item in a list.

Because the `len` command returns the count of items in the list, then `len(...) - 1` will always return the index of the last item in the list, for example:


```
last_index = len(modern_billionaires) - 1
print(modern_billionaires[last_index]) # outputs: "Warren Buffet"
```

Keep this trick in mind, it's a good one.

<hr/>



**Note**: if you try to access a list with an index that is outside of its range, <span style="color:red">this will cause your app to crash</span>. For example:


```
# bad code
words = ["don't", "do", "this"]

print(words[3]) # output: An error
```

The range of `words` in this case is `0` to (not including) `3`, i.e. `0` to `len(words)` - so trying to access index 3 is impossible since it doesn't exist.