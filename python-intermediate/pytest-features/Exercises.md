
## Exercise 1

### Fibonacci Sequence


The Fibonacci sequence is one of the most famous formulas in mathematics and CS world. You can read about fibonacci sequence [here](https://www.mathsisfun.com/numbers/fibonacci-sequence.html).


Create file called 1, in that file:
1. Write a function 1 - return the fibonacci number for a given index (for example: 1).
2. Write tests for different couples, each couple will have the index of the number in the sequence and the fibonacci number related to that index. For example, (2,1) should PASSED, but (5,4) should Fail



## Exercise 2

Create a new file called `storeTest.py` and add this setup function for initialising the store:
```python
def store():
  items = ("apple", "banana", "orange")
  amount = (2, 2, 1)
  return dict(zip(items, amount)) 
```
- Make sure you understand [zip](https://www.w3schools.com/python/ref_func_zip.asp) function.



Write 2 simple functions:
- buy_banana
- buy_two_bananas


Write two tests:
- test_buy_banana() 
- test_buy_two_bananas() 


Well done.

Now, Look at your code, make sure you don't have repetition.


## Exercise 3

### Anagram


An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. Here are some examples: `elbow => below`, `act => cat`, `meteor => remote`

You can read more about anagram [here](https://examples.yourdictionary.com/anagram-examples.html).


Create file called anagram.py, in that file:

1. Given two strings `str1` and `str2`, write a function `anagram(str1, str2)` that return **True if str2 is an anagram of str1**
2. Write tests for different couples of inputs




## Exercise 4

### Check Yourself

Did you use the parametrize mark for the fibonacci tests? And what about the anagram tests?

Did you use the fixture for the store?

If not, go ahead and fix your tests.

