You do not need to understand how these two functions work:


```
def remove_letter_from_text(text, letter):return "".join(filter(lambda c: c != letter, text))


def encode_text(text):
    return "-".join(map(lambda c: str(ord(c)), text))
```

However, here is what they expect, and what they return:

- `remove_letter_from_text`
    - Expects to receive two parameters: a string, and a single letter
    - Returns: the same string, but without the letter sent in the second parameter
     - Example: given `("albatros", "a")`, the function will return `lbtros`
- `encode_text`
  - Expects a string
  - Returns: the string converted to numbers separated by a `-`
    - Each number represents a different letter
    - Example: give `(cat)`, the function will return 99-97-116


**Your task** is to write a function called `show_encoded_filter`, which receives two parameters: a string, and a single letter.

Your function should use the parameters to first invoke `remove_letter_from-text`, then use the return value of that function and pass it into `encode_text`, and save that function's return value into a separate variable.



Your function should also print out the entire process.

For example, invoking `show_encoded_filter("sinusitis", "s")` should output:
```
"Updated text is inuiti"
"Encrypted text is 105-110-117-105-116-105"
```

It seems like a lot of instructions, but ultimately you won't be writing much code - just invoking other functions. Take some time to figure this out, then see this solution as well.

<details>
<summary>Solution</summary>
<div> 

```python
def remove_letter_from_text(text, letter):
    return filter(lambda c: c != letter, text)


def encode_text(text):
    return "-".join(map(lambda c: str(ord(c)), text))


def show_encoded_filter(text, letter):
    updated_text = remove_letter_from_text(text, letter)
    print("Updated text is " + updated_text)

    encrypted_text = encode_text(updated_text)
    print("Encrypted text is " + encrypted_text)


show_encoded_filter("sinusitis", "s")
```
</div>
</details>


## Spot Check 2

Write the `determine_biggest` function such that this will work:


```python
biggest = determine_biggest(91234, 91241)
print("Biggest number is " + str(biggest)) 
# outputs: Biggest number is 91241
```

A few notes:

- Your function should **not** use `print`.
- Test your function with a few different inputs.


Take some time, then check this solution as well.

<details>
<summary>Solution</summary>
<div> 

```python

def determine_biggest(num1, num2):
    if num1 > num2:
        return num1
    
    # Note that we don't need an "else", because `return` ends the function!
    return num2

biggest = determine_biggest(91234, 91241)
print("Biggest number is " + biggest) 
# outputs: Biggest number is 91241
```
</div>
</details>
