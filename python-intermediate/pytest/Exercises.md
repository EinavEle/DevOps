
## Exercise 1

Create a file called `exercise_1_test.py`


In this file write two tests:
1. Failure test
2. Success test

Run these two tests together and check the output.



## Exercise 2

**Prime number**


Create a class file called primes.py

In this file write two function:
1. `is_prime(number)` - this function return **True** if number is prime, **False** otherwise
2. `are_prime_numbers(*args)` - this function return **True** if **all** given number are primes, **False** otherwise

- Remember [*args](https://realpython.com/python-kwargs-and-args/)?


Create a tests class file called `primesTest.py` write the following tests using `primes.py` :
1. `test_is_three_prime()` - assert if number 3 is prime
2. `test_five_six_seven()` - asser if numbers 5,6,7 are primes
3. `test_one()` - assert if zero is not a prime number (This test is a negative number)



## Exercise 3

Create file called listTest.py and implement the following tests:
```python
my_list = ['I', 2, 'Love', 4, 56, 'Coding', "Python", "in", [8,9,10]]

def test_number():
  assert … # Should assert if number 3 is in my_list
  assert … # Should assert if number 56 is in my_list
  
def test_str():
  assert … # Should assert if "I", "Love" and "Coding" are in my_list

def test_upper_str():
  assert … # Should assert if all the strings in my_list are in upper case﻿

def test_negative():
  assert … # Should assert if number 6 is no﻿t in﻿ my_list - result should be true
```
