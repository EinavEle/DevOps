Simple generators can be easily created on the fly using generator expressions. It makes building generators easy. Generator expression creates an anonymous generator function.

The syntax for generator expression is similar to that of a list comprehension in Python:
```python
list_comprehension = [x for x in range(20)]
print(list_comprehension)
print(type(list_comprehension)) 
```
But the square brackets are replaced with round parentheses:
```python
gen = (x for x in range(20))
print(gen)
print(type(gen)) 
```
But we need to remember that although the syntax is very similar, there is an important difference:

**List comprehension returns a full list with all its elements, while a generator expression will return an iterator (that returns items one by one).**


## Advantages of a generator


### Easy to implement

We saw how much more compact generators are :)


### Memory efficient

A normal function that returns a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large.

Generator implementation of such a sequence is memory friendly and is preferred since it only produces one item at a time.


### Represent infinite stream

Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory and since generators produce only one item at a time, it can represent infinite stream of data.


The following example can generate all the even numbers (at least in theory):
```python
def all_even():
  n = 0
  while True:
    yield n
    n += 2 
```
