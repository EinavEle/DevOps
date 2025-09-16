Given a string that contains only characters, we want you to return a string with a different arrangement:

1. All lowercase are first, ordered from z to a, then all uppercase letters ordered from Z to A. 

**Example**: "ArYnjTdsV" => "srnjdYVTA"

<details>
<summary>Solution</summary>
<div> 

```python
word = "ArYnjTdsV"
res = "".join(sorted(word, reverse=True))
print(res)
```
</div>
</details>

2. All letters smaller from "m" first arranged alphabetically, then all letters bigger or equal to "m", arranged from biggest to smallest.

**Example**: "aGUiLSCMepk" = > "aCeGikLUSpM"

<details>
<summary>Solution</summary>
<div> 
```python
word = "aGUiLSCMepk"
smaller = sorted([x for x in word if x.lower() < 'm'], key=str.lower)
larger = sorted([x for x in word if x.lower() >= 'm'], reverse=True, key=str.lower)
res = "".join(smaller+larger)
print(res)
```
</div>
</details>
