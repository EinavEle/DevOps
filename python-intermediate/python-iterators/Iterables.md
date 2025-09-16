We saw we can use the for in syntax with many different objects:
```python
# lists
for num in [1,2,3]:
  print(num)

# tuples
for num in (1,2,3):
  print(num) 

# strings
for char in "wonders":
  print(char)

# dictionaries:
for key in {"name": "momo", "age": 33}:
  print(key) 
```

How does Python know how to iterate each of these objects?

The answer is that they are all iterables, meaning they are capable of returning their members one by one.


For every iterable object we can get an iterator, which is an object that allows you to go through all of its items.

We can get the iterator using the built-in function iter
```python
string_iterator = iter("Python is great")
list_iterator = iter([2,4,6]) 
```

With each iterator we can use the next method to return the next item.

After we got the iterator we can call the next method to go through all the items: 
```python
string_iterator = iter("Python")

print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator)) 
```

We can also pass a default value to the next method:
```python
print(next(string_iterator, None)) 
```

We will get the second argument None if there is no next item.


But how does it know when to stop?

When the iterator has no more elements it will throw a **StopIteration** Error.
```python
list_iterator = iter([])
next(list_iterator) # throws StopIteration exception 
```

We can catch it of course:
```python
try:
  print(next(list_iterator))
except StopIteration as e:
  print("no more items") 
```
