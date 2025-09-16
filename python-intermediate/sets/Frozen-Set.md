Just like tuples versus lists, frozensets are immutable sets. It means that they cannot be changed, but they support most of the regular set methods.



frozensets are created by calling `frozenset()` function, which expects to get a single (iterable) argument:


```python
fs = frozenset((1, 2, 3, 4))
print(fs)
print(type(fs))

fs = frozenset([1, 2, 3, 4])
print(fs)
```



As they are immutable, they do not have `add()`, `update()` and `remove()` methods:



As sets are mutable, they cannot be used as keys for dictionaries (or others sets);

frozensets, however, can be used as keys:


```python
set_ = {1,2}
frozenset_ = frozenset((1, 3, 4))


dictionary = {}
dictionary[frozenset_] = 1 # valid
dictionary[set_] = 1 # throws Error
```