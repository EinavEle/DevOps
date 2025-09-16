A function can return anything: a string, number, list.

A function can also return a function:
```python
def get_print():
  def my_print(msg):
    print(msg)
  
  return my_print
  

get_print()("hello") 
```

What is going on here?

First, `get_print` is a function that returns a function `my_print`.

So the return value of `get_print` is a function:
```python
def get_print():
  def my_print(msg):
    print(msg)
  
  return my_print

print_func = get_print()
print(type(print_func)) 
```
So, `print_func` is a function.

And like any other function, In order to execute it we need to add `()`
```python
print_func = get_print()
print_func("hello") 
```

Let's see another example:
```python
def generate_add(x):
  def inner(y):
    return x + y

  return inner 
```

Here we have a function that generates functions that add a constant number.

We can use the same `generate_add` function to create a function that adds 1 and a function that adds 2:
```python
add_1 = generate_add(1)
add_2 = generate_add(2)
print(add_1(5)) #6 
print(add_2(5)) #7 
```

