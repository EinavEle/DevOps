A simple function like `say_hello` is pretty limited - because it will always do the same thing.



One way to make a function more dynamic is to introduce the concept of **parameters**. A parameter is an **input** of a function, which we can use inside the function's **body** (i.e. indented under the `def`). Here is `say_hello` again, but this time with a parameter:


```
def say_hello(name):
print("Hello there, " + name)
```

Now this function expects to receive some input in order to work. The parameter, `name`, is the input - and it has to come from outside. But inside the body of the function, `name` is just a normal variable - that's why we can concatenate with it.



When a function expects a parameter, we need to invoke the function with some appropriate **argument**(s), like this:


```
say_hello("Sheila")
```

The above will invoke/run/execute `say_hello` and give it the value "Sheila" - this value goes inside the parameter `name`!

So now when we say `print("Hello there, " + name)` we're really saying `print("Hello there, Sheila")` - nice.



Another nice thing about functions is that they are reusable - that is, we can invoke them as many times as we want:


```
say_hello("Kyle")
say_hello("Julia")
say_hello("Oren")
say_hello("Gilgamesh")
```

And the function will always execute the same code for each invocation, except with different arguments.

<hr/>



Of course, the `say_hello` example is silly because we already have a function that prints some data to the console - `print`! Print is a function that receives a parameter, and outputs that parameter to the console.



However, `say_hello` makes our life a little bit easier, because instead of writing `print("Hello there, Sheila")` we can just write `say_hello("Sheila")`, and define inside the function that it should print with `Hello there`,  before the name - that's convenient.