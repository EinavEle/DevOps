If our entire text is composed with ASCII characters we can use the python built-in bytes object.

To create a bytes literal is very similar to creating a string, only that you add a b prefix:

```Python
byte_string = b'ABC' 
```

This is a sequence of bytes, which means each character is represented by 8 bits=256 options, which is...

I know you guessed it!

An ASCII character.
The number from 0-255 is translated into ASCII character. This is why we can only put ASCII characters in a bytes object.

To get the ASCII value we can simply iterate the string:

```Python
byte_string = b'ABC'
for x in byte_string:
  print(x) 
```

And get:

```console
65
66
67
```

To build a bytes object from a list of bytes we can simply use:

```Python
print(bytes([65,66,67])) # ABC 
```

Of course we can also get the values in hexadecimal base:

```python
print(b'ABC'.hex()) # 414243 
```

What if we have a string, and we want it in bytes?

For that we can encode the string with the wanted encoding:

```Python
print("ABC".encode('ascii'))
print("ABC".encode('utf-8')) 
```

The result is a byte code.


So, if we want to complete the task we had (to convert each character to the character after it), we can also use the encode method:

```Python
for b in "ABC".encode("ascii"):
  print(b) 
```

and we get:
```console
65
66
67
```

What if we try:

```Python
for b in "ABC😂".encode("ascii"):
  print(b) 
```

Well, the 😂 is not part of the ascii table.

And we will get an error:

```console
UnicodeEncodeError: 'ascii' codec can't encode character '\U0001f602' in position 3: ordinal not in range(128)
```

We need to use a unicode encoding, for example UTF-8:

```Python
print("ABC😂".encode('utf-8')) 
```

What we get is this:

```Python
b'ABC\xf0\x9f\x98\x82' 
```

The first 3 characters are the ASCII characters that can be represented in 1 byte.

The last symbol, that is numbered 128514 (decimal value) is represented across several bytes in hex base.

