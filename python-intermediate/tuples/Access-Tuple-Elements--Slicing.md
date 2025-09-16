Another way to access tuple elements is using the slice operator. The **slice operation** - colon `:` returns a new tuple contains a range of items.


```python
my_tuple = ("aaa", "bbb", "ccc", "ddd")

# Accessing elements 2nd and 4th
print(my_tuple[1:4]) # output: ('bbb', 'ccc', 'ddd')
```

Slicing can have negative indexes as well:


```python
my_tuple = ("aaa", "bbb", "ccc", "ddd")

# Accessing elements 2nd and 4th
print(my_tuple[-3:-1]) # output: ('bbb', 'ccc')
```

Here is how the negative indexes looks like:

```
  -4     -3     -2     -1
("aaa", "bbb", "ccc", "ddd")
```
<hr/>


Another cool thing about slicing is that you can step between the tuples' elements using [start:stop:step], meaning slice of tuple from `start` to `stop` with step `step`:

```python
my_tuple = ("aaa", "bbb", "ccc", "ddd")

# Accessing elements 2nd and 4th
print(my_tuple[2:4:2]) # output: ('ccc',)
```

When `start` and `stop` are absent, the meaning is "every `step` element".



We also have the option not to specify a parameter.

In that case python will use the default values:
start = 0
stop = len(str), the length of the string
step = 1



So if we want to take the first 5 letters we will do:
```python
str[:5]
```
If we want all the letters from the second letter till the end we will do:


```python
str[1:]
```
If we want to copy the string we will do:
```python
str[:]
```