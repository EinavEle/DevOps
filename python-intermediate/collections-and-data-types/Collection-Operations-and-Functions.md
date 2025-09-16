There are all kinds of collections: **mutable**, **immutable**, **ordered**, **unordered**, but some operations are relevant for all the collections.



### len

```python
len({"a": 1, "b": 2})
len([1,2,3]) 
```

Gives you the length of the collection



### membership

```python
4 in [2,4,6,8]    # mutable sequence
4 in {2,4,6}      # unordered mutable collection 
```

Check if an item exist in the collection.


Note that for dictionaries we check if a key exists:
```python
"a" in {"a": 1, "b": 2} # unordered collection 
```

If we try to look for a value we will get a wrong answer:
```python
2 in {"a": 1, "b": 2}   # False 
```
