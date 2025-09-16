So far we understand that a function:

- Executes some procedure/set of commands
- Can receive an input


The only missing piece of the puzzle is that a function can also give an **output** - for this we need to introduce the `return` statement:


```
def determine_outfit(temperature):
	if temperature > 25:
		return "t-shirt"
	else:
		return "jacket"

determine_outfit(36)
```

If you execute the code above we will see -- nothing! So what is `return` doing?



When we use `return` in a function, it does two things:

1. Ends the function **immediately**
    - This means that if we reach a `return` in the function absolutely no code afterwards (in the function) will execute
2. Allows us to capture the value that is being returned from the function


Here's how #2 looks in practice:

```
outfit = determine_outfit(36)
print(outfit) # outputs: t-shirt
```

What we've done now is

- invoked the `determine_outfit` function
- passed it the value of `36` - this is our **input**
- captured `t-shirt` inside of our new variable `outfit` - this is our **output**


**Note** that if we had passed `20` as an argument instead of `36`, the value of `outfit` would be `sweater` instead - that's because of the logic inside of our function.



This is why functions are often called **input-output machines**: given some data, do some processing, and output some data back.