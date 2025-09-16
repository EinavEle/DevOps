Create an empty array called `stuff`



Add the following items to the list:

- Cheese
- Curtain
- Castle


Create another variable called `new_thing`, give it whatever string value you like.



Now write some code that either

- Adds `new_thing` to the list if it is not already in there, or
- print "That's already in there"


Try this out on your own before checking out the solution here.

<details>
<summary>Solution</summary>
<div> 

```python
stuff = []

stuff.append("Cheese")
stuff.append("Curtain")
stuff.append("Castle")

new_thing = "Curtain"

if new_thing not in stuff:
    stuff.append(new_thing)
else:
    print("That's already in there")
```
</div>
</details>
