Python generators are a simple way of creating iterators.


There is a lot of overhead in building an iterator in Python. We have to implement a class with `__iter__()` and `__next__()` method, keep track of internal states, raise StopIteration when there was no values to be returned etc.


So instead of this class with all its fuss:

```python
class PrintNumbers:
  def __init__(self, size):
    self.max = size

  def __iter__(self):
    self.numbers = list(range(self.max + 1))
    self.counter = 0
    return self

  def __next__(self):
    if self.counter >= self.max:
      raise StopIteration

    self.counter += 1
    return self.numbers[self.counter] 
```

We can get the same result with a generator:

```python
def plus1(stop):
  for i in range(stop):
    yield i 
```

**Awesome!**

### So what is this generator?

A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).


So we can loop through it with a regular for loop:
```python
for x in plus1(4):
  print(x) 
```


### How do we create a generator in Python?

It is fairly simple, it is as easy as defining a normal function with yield statement instead of a return statement.


If a function contains at least one yield statement (it may contain many yield statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.


**For example**, let's look at a generator function named `my_gen` that contains several yield statements:
```python
def my_gen():
  n = 1
  print('This is printed in the first call')
  yield n
  n += 1
  print('This is printed second')
  yield n
  n += 1
  print('This is printed at last')
  yield n 
```
Because generator functions implement the iterator protocol we can use them just like we would use an iterator.


First get the iterator object:
```python
iter_gen = my_gen() 
```

Just like an iterator it returns an object but does not start execution immediately.


Now we can use the next function to get the values one by one:
```python
next(iter_gen)
next(iter_gen)
next(iter_gen)
next(iter_gen)      
```
Once the function yields, the function is paused and the control is transferred to the caller.

When there are no more elements, the `StopIteration` error is thrown.


Normally, generator functions are implemented with a loop having a suitable terminating condition.

Let's take an example of a generator that reverses a string:
```python
def reverse(iterable):
  length = len(iterable)
  for i in range(length - 1, -1, -1):
    yield iterable[i]    # For loop to print the reversed string


for item in reverse("hello"):
  print(item) 
```
This generator function also works with other kind of iterables like list, tuple etc.

Try running it with a list:
```console
["Eric", 1985, ["Dan", "James", "Anna"]] 
```
