For the computer to "remember" some value, we as the developers have to **define** a variable and give it the value we want to remember. For example:


```
name = "Serena"
```

In Python, variable definition is straightforward:



1. Make up a (sensible) name for the variable
2. Use the equal sign ( `=` ) to **assign** the value into the variable


From this point on in the app, the computer will remember that `name` is a placeholder for "Serena", so if you execute these commands:


```
print("Welcome, " + name)
print(name + ", would you like to see some Tennis Rackets?")
print("Happy to have you back soon, " + name + "!")
```

You will see this output:


```
Welcome, Serena
Serena, would you like to see some Tennis Rackets?
Happy to have you back soon, Serena!
```

Even though the name you choose for the variable can be anything, for example:


```
mirror = "Serena"
print("Hi, " + mirror) # outputs "Hi, Serena"
```

We prefer to use sensible variable names to make our code easier to read.



<hr/>

**Note**:  we use the `#` symbol to write **comments** in our code. A comment will be completely ignored when you execute your code, but can sometimes help the developer make some notes for context or clarity.

<hr/>



### Longer Variable Names

When we need a variable name to be longer, the common practice in Python is to use the `_` (underscore) symbol to separate between words:


```
favorite_show = "Pokémon"
number_of_pokemon = 151
```

Variable names can also have numbers, but must start with a letter:


```
pokemon_1 = "Bulbasaur" # good
4_pokemon = "Charmender" # bad
```