In python we can't concatenate a number to string

```python
error = "I am the " + 1 
```

In this case we will get an error:
```console
TypeError: can only concatenate str (not "int") to str
```

To convert from a numeric value (or Boolean) to a string, we can use `str()`:

```python
proper = "I am the " + str(1)
# Same as empty = ""
empty = str() 
```

It is possible to create a string from a collection or a dictionary, like list:

```python
list_ = [3, 4, "Bobby"]
list_str = str(list_)

dict = {3 : "kuku"}
dict_str = str(dict)
print(dict_str) 
```

In the same manner we can convert between different types:
```python
str_to_int = int("304")
print(str_to_int)

float_to_int = int(3.05)
print(float_to_int)

int_to_float = float(9)
print(int_to_float) 
```

You get the point...
