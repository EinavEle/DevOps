A tuple is a collection of Python objects which are separated by commas, **ordered** and **immutable** (unchangeable, once created can not be changed). Tuples are written with round brackets and it looks like this:


```python
fruits_tuple = ("apple", "orange", "banana")
print(fruits_tuple) 
# output: ('apple', 'orange', 'banana')
```

A tuple can contain mixed data types:
```python
mixed_tuple = (0, "apple", 3.4)
print(mixed_tuple) 
# output: (0, 'apple', 3.4) 
```



To write a tuple containing a single value you have to include a comma, even though there is only one value, otherwise it will be considered as a single element

```python
# tuple with one value
num_tuple = (10,)
print(num_tuple) #(10,)

# This is aslo tuple with one value
num_tuple = 10, 
print(num_tuple) #(10,)

# This is a string, NOT a tuple.
not_tuple = ('apple')
print(not_tuple) #apple

# This is an int, NOT a tuple.
not_tuple2 = (10)
print(not_tuple2) # 10

```

### Empty Tuples

We can also create what's known as **empty tuples**, two parentheses containing nothing which looks like this:


```python
empty_tuple = ()
print (empty_tuple) # ()
```