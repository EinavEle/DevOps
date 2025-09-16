In python **everything is an object**.

Even the built in types.

```python
i = 9
print(type(i))    # <class 'int'>
f = 5.25    
print(type(f))    # <class 'float'>
b = True    
print(type(b))    # <class 'bool'> 
```

We can see that the types are all classes.


For the next example we will use the id function, which gives us the identity of an object as an integer.

Usually, it corresponds to the object's location in the memory.

Example:
```python
x = "Just a string"
print(id(x))
```

You will get an integer, something like: `4440977456`


Now, let's take a look at this example:
```python
x = 10
y = x
print(id(x))
print(id(y))
print(id(10))  
```

You might be surprised to find out that all the ids are the same:
```python
print(id(x) == id(y))
print(id(y) == id(10)) 
```

This is because everything on python is an object, and this is why everything is passed by reference.

**In fact all the references: x, y, 10, are all referencing the same object.**
