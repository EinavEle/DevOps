Technically speaking, Python **iterator objects** must implement two special methods, `__iter__()` and `__next__()`, collectively called the **iterator protocol**.

An object is called **iterable** if we can get an iterator from it.

Most of built-in containers in Python like: `list, tuple, string, dict, etc ...` are iterables.


## __iter__()


An iterator is an object representing a **stream of data**. You can create an iterator object by applying the `iter()` built-in function to an **iterable**.

```python
numbers = [10, 12, 15, 18, 20]
fruits = ("apple", "pineapple", "blueberry")
message = "I love Python"
print(iter(numbers))
print(iter(fruits))
print(iter(message)) 
```


## __next__()


You can use an iterator to manually **loop over the iterable** it came from.

If we repeatedly pass the iterator to the built-in function `next()` we will get the next item from the iterator. We've already seen how it works, but here is a quick reminder:

```python
numbers = [10, 12, 15, 18, 20]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) 
```

In fact, `next` retrieves the next item from the *iterator* by calling its `__next__()` method.

In the same manner, the built-in function `iter` will call the `__iter__()` function.
