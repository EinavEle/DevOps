# Intro

**Single and double underscores** have a meaning in Python variable and method names. Some of that meaning is merely by convention and intended as a hint to the programmer — and some of it is enforced by the Python interpreter.


Here we will discuss the following five **underscore patterns** and **naming conventions** and how they affect the behaviour of your Python programs:

- Single Leading Underscore: `_var`
- Single Trailing Underscore: `var_`
- Double Leading Underscore: `__var`
- Double Leading and Trailing Underscore: `__var__`
- Single Underscore: `_`


Let’s dive right in!




## 1. Single Leading Underscore: `_var`


When it comes to variable and method names, the single underscore prefix has a meaning by convention only. It’s a hint to the programmer, but it does not affect the behaviour of your program.

The underscore prefix is meant to hint that a variable or method starting with a single underscore is intended for internal use. This convention is defined in PEP 8. 

This isn’t enforced by Python. Python does not have strong distinctions between **“private”** and **“public”** variables like Java does.


Take a look at the following example:
```
class Test:
  def __init__(self):
    self.foo = 11
    self._bar = 23

  def add1(self):
    self._bar += 1 
```
Here `_bar` is meant to be used only inside the class.

If we want we can create an instance and access the `_bar` property, there is no restriction, but we should take under consideration that that was not the intention of the programmer that wrote the class.
```
 t = Test()
 >>> t.foo # 11
 >>> t._bar += 2
 >>> t._bar 25
```


## 2. Single Trailing Underscore: `var_`


Sometimes the most fitting name for a variable is already taken by a keyword. Therefore names like class or def cannot be used as variable names in Python.


In case you still want to use it you can append a single underscore to break the naming conflict:
```
def make_object(name, class):
  pass   
```

This code will throw a `SyntaxError: "invalid syntax"`


Instead, add to class a trailing _:
```
def make_object(name, class_):
  pass 
```

In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords.




## 3. Double Leading Underscore: `__var`


The double underscore prefix, **is not just a name convention**, it affect the interpreter.

This name pattern helps us create unique class properties (functions or variables) that **cannot be overridden**.


Let's take a look at this class:
```
class Test:
  def __init__(self):
    self.foo = 11
    self.__baz = 23

  def add(self):
    self.__baz += 1
    print(self.__baz)
```

Here we define a class variable `__baz`.

We can access the variable internally, within the class, in our example in the `add` method.


```
instance = Test()
instance.add() 
```

Run this code and you will see a print of `24`.


But if we try to access the variable:
```
print(instance.__baz) 
```

We will get an `AttributeError`:

    'Test' object has no attribute '__baz'


This is because the interpreter will create a new name for the `__baz` property, a name that is combined from the name of class as well. The new name is: `_Test__baz`.


So we can access the `__baz` variable like this:
```
print(instance._Test__baz) 
```

This behavior helps us guarantee that if another class extends Test it cannot override the `__baz` property.


## 4. Double Leading and Trailing Underscore: `__var__`


**Side Note:**
Before we start, just a quick moment for terminology.

`__` - double underscore - is also called **"dunder"** in short. Just to get you in place with the pythonic language :)


Names that have both leading and trailing double underscores are reserved for special use in the language. This rule covers things like `__init__` for object constructors, or `__call__` to make an object callable.


It’s best to stay away from using names that start and end with double underscores (“dunders”) in your own programs to avoid collisions with future changes to the Python language.


It is important to note that name mangling is not applied if a name starts and ends with double underscores. Variables surrounded by a double underscore prefix and postfix are left unscathed by the Python interpreter:
```Python
class PrefixPostfixTest:
    def __init__(self):
      self.__bam__ = 42
      
>>> PrefixPostfixTest().__bam__ # 42 
```

## 5. Single Underscore: `_`


Per convention, a single standalone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant.

For example, in the following loop we don’t need access to the running index and we can use “_” to indicate that it is just a temporary value:
```
for _ in range(5):
  print('Hello, World') 
```

You can also use single underscores in unpacking expressions as a “don’t care” variable to ignore particular values.

Again, this meaning is “per convention” only, the single underscore is simply a valid variable name that’s sometimes used for this purpose.


In the following code example I’m unpacking a car tuple into separate variables but I’m only interested in the values for color and mileage.

However, in order for the unpacking expression to succeed I need to assign all values contained in the tuple to variables. That’s where “_” is useful as a placeholder variable:
```
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color) # 'red' 
```

Note that we can also print the _ :
```
print(_) # 12 
```

Besides its use as a temporary variable, “_” is a special variable in most Python REPLs that represents the result of the last expression evaluated by the interpreter.

This is handy if you’re working in an interpreter session and you’d like to access the result of a previous calculation. Or if you’re constructing objects on the fly and want to interact with them without assigning them a name first:
```
>>> 20 + 3 23
>>> _ 23
>>> print(_) 23
>>> list() []
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _ [1, 2, 3]  
```
