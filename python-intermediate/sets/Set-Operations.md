Sets are often used for mathematical and statistical purposes. We can use sets for operations like union, intersection, difference and symmetric difference.

It can be done by either using methods, or bitwise operations.



## Union


Union stands for the entire data covered by both collections:


```python
s1 = {1, 3, 5}
s2 = {2, 4}


s1.union(s2) # {1,3,5,2,4}
 
s1 | s2 # bitwise operation => {1,3,5,2,4}
```



## Intersection


Intersection stands for the common elements shared between both collections:
```
s1 = {1, 2, 5}
s2 = {2, 4, 1}

s1.intersection(s2) #{1,2}

s1 & s2
```

## Difference


Set difference shows only the items that present uniquely in the specific set being tested:
```python
s1 = {1, 2, 5}
s2 = {2, 4, 1}
s1 - s2 # {5}
```

Or:
```
s1.difference(s2) # {5}
```

The result will be different if we use the other set:

```
s2.difference(s1) # {4}
```



Note that the difference parameter can be also a list:
```
s1.difference([6,7,5])
```



## Symmetric difference


Symmetric difference stands for all the items that are unique for each collection, leaving out the common ones:
```
s1 = {1, 2, 5}
s2 = {2, 4, 1}
print(s1 ^ s2) # {4,5}
```

Or:


```
s1.symmetric_difference(s2)
```

Another way to look at this, is by subtracting the common items ( `&` ) from the all items ( `|` ):


```
(s1 | s2 - (s1 & s2))
```