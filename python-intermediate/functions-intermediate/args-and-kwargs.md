We saw that we can have default parameters for a function:
```python
def add_numbers(a, c, b=5):
  return a + b + c

print(add_numbers(1, 2, 3))
print(add_numbers(1, 2)) 
```

In the first time we pass 3 arguments, so b = 3, and the result will be 6.

In the second call we pass only 2 arguments, so b will get the default value of 5, and the result will be 8.

---

Let's take a look at the following function:
```python
def add_to_list(value, nums=[]):
  nums.append(value)
  return nums

print(add_to_list(1))
print(add_to_list(2)) 
```

You were probably expecting to see:
```console
[1] 
[2] 
```

But instead we get:
```console
[1] 
[1, 2] 
```

You need to beware when using mutable default parameters.


What happened?


**Default parameter values are evaluated when the function definition is executed, not each time the function is called**.

This means that if you use a mutable default argument and mutate it, you have mutated that object for all future calls to the function.


How can we solve it?
```python
def add_to_list(value, nums=None):
  nums = nums or []
  nums.append(value)
  return nums 
```


## args - Flexible Arguments


We can define a function with unlimited number of arguments:

```python
def more_is_better(*args):
  print(args)


more_is_better(1, 2, 3, 4) 
```

The numbers we passed 1,2,3,4 will be converted to a tuple (1,2,3,4)


Try running the function `more_is_better` with different inputs:
- 1,2
- 1, "hello", True
- [1,2,3], 1,2,3


Note that if we pass a list:
```python
more_is_better([1,2,3]) 
```
We will get a tuple of 1 item - the list.


We can also define unlimited keyword arguments for a function as a dictionary:
```python
def print_suitcase(**suitcase):
  for item,ammount in suitcase.items():
    print(item, ammount) 
```

The `**` means the function will receive the arguments packed in a dictionary.

This is why we can do `suitcase.items()` because it is a dictionary.


This function can receive any number of keyword arguments:
```python
print_suitcase(shirts=3)
print_suitcase(shirts=4, shoes=2, watermelon=16) 
```
Python will pack the key, value pairs in a dictionary and pass it to the function, which in turn can use it through the suitcase reference.


In a reverse manner we can do dictionary unpacking:
```python
def print_bag(bananas=0, apples=0):
  print("bananas", bananas)
  print("apples", apples)
  print_bag(2,3)

fruits = {"apples": 4, "bananas": 5}
print_bag(**fruits) 
```
We can unpack the fruits dictionary into the keyword arguments


Note that in the latest example we had a fixed number of parameters. If we want an unlimited number of keyword arguments we can use packing and unpacking like this:
```python
def print_suitcase(**suitcase):
  for item, ammount in suitcase.items():
    print(item, ammount)

items = {
  "shirts": 2,
  "shoes": 8,
  "watermelon": 100
}

print_suitcase(**items) 
```

Of course we can use any combination of the `args` and `kwargs`, but we must make sure to keep the order
```python
(regular_arguments, *args, **kwargs)
```

For example:
```python
def all_arguments(num, *args, **kwargs):
  print("regular argument", num)
  print("args", args)
  print("kwargs", kwargs)

all_arguments(3, "arg1", "arg2", arg3=3, arg4=[1,2]) 
```

Awesome! Let's move on.
