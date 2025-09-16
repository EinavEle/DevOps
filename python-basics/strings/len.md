Let's start with some basics.



Many times when we have a string we want to know its length.

For example, we might want to validate the minimum length of a password.
```
password = "notgood"
```
To check the length of the string we use the python built-in function len (short for length)
```
if len(password) < 8:
  print("Your password is too short, the minimum length should be 8 characters")
```

On a side note, `len` is not unique for strings, we can use it for lists, tuples, dictionary and more.