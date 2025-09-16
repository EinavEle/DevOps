Because a tuple represents more than one value, we need a way to access different items in a tuple. We do this using the concept of indexes.

To access values in tuple, use square brackets (index operator) where the index starts from 0. The index must be an integer.


```python
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[0]) # output:﻿'a'
print(my_tuple[3]) # output:'﻿d'
print(my_tuple[4]) # IndexError: tuple index out of range
```

Nested tuples can be accessed using nested indexing:


```python
nested_tuple = ("shoobert", [10, 20, 30], (0, 2.0, 3.5))

# nested index
print(nested_tuple[0][5]) # output:﻿ 'e'
print(nested_tuple[1][1]) # output: 20
```



We can also use negative indexing, the index -1 refers to the last item, -2 refers to the second last item and so on..


```python
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[-1]) # output:'d'
```