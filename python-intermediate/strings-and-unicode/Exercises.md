## Exercise: to_upper
### Instructions:

Write a `to_upper(c)` function using `ord()` and `chr()` to return the uppercase letter of c, if it is not a lower case return the character as is.


For example:
```
print(to_upper("d"))    # "D"
print(to_upper("Q"))    # "Q" (no change)
print(to_upper("!"))    # "!" (no change) 
```

Write an `upper(s)` function to return a copy of the string s with all of its lowercase letters changed to uppercase and the rest unchanged. Use your `to_upper()` function.


For example:
```
print(upper("I love Python!"))    # "I LOVE PYTHON!" 
```


## Exercise: Unicode Encryption
### Instructions:

Write a function `encode(msg)` to encrypt message.

Each character c will encode by the Unicode value of c. The characters will be separates by spaces.

The function should return the encrypted message.

For example:
```
print(encode("Hello"))    # "72 101 108 108 111" 
```

Write a function `decode(msg)` to decode encrypted message.

The function should return the decoded message.


For example:
```
print(decode("72 101 108 108 111"))   # "Hello"
print(decode(encode("Hello")))        # "Hello" 
```


## Exercise: Word value
### Instructions:

Write a `get_word_value(word)` function to return the value of word based on assigning a=1, b=2, . . . , z=26, and computing the sum of the values of the letters in word.

Assume the word is all lowercase.

For example:
```
print(get_word_value("day"))    # 4 + 1 + 25 = 30 
```


## Exercise: Caesar cipher
### Instructions:

A Caesar cipher is a decoding algorithm.

It receives a shift n that alters each letter in the message by moving forward n steps.


For example, if n = 3, then:

    A → D
    B → E
    ... and so on

wrapping around so that:

    X → A
    Y → B
    Z → C


Write an encode(msg, n) function to encode msg using a Caesar cipher with shift n.

Assume msg consists entirely of uppercase letters, with no spaces or punctuation.


For example:
```
print(encode("ABXYZ", 3))   # "DEABC" 
```


Also write a decode(msg, n) function to decode msg.


For example:
```
print(decode("DEABC", 3))    # "ABXYZ" 
```


## Exercise: Convert string-number to int
### Instructions:

Write function that receive number as string and return the number as int **without using int() conversion**.

You need to handle the case the input string contain any non-digit character.

You can choose the way to handle it.

For example:
```
print(string_number_to_int("10"))       # output: 10
print(string_number_to_int("123"))      # output: 123
print(string_number_to_int("99"))       # output: 99
print(string_number_to_int("ABC")) 
```

## Exercise: Convert string number to decimal - Extension
### Instructions:

Improve the function from the previous exercise and receive number as string and base.

The function should return the number as int **without using int() conversion**.

The base can be: 2 (BIN), 8 (OCT), or 10 (DEC)

You need to handle the case the input string contain any digit that not exist int the base.

You can choose the way to handle it.

For example:
```
# base 2
print(string_number_to_decimal("10", 2))      # output: 2
print(string_number_to_decimal("101", 2))     # output: 5
print(string_number_to_decimal("12", 2))      # base 8
print(string_number_to_decimal("7", 8))       # output: 7
print(string_number_to_decimal("123", 8))     # output: 83
print(string_number_to_decimal("10", 8))      # output: 8
print(string_number_to_decimal("9", 8))       # base 10
print(string_number_to_decimal("10", 10))     # output: 10
print(string_number_to_decimal("123", 10))    # output: 123
print(string_number_to_decimal("99", 10))     # output: 99
print(string_number_to_decimal("ABC", 10))
```

Why your code doesn't work on base 16?
