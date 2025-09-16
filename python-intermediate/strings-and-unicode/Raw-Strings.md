We know we can use escaped character in a string. For instance:

```
print("This is a new\n dawn") 
```
And we will get:
```bash
This is a new
 dawn
```

If on the other hand we want the string to be printed as is we can use an r (or R) prefix:

```
print(r"This is a new\n dawn") 
```

In this case `This is a new\n dawn` will be printed without dropping a line.
