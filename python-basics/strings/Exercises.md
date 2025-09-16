## 4 Char String

Write a Python program that will create a new string from the first 2 and the last 2 chars of a given a string. If the string length is less than 4, return instead of the empty string.

Example:



"tomato" => "toto"
"fox" => ""
"protocol" => "prol"

<details>
<summary>Solution</summary>
<div> 

```python
word = "tomato"
result = word[:2] + word[-2:] if len(word) >= 4 else ""
print(result)
```
</div>
</details>


## Swap First Letter

Write a program that will receive 2 strings and returns 1 string by swapping their first characters and combining them into 1 string, separated with a space.

For example:

"good", "morning" => "mood gorning"
"Hey", "You" => "Yey Hou"
<details>
<summary>Solution</summary>
<div> 

```python
str1 = "good"
str2 = "morning"

if len(str1) < 2 or len(str2) < 2:
    res = ""
else:
    res = str2[0] + str1[1:] + " " + str1[0] + str2[1:]
print(result)
```
</div>
</details>

##  Replace 2

Replace the first 2 occurrences of "oo" with "u" in a given string.

For example:

"boo boo boo too ta da" => "bu bu boo too ta da"

<details>
<summary>Solution</summary>
<div> 

```python
word = "foo foo doom doom da"
res = word.replace("oo", "u", 2)
print(res)
```
</div>
</details>
