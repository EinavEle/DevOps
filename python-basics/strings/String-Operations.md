We can use many operators with strings: +, * and more.

Let's see a few examples.



## Concatenation



We can combine 2 strings with a `+` operator:
```
print("Good " + "job")
```

We can duplicate a string with a `*`  operator:
```
print("mush" * 2) # mushmush
```

We can compare 2 strings with `==`:
```
s1 = "Kush"
s2 = "Kush"

print(s1 == s2)
```

or use `>` for lexicographical comparison:
```
print("apple" > "banana")  # False
```



## Split



Python provides the `split` method for splitting strings based on delimiters (values we use to separate items):

The most common split is to divide a sentence into word:
```python
moto = "It’s weird not to be weird"
print(moto.split(" "))
# ['It’s', 'weird', 'not', 'to', 'be', 'weird']
```

But we can split according to different delimiters:
```python
moto = "It’s weird not to be weird"
print(moto.split("not"))
# ['It’s weird ', ' to be weird']
```
Note that strings are case sensitive:
```python
moto = "It’s weird not to be weird"
print(moto.split("Not"))
# ['It’s weird not to be weird']
```



## Join



Another common operation is join. It transform a list of strings into 1 string, with the options to add a delimiter in between the string items:
```python
delimiter = '*'
print(delimiter.join(['S', 'T', 'A', 'R', 'S']))
```

## replace

We can use `replace()` to replace a certain substring/character with another:
```
begin = "Just an innocent"
end = " sentence"

print(begin.replace("innocent", "awesome") + end)﻿
```

replace can get a third (optional) argument, specifying the number of instances we want to replace:
```
sentence = "My name are Amitai, and my grammer skills is terrible"
print(sentence.replace("are", "is", 1))
```

There are many more useful things we can do with strings. Let's see a few more examples.



## startswith

Pretty straight forward.


```python
usual_morning_sleep = "Mother: Wake up, you'll be late to Python lesson!"

# In University
if usual_morning_sleep.startswith("Mother"):
    print("Me: Mom, I don't feel so well today.")
```



## in


```
if "Python" in "I love Python":
    print("Yay!")
```




## endswith


```
"Want more?".endswith("?")
```



## find


```
inp = "That keeps me searching for a heart of gold... And I'm getting old."
print(inp.find("gold")) # 39
print(inp.find("Silver"))  # Returns -1 if absent
```



## index

Returns the index of the first occurrence of a substring inside a string.


```python
i = "Have a cookie, cookie.".index("cookie")
print(i)

j = "Have a cookie, cookie.".index("chuky")
print(j) # throws error 
```

Notice that `index()` and `find()` actually provide the same functionality, only that find() returns -1 if the substring is not found, and `index()` throws an exception.

If index() is used in concatenation with other actions, the failure can be silently skipped without notice.



## upper and lower

Change the string to lower/upper case.
```
print("i have small expectations".upper())
print("PEOPLE TELL ME THAT I'M TOO DRAMATIC".lower())
```



## title

 Makes the first character in every word upper case


```python
print("ten reasons why i love python".title())
# Ten Reasons Why I Love Python
```