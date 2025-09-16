## Exercise 1

Write a function that receives two strings, and returns the longest string.

Remember that you can use `len` to determine the length of a string.


<details>
<summary>Solution</summary>
<div> 

```python
def longest_string(str1, str2):
    return str1 if len(str1) > len(str2) else str2


print(longest_string("abc", "ab"))
print(longest_string("ab", "abc"))
```
</div>
</details>



## Exercise 2

Modify the function from the previous exercise so that now it can also return "same length" in case both strings are the same length.


<details>
<summary>Solution</summary>
<div> 

```python
def longest_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    return "same length"


print(longest_string("abc", "ab"))
print(longest_string("ab", "abc"))
print(longest_string("abc", "abc"))
```
</div>
</details>



## Exercise 3

Write a function called `is_long_string` that returns `True` if a a given string is longer than 10 characters, `False` otherwise.

Write another function called `judge` that:

- Receives two strings
- Determines which one is the longest
- Uses `is_long_string` to print either "____ is a long string", or "____ is a normal string" for the longest string received


For example,

Running `judge("shepherd", "cataclysmic")` should eventually print `cataclysmic is a long string`
Running `judge("horse", "cat")` should eventually print `horse is a normal string`

<details>
<summary>Solution</summary>
<div> 

```python
def is_long_string(text):
    max_length = 10
    return len(text) > max_length


def judge(str1, str2):
    longest = str1 if len(str1) > len(str2) else str2
    size = "long" if is_long_string(longest) else "normal"
    print(longest, f"is a {size} string")


judge("shepherd", "cataclysmic")
judge("horse", "cat")
```
</div>
</details>
