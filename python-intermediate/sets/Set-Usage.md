We can use the set structure and operations to achieve all kind of tasks, simply and efficiently.



For example:

How can we get all unique elements in a List?





That can be done in only one line:


```
lst = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]

set(lst)
```


Now, let's use sets to find all common items between two lists:


```
s1 = [1, 2, 3, 4, 5, 6]
s2 = [4, 5, 6, 7, 8, 9]
​
set(s1) & set(s2)
```