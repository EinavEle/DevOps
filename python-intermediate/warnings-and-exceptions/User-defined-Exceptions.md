It is possible (and even suggested) to implement your own kinds of exceptions. It is done by inheriting from *Exception* class:

```Python
class NoMoneyLeft(Exception):
  """That what happens when you use credit card"""
  pass

class DogAteHomework(Exception):
  """Kids use it all the time, but it happens!"""
  pass

class NothingExceptionalHappend(Exception):
  """Just a normal afternoon"""
  pass
    
try:
  raise NoMoneyLeft:
  # raise DogAteHomework
  # raise NothingExceptionalHappend
except NoMoneyLeft
  print("Call mommy")
except DogAteHomework:
  print("Call daddy")
except NothingExceptionalHappend:
  print("Call the cops")
```
