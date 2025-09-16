Tuples are immutable which means you cannot update or change the values of tuple elements.
```python
my_tuple = ("aaa", "bbb", "ccc", "ddd")
my_tuple[1] = "eee" # TypeError: 'tuple' object does not support item assignment
```

Even though we can not update or change tuples, it is possible to create new tuple from existing tuples:
```python
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)

total = numbers1 + numbers2
print(total) # output: (1, 2, 3, 4, 5, 6)
```