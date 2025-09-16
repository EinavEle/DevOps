We saw one way to create a tuple using `()` :
```python
tup = (1, 2, 3, 4)
```

But we can also create a tuple without parentheses, like this:
```python
tup_no_parentheses = 1, 2, 3, 4
```

And 1 last way is using the python `tuple` function.

We can use it to create an empty tuple:
```python
empty_tuple = tuple()
```

or create a tuple based on an existing iterable (an object that can be “iterated over”, like in a loop, but we will get to it later),

like a list:
```python
empty_tuple = tuple([1,5,3])
```