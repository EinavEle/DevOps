Sets are very similar to dictionaries, only that they are consisted of single keys, rather than pairs of key and value.



For example:
```
evens = {2,44,24,62,78}
```

Like dictionaries, sets are not ordered, they are mutable, and their (unique) elements must me immutable (so they can be hashable).



An empty set is created by calling `set()`, as empty braces `{ }` are reserved for empty dictionaries:


```python
s = set()

print(type(s))
print(s)
```

Non-empty sets are generated with braces `{ }` and **hashable** values inside them:


```
s = {3, "Yossi", False, (1,), None}
```



The set's item must be immutable.

Since list is a mutable type, if we try to create a set that contains a list we will get an exception:


```python
s = {list()}
```

```console
>> TypeError: unhashable type: 'list'
```

However, we can construct a set from a list:


```python
s = set([4, 3, 2, 1])

s # {1, 2, 3, 4}
```

We can generate a set from a string:
```
s = set("Tomorrow never dies")
```

Remember - a set contains only unique elements, so every character appears only once.