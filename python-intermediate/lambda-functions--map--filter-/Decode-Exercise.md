**Note**

Anything you can do with a map or a filter you can do with list comprehension. It is recommended to try both ways.

<hr/>



## Decode



The following dict is a "code" for a cipher:


```python
code = {
    "0": "A",
    "1": "E",
    "2": "O",
    "3": "U",
    "4": "G",
    "5": "R",
    "6": "T",
    "7": "U",
    "8": "Y"
}
```

Use this code to decipher the following message:





encrypted_message = "82705145106"

<details>
<summary>Solution</summary>
<div> 

```python
encrypted_message = "82705145106"

code = {
    "0": "A",
    "1": "E",
    "2": "O",
    "3": "U",
    "4": "G",
    "5": "R",
    "6": "T",
    "7": "U",
    "8": "Y"
}

message = "".join(map(lambda c: code[c], encrypted_message))

print(message)
```
</div>
</details>
