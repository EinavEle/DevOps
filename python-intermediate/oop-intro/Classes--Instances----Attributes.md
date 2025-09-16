One of the core principles of OOP is **encapsulation** - this means wrapping our code into isolated parts, each with its own responsibility. When we write functions, for example, we are encapsulating a small bit of code that executes a set of commands.


In OOP, the broadest form of encapsulation is when we write a **class**, which at its most basic looks like this:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
```

One of the most important things to remember about a class is that **it is only a blueprint** - by itself, a class does nothing. It merely tells us how a "Person" is meant to look. It does not create anything at all.

Before we talk about init and self, let's see how we use this blueprint to create an **object**.


## Instantiation

An **object** is some entity that has either attributes, methods, or both.

**Attributes** are defining characteristics of an object - like name or age - and **methods** are tasks the object can do; we'll look at these later.


In the `Person` class above, we have two attributes: `name` and `age`, and in order to create an **instance** (i.e. object) of a Person, we need to **instantiate** it, like this:

```python
person1 = Person("Liam", 38) 
```

In the above code we "called" the Person class and passed it the "parameters" it expected - a name and an age.

But Person is not a *function*, it's a class. So "Liam" and 38 are technically not parameters, but rather the **attributes** of this particular *instance* of a Person - our variable `person1`


An **instance** is a *physical manifestation* of a class, a proper object.

Remember: a class is only a **blueprint**; an instance *uses* that blueprint to create an actual object that we can use.


We can use objects in a similar way that we use dicts in Python, but instead of accessing their keys with brackets, we use **dot notation**, like this:
```python
print(person1.name + " is " + str(person1.age) + " years old")
# output: Liam is 38 years old 
```

Of course, you can make as many instances (objects) from a class as you like:
```python
person1 = Person("Liam", 38)
person2 = Person("Alex", 22)
person3 = Person("Luis", 19)
person4 = Person("Ben", 27) 
```

And because they're simple objects, we can use them as we would use a regular dict - for example, storing them in a list and iterating over them:
```python
imaginary_friends = [
    Person("Liam", 38),
    Person("Alex", 22),
    Person("Luis", 19),
    Person("Ben", 27)
  ]
  
for buddy in imaginary_friends:
  print(buddy.name + " is my friend. Really.") 
```

Objects are great.
