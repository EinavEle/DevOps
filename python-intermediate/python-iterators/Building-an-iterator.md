So now after we have learned the iterator protocol we can create our own iterator.

For example:
```python
class PrintNumbers:
  def __init__(self, size):
    self.max = size

  def __iter__(self):
    self.numbers = list(range(self.max + 1))
    self.counter = 0
    return self
    
  def __next__(self):
    if self.counter >= self.max:
      raise StopIteration
      self.counter += 1
      return self.numbers[self.counter] 
```

Here we created a class that implements the iterator protocol.


Now, `printNumbers` instance is an iterable so we can iterate it with a for loop like this:
```python
iterable = PrintNumbers(3)
for num in iterable:
  print(num) 
```
