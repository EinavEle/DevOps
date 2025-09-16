##  Exercise 1

Determine whether the following expressions will output True or False



- (5 > 2) and False
- not ("knife" == "sword")
- (1 < 2) or (-1 > -1) or not False
- not (not True)
- "5th Avenue" != "5th Avenue"
- 52 != "52"


Make sure you figure this out on your own before testing out the code yourself .

## Exercise 2

What will be the values of a, b, and c at the end of this code?


```
a = 3
c = 0
b = a
c = a + b
b = 2
a = b
b = c
c = a
a = b + (c + a)
```

<details>
<summary>Solution</summary>
<div> 
a = 10
b = 6
c = 2
</div>
</details>


## Exercise 3
Write out code for the following:

- Declare two variables: `password` and `confirm_password`
  - Give both a value
- Declare a third variable called `is_correct`
  - Its value should be `True` or `False`, depending on whether `password` and `confirm_password` are the same
- Use concatenation to output "The password is correct: True" or "The password is correct: False" using the value of `is_correct`

<details>
<summary>Solution</summary>
<div> 

```python
password ="123"
confirm_password = "123"
is_correct = True
print("The password is correct" + is_correct)
```
</div>
</details>

