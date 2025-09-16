Now let's say we want to make the Singer a little more specific. It should still have a name and income, but its perform should be different:

```python
class Singer(Artist):
  def perform(self):
    print(self.name + " is singing now") 
```

What we're doing above is called **overriding** the `perform` method; this means that now Singer's perform will be different from its parents;

```python
s = Singer("Lis", 43) 
s.perform() # outputs: Lis is singing now
a = Actor("Al", 24) 
a.perform() # outputs: Al is performing now 
```

Even though Singer still has a name and income from its parent, it has now defined its own way of performance.


