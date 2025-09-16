Operators are symbols (or a series of symbols) that allow us to perform certain basic operations.



We will begin with operators with which you are probably familiar: mathematical operators.





## Mathematical Operators



The symbols we use when we want to perform mathematical operations are:

- `+` - plus; addition
- `-` minus; subtraction
- `/` - slash; division
- `*` - asterisk; multiplication


We use these symbols intuitively, so let's see a few examples:


```
print(3 + 5) # outputs 8
print(10 / 2) # outputs 5
```

We can also use **parentheses** to create **expressions**, like this:


```
print( (3 + 5) * (10 / 2) ) # outputs 40
```
Notice that when we write expressions, Python will **evaluate** them inside-out (i.e, first the inner expressions in the parentheses, then go out) - this is true in other cases as well, not just mathematical operations.



We can also **store the results of operations in variables**, like this:


```
current_score = 80
points = 20

final_score = current_score + points
print(final_score) # outputs 100
```

Note that in the code above we've declared a new variable, `final_score`, and its value is the sum of two other variables - this is perfectly valid and applies in other situations too, not just for math operations.







## Comparison Operators



When we need to compare values, we can use the `==` operator, called **double-equals**, to check for equality. This operator will **always output a boolean** value:


```
print(3 == 5) # outputs False

status = "father"
print(status == "father") # outputs True
```

Notice the difference in this code between **assigning** the value "father" to the variable `status`, and **comparing** whether the value of `status` is the same as the string "father" - this difference is crucial to understand.


<em>Remember: when you want to declare a new variable, you assign its value with a single equals sign; when you want to compare variables, you use the double-equals.</em>


<hr/>


We can also compare whether two things are not equal using the `!=` operator:


```
print(3 != 5) # outputs True
```

Simple enough.

<hr/>

We also have other operators to compare values that aren't exactly equal or not equal:



- `<` - less than
- `>` - greater than
- `<=` - less than or equal
- `>=` - greater than or equal


These are also used intuitively:


```
print(3 < 5) # outputs True
print(3 < 3) # outputs False
print(5 >= 5) # outputs True
```

Of course, the same rules of expressions and creating variables apply, which we will see shortly.





## Logical Operators



We use comparators (equals, greater than, etc) to define "logical flow" in our app, which we will explore later, but before that we will see a way to combine operators with logic, using the following operators:



- `and` - operator that requires two `True` values
- `or` - operator that requires at least one `True` value
- `not` - operator that changes a `True` expression to a `False` one, and vice-versa


Let's understand these with a few examples:


```
age = 18
is_citizen = True

print("Can this person vote?")
print( (age >= 18) and is_citizen ) # outputs True
```

You can think of the `and` operator as one that outputs `True` if the expressions on its left **and** its right **both** resolve to `True`

If you want to break-down how Python is executing the code above, you can think of it like this:


```
print( (age >= 18) and is_citizen) ) 
# Python first evaluates the (age > 18) expression, and then it sees this:
print( True and is_citizen)
# Which is simply:
print( True and True)
# And because of the way the `and` operator works, the above resolves to:
print(True)
```

Here is a slightly more complex example:


```
age = 18
is_long_line = True

print("Can this person vote?")
print( (age >= 18) and not is_long_line ) # outputs False
```

The reason the above outputs `False` is because we are flipping the value of `is_long_line` when we put a `not` in front of it.

Breaking it down, it looks like this:


```
print( (age >= 18) and not is_long_line )
print( True and not is_long_line)
print( True and (not is_long_line) ) # adding parentheses for emphasis
print( True and (not True) )﻿
print( True and False )

# Finally, because `and` requires both expressions on its left and right to be True:
print(False)
```

The way `or` works is similar to `and`, except `or` needs at least one side to be `True`, so the expression `True` or `False` would output `True`:


```
print( (3 < 5) or (5 > 3) ) # outputs True
```

You can write out the break-down on your own ;)