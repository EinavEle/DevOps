256 different characters worked well until everyone realized that there were thousands of other characters in other languages that should also be supported. Unicode was then invented which reserves up to 4 bytes for each character allowing for more than a million valid code points.

A code point is simply the number in the table. We will see soon that there are a few ways to represent that number=code point.

Here is part of the unicode table:

![](./unicode_table.png)

It basically defines a ginormous table of 1,114,112 code points that can be used for all sorts of letters and symbols. That's plenty to encode all European, Middle-Eastern, Far-Eastern, Southern, Northern, Western, pre-historian and future characters mankind knows about.

### Different Encodings

These are a lot of characters. To optimize this, there are several ways to encode Unicode code points into bits. UTF-32 is such an encoding that encodes all Unicode code points using 32 bits. That is, four bytes per character. It's very simple, but often wastes a lot of space. UTF-8 is a variable-length encodings. If a character can be represented using a single byte (because its code point is a very small number), UTF-8 will encode it with a single byte. If it requires two bytes, it will use two bytes and so on. It has elaborate ways to use the highest bits in a byte to signal how many bytes a character consists of. This can save space, but may also waste space if these signal bits need to be used often.

You can read more about it [here](https://docs.python.org/3/howto/unicode.html#encodings).


Since `Python 3.0`, the language’s str type contains Unicode characters, meaning any string created using `""`, `''`, or `""" """` is stored as Unicode.

In order to get the unicode value we can use the ord function:
```
ord('C') # 67 
```
You can look at the unicode table and see that the code point (decimal numeric value) is 67.


To go the other way around, meaning, get the character from a decimal value we can use the chr function:

```
print(chr(67)) # C 
```

So now, after we know how to go back and forth from characters to their code point and back, we can complete the task and encode the string:

```
res = ""

for c in "abc":
  code = ord(c)
  incremented_code = code + 1
  incremented_char = chr(incremented_code)
  res += incremented_char

print(res)
```

or:
```
print("".join([chr(ord(c)+1) for c in "abc"]))
```