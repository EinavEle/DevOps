How will we implement find index?

Assuming we have a list of numbers:
```python
numbers = [11,3,64,17,94] 
```

We know how to iterate the list and find a specific item:
```python
def find_index(items, item):
  for number in items:
    if number == item:
      return number 
```

But how will we know the index of the item?


In Python we have a special function enumerate, that allows us to iterate over the elements of a list and keeping a counter:
```python
def find_index(items, item):
  for index, value in enumerate(items):
    if value == item:
      return index
    return -1 
```

In each iteration the enumerate will return a tuple of index and value.


By default the counter will start from 0, which is a very common case when we work with indices, but we can set it to any number we want:

```python
numbers = [11,3,64,17,94]
for i,v in enumerate(numbers, 100):
  print(i, v) 
```
Run this code and check the prints!
