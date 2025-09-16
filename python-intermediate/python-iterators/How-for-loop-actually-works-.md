**How for loop actually works?**


Let's take a closer look at the for loop:
```python
for element in iterable:
  # do something with element 
```

It is actually implemented as:

```python
iter_obj = iter(iterable)
while True:
  try:
    element = next(iter_obj) 
```

First we create an iterator by using the iter function (that uses the `__iter__()` function)
```python
iter_obj = iter(iterable) 
```

Then we start with an infinite loop, getting each time the next item in line:
```python
while True:
  try:
    element = next(iter_obj) 
```
If a StopIteration exception is raised, we will break out from loop.


So internally, the for loop creates an iterator object, by calling `iter()` on the iterable.

Ironically, this for loop is actually an infinite while loop.

Inside the loop, it calls `next()` to get the next element and executes the body of the for loop with this value. After all the items exhaust, StopIteration is raised which is internally caught and the loop ends.

```python
iter_obj = iter(iterable)
while True:
  try:
    element = next(iter_obj)
  except StopIteration:
    break 
```
