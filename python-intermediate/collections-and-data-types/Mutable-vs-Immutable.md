We already know that everything in python is an object, but it is important to distinguish between 2 different kinds of objects:

## mutable and immutable


**A mutable object can change its content.**

A simple example:
```python
x = [1,2,3]
copy = x 
x += [4]              # changing the list
print(x)              # [1,2,3,4]
print(copy)           # [1,2,3,4] 
```

Here we create a list and then concat another list to it.

The list stays the same, so when we change the list stored in x we also change the list in `copy`.


On the other hand, an immutable object sets its content once, only at creation time, and can never be changed.

Let's take a look at the same example with a tuple which is immutable:
```python
y = (1,2,3)
copy = y 
y += (4,)    # changing the tuple
print(y)     # (1,2,3,4)
print(copy)  # (1,2,3) 
```

what happened here?

when we concat the (4,) tuple we in fact did not change the tuple, but created a new tuple and assigned it to y.


So, in fact, every operation we will do on immutable type, that changes the content, will create a new object.


We can see it also with the `id` function.

```python
a = "always the same"
b = "always the same"
print(id(a))
print(id(b)) 
```

For immutable types, all objects with the same value, will have the same id.

This is not the case for mutable types:
```python
a = [1,2]
b = [1,2]
print(id(a))
print(id(b)) 
```

Here the ids are not the same.
