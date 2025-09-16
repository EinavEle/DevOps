In our Person class we have these two new concepts: `init` and `self`:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
```

The init is short for **initializer** - it helps us **initiate** or instantiate objects. The init is a function (known as the **constructor**) that exists in any class (whether you write it out or not), and **it gets invoked as soon as we create an instance** of the class.


We never explicitly call init ourselves, but it gets invoked automatically.

So what's going on in this function?


In `init` we literally initialize the class attributes.

In other words, it is where we declare what properties any instance of the class will have.


The parameters of `init` work like the parameters of a function, in that we can use them as normal variables. For example, we could do something like this:

```python
class Person:
  def __init__(self, name, age):
    self.name = "Doctor " + name
    self.age = age 
```

Then if we instantiated a new Person:

```python
p = Person("Alice", 31) 
print(p.name)  
```

We'd see Doctor Alice


**In summary:** the `init` function is the **setup** area of a class. It is where we set our class attributes, and possibly execute other setup operations.

Now let's understand self ...



## The `self` keyword

In a normal Python class, any function's first parameter needs to be self. Python uses self in order to allow you to reference the instance itself. In the constructor (init), we use self to associate the attributes with the instance to be created. To understand this, take a look at this code:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ana", 8)
p2 = Person("Javier", 6)
print(p1.name) # outputs: Ana
print(p2.name) # outputs: Javier 
```

Both `p1` and `p2` are instances of the same class, `Person`.
However, `p1.name` and `p2.name` have different values exactly because self associates `Ana` to `p1`, and `Javier` to `p2`.
Without `self`, any instance we created would have the same values - and that's pretty useless.
