Create your own dict called `fridge` to manage the food in your refrigerator. These are the key-value pairs you should have:



- milk - value should be 1
- bananas - value should be 4
- juice - value should be 2


Now write some code that outputs either

There is one bottle of milk left - this should only output if the value of `milk` is exactly 1

Or

There are **x** bottles of milk left



Where **x** is the value of the key milk in the dict.

<hr/>

Try this out for a bit, then see this for a solution.

<details>
<summary>Solution</summary>
<div> 

```python
fridge = {
    "milk": 1,
    "bananas": 4,
    "juice": 2
}

if fridge["milk"] == 1:
    print("There is one bottle of milk left")
else:
    print("There are " + str(fridge["milk"]) + " bottles of milk left")
```
</div>
</details>
