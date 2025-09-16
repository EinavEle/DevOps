Often times when you write code, you will accidentally make a mistake.

These mistakes are known as **bugs** in our code. There are a few types of bugs, but we will focus on:



- Syntax
- Runtime
- Logical




## Syntax Errors



These bugs are the easiest to spot because your code won't even execute when they happen. 

Syntax errors are when you've written invalid code that the computer does not know how to read. For example:


```
print("Won't see this")
print(!)
```

If you execute the above code, you'll see an error that looks like this:


```
SyntaxError: invalid syntax
```

You won't see the text from the first `print`, because the `!` completely threw Python off - it does not know how to handle random symbols, so it **crashes** the entire application.



Thankfully, these errors usually come with a clear indication of where in your code the error happened (i.e. what line, in what file) - so you should read the error carefully, and then go **debug**, i.e. fix your code.





## Runtime Errors



These are a little trickier to spot, because your code will run properly **until** the computer tries to execute the bad code. Here is an example:


```
print("All good")
print(4 + " children")
```

When you execute the above, you will see `All good` output, but then you will see something like this:

This second line is problematic because in Python we cannot concatenate a number and a string (without using the `str` command).

If you try to execute the above code, this is the output you will see:


```
TypeError: cannot concatenate 'str' and 'int' objects
```

These kinds of errors also usually come with a clear indication of where they happened, so they tend to be easy to fix if you read the output.





## Logical Errors



These are the hardest ones to find, because your application will keep running, but you will get the wrong result.

For example, say we are writing a program that determines if someone is allowed to vote. To vote, you have to be at least 18 years old.

Here is our code:


```
name = "Gina"
age = 23

print("Can " + name + " vote?")
print(age <= 18) # outputs: False
```

The code outputs `False`, even though Gina is 23 years old.

Nothing crashed, no errors are output, but we the developers made a mistake: we used `<=` instead of `>=` - there is no way for the computer to know what we meant, which is what makes these bugs hard to find.


<hr/>


Bugs and **debugging** (the process of getting rid of bugs) are a natural part of programming - don't get discouraged if you make mistakes; it happens to all developers!