To write a function in Python, we use the reserved keyword `def`:


```
def say_hello():
	print("Hello there")
```

All we've done above is define a simple procedure: print "Hello there" to the console.



However, if you execute the above code, you'll note that nothing happens. That is because **defining a function does nothing** - we have to invoke the function in order to execute the code inside of it.



Function invocation looks like this:


```
say_hello()
```

Running the above code will execute all the code inside of the `say_hello` function, so now we will see `Hello there` output in the console.



As you can see, invoking a function is simply a matter of using the function's name, followed by parentheses: `()` - the parentheses are what tell Python "Hey! Go inside this function, and run any code inside of it."



One of the nice thing about functions is that they allow us to write bits of code, and only use them when we need.