List comprehension is an elegant and widely used syntax to create a list from a loop with just one line:



Let's say we want to add 1 to each element in the list.

Instead of doing:


```
original = [2, 4, 6, 8, 10, 12, 14]
plus1 = []

for element in original:
    plus1.append(element + 1)

print(plus1)
```

We can simply do:
```
original = [2, 4, 6, 8, 10, 12, 14]

plus1 = [x+1 for x in original]
print(plus1)
```



We can see that the main "for loop" syntax remained as is `for x in original`

The only change is that we specify the new value at the beginning.



What if we want only some of the elements in the new list?

We can add a condition:
```
original = [2, 4, 6, 8, 10, 12, 14]

bigger_than_8 = [x for x in original if x > 8]
print(bigger_than_8)
```

This is a great power! and the pythonic way!

Use it!