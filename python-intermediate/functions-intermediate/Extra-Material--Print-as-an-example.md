# print()


You already know the print function. **But it has more features that you can use.**

This is how `print()` function is actually defined:

```python
def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
  pass 
```


All non-keyword arguments are converted to strings like `str()` does and written to the stream, separated by **sep** and followed by **end**.


A bit more officially:

**objects**: These are the values we want to print.

**sep**: This is a separator that is used to separate between the values we print. By default it is a space.

**end**: This is the character that is added at the end of the values we print (a newline by default).


So we can pass multiple variables with different types:
```python
print("the ", 3 , " colors are: ", ["blue", "red", "green"]) 
```

We can separate the variables with any string we want, for example "Yo":

```python
print("Here", "we", "go", "again", sep=" Yo ")
# Here Yo we Yo go Yo again 
```

And we can finish the sprint with any string we want, for example `!\n`

```python
print("This is a sentence", end="!\n")
# This is a sentence! 
```

Both **sep** and **end** must be strings.

They can also be None, or not defined at all, which means to use the default values.

If no objects are given, `print()` will just print the **end** string, by default an empty line.



**file**: The stream that our values are printed to.

This argument must be an object with a write(string) method.

By default it is `sys.stdout` object (i.e. the screen).


But we can also print to a file:
```python
with open("result.txt", "a") as res:
  print("hello", file=res)

# OR

my_file = open("result.txt", "a")
print("hello again", file=my_file)
my_file.close() 
```


**flush**: Usually the stream file determines if the objects we print will be buffered or not. Since Python 3, we can force print to flush the content regardless **end** and **file**. In Older version, we would call `sys.stdout.flush()` (or file.flush in other cases) in order to achieve that.

```python
print("Print me now!", flush=True) 
```
