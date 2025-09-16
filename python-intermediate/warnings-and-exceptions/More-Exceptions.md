### ZeroDivisionError
```python
3 / 0
```

In the console:
```console
Traceback (most recent call last):
  File "/Users/shiranusboim/PycharmProjects/untitled/exeption.py", line 1, in <module>
    3 / 0 
ZeroDivisionError: division by zero 
```

### IndexError
```python
lis = [3, 2, 1]
lis[4] 
```

In the console:
```console
Traceback (most recent call last):
File "/Users/shiranusboim/PycharmProjects/untitled/exeption.py", line 2, in <module>
  lis[4] 
IndexError: list index out of range  
```

### SyntaxError
```python
if True 
```
In the console:
```console
File "/Users/shiranusboim/PycharmProjects/untitled/execption.py", line 1
  if True
        ^
SyntaxError: invalid syntax
```


### IndentationError
```python
if True: print("Where is the identation?")
```
In the console:
```console
File "/Users/shiranusboim/PycharmProjects/untitled/warning.py", line 2
  print("Where is the identation?") 
  ^
IndentationError: expected an indented block
```

There are different kinds of exception, this way you can understand what happened. For example when parsing a file, you probably should handle differently if the file has no data, someone else using it or one of the lines has a Unicode char and you didn't expect that.