Let's expand our Person class to make it a little more interesting:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def introduce(self):
    print("Hi there, I am " + self.name) 
```


Now as well as the `init` and some attributes, we have another function: `introduce`


In fact, when we define functions inside of a class, we call them **methods**. It's just a fancy name for the same thing: an input-output machine.


Methods work exactly the same way as functions:
- We define them with def
- They can receive parameters
- They have to be invoked, with arguments if necessary


The only big difference between methods in a class and normal functions is that the first parameter has to be self - and here we see a good use of that: when we invoke introduce, we want it to use the associate name attribute - and the only way to access that is through self:

```python
p1 = Person("Jezrien", 102)
p2 = Person("Tal", 96)
p1.introduce() # outputs: Hi there, I am Jezerien
p2.introduce() # outputs: Hi there, I am Tal 
```

Notice that it is `p1` and `p2` that invoke introduce - **we cannot invoke class methods without an instance** of that class. This is important.
