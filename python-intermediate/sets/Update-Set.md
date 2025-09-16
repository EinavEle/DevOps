
## Adding or changing a set element



On one hand, sets are mutable. On the other hand, there is no meaning to indexing, as set are not ordered.

From that reason, we cannot simply change an element in a set, but only remove an element and add a new one.


```
s = { 3, 6, 'bibi', ('Simon', 'Garfunkel') }
s.add(5)
print(s)
```

Addition of an element, can be done by using add(), 


We can add multiple elements with `update()`:


```
s.update([11, 22], (55,), ('mimi',))
print(s)
```

`update()` unpacks the given arguments and adds them to the set.

Note that if 'mimi' would have been given outside a dedicated tuple, 'm' and 'i' letters would be added.



### Deleting an element from set



`del` is not supported in sets:


```
s = { 'Avi', 'Itzik', 'Kobi' }

del s['Avi'] # Error
```



The proper way would be using `discard()` or `remove()` methods:


```
s.discard('Avi')
s.remove('Itzik')
```

The difference between them is that when trying to delete an element which does not exist, `remove()` throws an exception, and `discard()` returns `None`:


```python
s.remove('Itzik') # KeyError: 'Itzik'
print(s.discard('Itzik')) # None
```

It is also possible to remove items from a set by calling `pop()`.

The removal will be done arbitrarily (as there is no order):


```
s = {5, 6, 7, 8, 9}
s.pop()
```

With `clear()`, we can remove all items:


```
print(s)
s.clear()
print(s)
```

### Membership



We can ask if a certain key exists in a set by using in:
```
'T' in s
```
