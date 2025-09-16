As we write more code, and more complex code, it is useful to be able to check what kind of data we are working with.


At the simplest level, we know that "shoobert" is a string, 42 is an int, and True is a boolean.

We can validate this at the Pythonic level by using the type function, like so:

```python
print(type("shoobert"))
print(type(42))
print(type(True)) 
```

And accordingly, we'll see the following in the output:

```output
<class 'str'>
<class 'int'>
<class 'bool'> 
```

Look at that! It should come as know surprise that we see str, int, and bool - but they're all a class! Fun fact.


---


Let's take this a step further and use type on our own instances:

```python
class Artist:
  def __init__(self, name, income):
    self.name = name
    self.income = income
  
class Actor(Artist):
  def __init__(self, name, income, most_known):
    super().__init__(name, income)
    self.most_known = most_known
    
class Singer(Artist):
  def perform(self):
    print(self.name + " is singing now")
    
s = Singer("Ellie", 400)
a = Actor("Jerome", 450, "Leob")
ar = Artist("Arnie", 210)
print(type(s))
print(type(a))
print(type(ar)) 
```

Running the above code outputs:
```output
<class '__main__.Singer'>
<class '__main__.Actor'>
<class '__main__.Artist'> 
```

Which should come as no surprise. But now we're going to look into isinstance - and that's a fun one.


## isinstance


Check this out:

```python
isinstance(s, Singer) # outputs: True 
```

Using the same instance and class from before, we understand that `isinstance` is a built-in function in Python that returns `True` or `False` depending on whether the first argument (the instance) *is an instance* of the second argument (the class).


In the above case, it's naturally true.


But now check this out:

```python
isinstance(s, Artist) # outputs: True 
```

This is also True! That means that s, an instance of Singer, is both a Singer **and** an Artist - cool!

This idea of being two things at once is broadly referred to as **polymorphism** - but we won't get into that right now.


However, note that `s` is **not** an instance of `Actor`, even though `Actor` is also a child of `Artist`. In other words, this is false:

```python
isinstance(s, Actor) # false. 
```
