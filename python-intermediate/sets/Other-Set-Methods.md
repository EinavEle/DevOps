### isdisjoint()


This method returns True when two sets are compared and there is no common value between them (i.e. the sets do not intersect):


```
s1 = {1, 2, 3, 4}
s2 = {1, 5, 6, 7}
s3 = {5, 6, 7, 8}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))
```



### issuperset()


This method returns True if the set in use (perfectly) contains another set:


```
s1 = {'a', 'b', 'c', 'd'}
s2 = {'a', 'b', 'c'}
s3 = {'a', 'b', 'e'}
s4 = {'a', 'b', 'c', 'd'}
s5 = set()

print(s1.issuperset(s2))
print(s1.issuperset(s3))
print(s1.issuperset(s4))
print(s1.issuperset(s5))
```


### issubset()


This method does the opposite of the previous one: It returns `True` if the set in use is contained by another set:


```
s2.issubset(s1)
```



Using the same sets with issuperset() will, of course, return False:


```
s2.issuperset(s1)
```