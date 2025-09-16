Sometimes we want to set a default value for a function parameter.

That means that it is an optional parameter, and the user does not have to pass it.

In case the user did not pass this parameter we want to automatically set a default value.



Let's look the python built-in `round` function.

It has a mandatory parameter `x`, which if the number we want to round.

So to round number `0.123456` we will execute:
```
round(0.123456)
# returns 0
```
How does python know how to round the number with no decimal digits?



Very simple, it has a **default parameter** called `n` that is initialised to 0 if not defined.



If we want to round a number to 2 decimal digits we can pass a n argument like this:
```
round(0.123456, 2)
```

How is it done?


```
def my_round(num, decimal_digits_limit=0):
    print(f'num =  {num}')
    print(f'decimal_digits_limit =  {decimal_digits_limit}')
```

Here we define my_round with 2 parameters:

- 1 mandatory (num)
- 1 optional (decimal_digits_limits)


Note: For simplicity we will not implement the method only print its arguments.



Now we can call the function with decimal digits limit or without it:
```
my_round(0.123456)
# 0.123456, 0 
my_round(0.123456, 2)
# 0.123456, 2
```
Try to run the function and see the results!


A small note before we continue:
`pass` keyword is a null operation - when it is executed, nothing happens.

It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed.

For example, an empty function:
```
def foo():
    pass
```

If we try to leave the function empty:
```
def foo():
``` 
We will get an error.

Now, we can continue.



Function Parameters have one rule!



**Required (mandatory) parameters must come first!**



Try running this example:
```
def foo(x=0, y):
    pass


foo()
```

You will get a `SyntaxError`:
```python
SyntaxError: non-default argument follows default argument
```


In order to make the function run we need to place the required parameter first and then the optional:
```
def foo(y, x=0):
    pass
```