The `filter` function is powerful in-and-of itself, but we can can make it even better by introducing **lambdas**.



A lambda function is a normal function, except:

- We can write it in **one line**
- It has slightly different syntax
- It is anonymous, i.e. it won't have a name


Here's a basic function we're going to convert to a lambda function:


```python
def is_allowed_entry(person):
    return person["age"] > 18 or person["is_vip"]
```

A simple function that receives a `person` dict, and returns a boolean.

Now as a lambda:


```python
lambda person: person["age"] > 18 or person["is_vip"]
```

Yes.



Here are the key differences:

- We use the `lambda` keyword to define lambda functions
- After `lambda`, we indicate the parameters of the function
- There is no `return` statement - the function implicitly returns whatever comes after the ` :  ` - in this case just a boolean


However, as we've written the above function, we cannot invoke it. We've defined a function with no name, and so have no way to access it.



We could do something like this:


```python
f = lambda person: person["age"] > 18 or person["is_vip"]

print(f({"age": 13, "is_vip": True})) # outputs: True
```

But usually that's not how we use lambdas.



In the next section we'll see how we can use `filter` and lambda functions together.