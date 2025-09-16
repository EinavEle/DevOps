Remember, the formula for using `filter` is:


```python
filter(a_function, a_list)
```

And we just saw how to create one-line lambda functions, so the natural marriage of these two concepts is this:

```python
all_people = [
    {"age": 13, "is_vip": True},
    {"age": 13, "is_vip": False},
    {"age": 24, "is_vip": False}
]


# filter with a lambda!
allowed_people = list(filter(
    lambda person: person["age"] > 18 or person["is_vip"],
    all_people))
print(allowed_people) # outputs the first and last people
```

And this really is good news for humanity. That is some lovely code.



Again, `filter` is still receiving two parameters: a function, and a list. The only difference is that now we're using a lambda function instead of defining a separate function outside of the `filter`