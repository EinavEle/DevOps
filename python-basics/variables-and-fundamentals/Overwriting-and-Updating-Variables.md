Whenever you define a variable in Python, you can always reset its value with something else, or update it.



Here is an example of **overwriting**:


```
favorite_movie = "The Lord of the Rings"
favorite_movie = "The Lion King"
```

As you can see, we are simply re-defining the variable with a new value.

Notice that we could overwrite it with a different type as well, but typically we shouldn't do that. In other words, **this is considered bad**:


```
stuff = "Bread"
stuff = 42
```

<hr/>

Instead of completely resetting a variable, we can also update it via mathematical operations or concatenation, like this:


```
name = "Jillian"
name = name + ", PhD"

print(name) # outputs: Jillian, PhD
```

In this case we still have the variable `name`, but its value has been updated - this is great, as it means our variables are dynamic, meaning they can change.



We can also update numbers in a similar way:


```
number_of_kids = 1
adopted_kids = 2

number_of_kids = number_of_kids + adopted_kids
print(number_of_kids) # outputs: 3
```

Updating variables is something we do quite often, so make sure you're comfortable with this idea.