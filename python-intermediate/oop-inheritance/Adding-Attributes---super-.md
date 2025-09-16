Say we want to differentiate our Actor from our Artist a little, but we don't want another method. We only want to identify which movie the actor is most known for. We can add a new attribute to the class. To add attributes beyond those the parent gave us, we use the self keyword. But before that, we must invoke the parent constructor using the `super` keyword:

```python
class Actor(Artist):
  def __init__(self, name, income, most_known):
    super().__init__(name, income)
    self.most_known = most_known

a = Actor("Al", 24, "Scar")
a.perform()
print(a.most_known) # outputs: Scar 
```

We use super when we want to **invoke the parent's constructor** - we can see that explicitly above as we are literally invoking `__init__`; in particular, we are invoking it with the `name` and `income` arguments, the two parameters that Artist knows how to handle.


Once we're done passing the relevant attributes to the parent, because we are now in the Actor's own `__init__`, we are free to add a unique attribute that is only meant for Actor, and neither for Singer nor Artist


So now we are able to create a class, inherit from it, *and* make the child unique in its own right.
