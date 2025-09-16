
## Exercise #1 : My Enumerate
### Instructions :

Implement the enumerate Python function.

You can call your function `my_enumerate`

Read about it [here](https://www.programiz.com/python-programming/methods/built-in/enumerate)

Obviously, do not use the python built-in enumerate function itself.


### Tests:

Make sure the following tests pass:

- Test #1 :*
```python
for index, elem in my_enumerate([10, 20, 30, 40]):
  print(index, elem) 
```
Result:
```console
0 10
1 20
2 30
3 40
```

- Test #2 :*

```python
for index, elem in my_enumerate([10, 20, 30, 40], 10):
  print(index, elem)  
```
Result:
```console
10 10
11 20
12 30
13 40
```

## Exercise #2 : My Accumulate
### Instructions :

Write a `my_accumulate` generator that returns a series of accumulated sum.


For Example:
```python
for elem in my_accumulate([1,2,3,4,5]):
  print(elem) 
```
Will return:
```console
1
3
6
10
15
```

## Exercise #3 : Prime Factors Generator
### Instructions :

Write a generator that returns the [prime factors](https://www.mathsisfun.com/prime-factorization.html) of a number.


In short, factors are numbers which by multiplication give a number.

For example, 2,6 are factors of 12, but 6 is not a prime number.

The prime factors of `12` are: `2,2,3`.


Now don't get lazy and check your solution.

For example:
```python
for x in get_prime_factors_generator(100):
  print(x) 
```
Would print:
```console
2
2
5
5
```

## Exercise #4 : Circle Iterator
### Instructions :

Create an iterator `CircleIter` that given a sequence and a <number of times>, will go through the elements in the sequence <number of times> times.

If the sequence is finished, start from the beginning.

Implement the iterator using a class that implements the iterator interface.

**Note:** You are *not allowed* to use the iterator interface in your implementation.


- Usage Example:
```python
for x in CircleIter([1,2],5):
  print(x, end=" ") 
```
The output should be:
```console
1 2 1 2 1 
```

- Another Example:
```
for x in CircleIter([1,2,3],4):
  print(x, end=" ")
  for y in CircleIter([5,6],3):
    print(y, end=" ")
print() 
```
The output should be:
```console
1 5 6 5 
2 5 6 5 
3 5 6 5 
1 5 6 5 
```