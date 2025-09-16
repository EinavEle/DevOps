The most basic flow of input and output (in short I/O) is to ask the user for some input, store it, use it and then return an answer to the user.



It looks like this:
```
name = input("what is your name?")

print("Hello " + name)
```

The `input` function prints the user a message and waits for the user to type an input.

Then the user will type an input - his name, in the cmd, and the program will continue its execution, printing `"Hello <name>"`



Python provides us with two bulit-in functions for I/O: input() and print().



## input()



We can use the input function with or without a message:
```
input()

input("Dear user, please enter a key:")
```

It is important to remember that every input we get comes as a **string**:

If we do not remember that, we can get some surprising results:


```
num = input("Pick a number, and nothing but a number!")
result = num * 2
print(result)
```

What will happen here?

Run the code and see.

Can you explain why?



We can even get errors:
```
num = input()
result = num - 2
print(result)
```


We can overcome that by converting the string we got to a number:
```python
num = input()
result = int(num) - 2
print(result)
```


Another conversion to a number can be done with `float()`:
```
float("4")
```

With `eval()` we can evaluate a string expression as mathematical expression:
```
result = eval("4 + 8 / 2")
print(result)
type(result)
```

But we cannot use variables and unrecognized names:


```
# Error: eval() must get mathematical symbols
eval("4 + 5 - Moshe")
```



## print()



You already know the `print()` function.

But let's see some more features that you can use.



### Pass multiple arguments


```python
print(1, 2, 3, 4)
# 1 2 3 4
```



### Decide how to end the print



By default python ends the prints with a line break.

But we can decide to end it with a space, which means the next print will start in the same line
```
print("Hello", end=" ")
print("World")

# Hello World
```