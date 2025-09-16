Say we have these two classes:

```python
class Singer:
  def __init__(self, name, income):
    self.name = name
    self.income = income

class Actor:
  def __init__(self, name, income):
    self.name = name
    self.income = income 
```

Clearly there are differences between an actor and a singer, but certainly there are overlaps as well, as we see above.


This is a classic use-case for inheritance: instead of repeating attributes (and possibly methods) in separate classes, we can create a **parent** class that will use as a representative of most of the general attributes/methods of both classes, and then each **child** class will **inherit** from this parent, adding whatever unique attributes/methods it needs.


Let's see this in practice:

```python
class Artist:
  def __init__(self, name, income):
    self.name = name
    self.income = income

  def perform(self):
    print(self.name + " is performing now") 
```

Here we've defined a new class - Artist - with the same attributes, but also with a perform method. This will be our super class. Now let's turn Singer and Actor into children:

```python
class Singer(Artist):
  pass
  
class Actor(Artist):
  pass 
```

A few things going on here:
- In order to **inherit**, we pass the parent class to the child class, as we've done above.
- The pass keyword says "Do nothing, and just accept everything from the parent".


It may seem silly to have a child that is exactly like it's parent, but we'll make it more interesting soon. For now, check this out:

```python
s = Singer("Lis", 43)
s.perform() # outputs: Lis is performing now
a = Actor("Al", 24)
a.perform() # outputs: Al is performing now 
```

Here's the cool bit: **we didn't define any attributes or methods** in the child classes, **but they still have access to everything from their parents** - that's exactly what inheritance is, and how it works.


Singer and Actor **don't need** to define `name`, `income`, and `perform()` - because their parent defines it for them!

Of course, when we make an instance of a Singer or an Actor, we still have to pass the relevant arguments, but that's all!
