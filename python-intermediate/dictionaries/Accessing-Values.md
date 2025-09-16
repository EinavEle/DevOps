When we use dicts, we are only interested in their values - the keys are just a way to logically structure our data.



Using the same object from before:


```python
user = {
	"name": "Karolin",
	"username": "ksmart3",
	"age": 27,
	"has_purchased": False
}
```

We can access these values using what's known as **bracket notation**:


```
print(user["name"] + " is " + str(user["age"]) + " years old.")
# outputs: Karolin is 27 years old.
```

So all we need to do to extract a value from a dict is to use the variable name - `user` - and access the correct key in that dict - `name`, `age`, etc.

<hr/>

As always, values are simple pieces of data. Therefore, we can access dict values and store them in new variables as well:


```
generated_password = user["name"] + "_" + user["username"]
print(generated_password) # outputs Karolin_ksmart3
```

This new variable - `generated_password` - is now completely independent of the dict, and is a simple string variable.

Likewise, the original `user` dict remains unchanged, and still holds all its keys and values.

<hr/>

Another way of accessing values in a dict is with the `get` method.
```
student = {
    "name": "koko",
    "age": 42
}


print(student.get("name"))
```
One difference, that can be an advantage, is that if we are looking for a key that doesn't exist we will get `None`, not like when we use the brackets notation, in which case we will get an error thrown:
```
print(student.get("address")) # None
print(student["address"]) # throws KeyError: 'address'
```

Last thing that is cool about the get method, is that it receives an additional optional argument for a default value, that is if we tried to get the score value of a student, but the student doesn't have a score key we can get a 0 instead.



So instead of doing this (or something similar):
```
score = None
try:
    score = student["score"]
except KeyError:
    score = 0
```

We can do this:
```
score = student.get("score", 0)
# score = 0
```