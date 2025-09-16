When we talk about variables, aside from defining them we also have to note what the variable's **type** is:


```
best_vegetable = "carrot"
carrot_price = 4
```

We say that the `best_vegetable` variable is of type **string** - that is, any text wrapped between quotes.

Next, the `carrot_price` variable is of type **integer** - that is, a whole number.



It is important to make the distinction between variable types because some operations can be done with certain types but not with others.



We'll dive deeper into operations later, but for example:


```
print(5 + 5) # operation that makes sense
print(5 + "sugar") # nonsense operation
```

Remember: **anything in quotes is a string**. If it doesn't have quotes, it's either a variable, or a different data type.





## Booleans

The third basic type in most programming languages is called a **boolean**, and it is special because it has only two possible values: `True` and `False`. For example:


```
is_good_day = True 
# capitalization matters, i.e. it's True, not true

should_eat_burger = False
```

Note that we typically start names of variables that have boolean values with words like `is`, `should`, `has`, or we give them a name that could have a "yes" or "no" answer, like `exists` or `found`



These data types come into play later on when we start talking about conditions in our program, but for now it is enough to know that they exist.



We can use the built-in function type to discover the type of a variable:

```
i = 9
print(type(i))

b = True
print(type(b))

s = "text"
print(type(s))

n = None
print(type(n))
```

and this will be the result:

```
<class 'int'>
<class 'bool'>
<class 'str'>
<class 'NoneType'>
```

You can see that there is an additional type: `NoneType`

`None` is like `null`, if you know it from other languages.

it is a python keyword used to define no value at all.