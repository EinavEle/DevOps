
## Reduce

**Implement the function reduce.**


The function signature is:
```python
reduce(function, iterable[, initial]) -> value
```


|||important
## Optional

do notice this part `[, initial]` means that the initial argument is optional and can be passed and used in a function
|||

Where:

**function**: A function to execute on each element of the iterable.

It takes 2 arguments:

**accumulator** - The accumulator accumulates the function's return values.

It is the accumulated value previously returned in the last invocation of the function or

the initial value, if it was supplied.


**currentValue** - The current element being processed in the iterable.


**initial** (Optional) - A value to use as the first argument to the first call of the function.

If no initial value is supplied, the first element of the iterable will be used and skipped. 


The function definition is:

Apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.


For example:

If we call reduce with a sum function and a list of `[1, 2, 3, 4, 5]`) it will calculate `((((1+2)+3)+4)+5)`.

---

### Tests


To test your function try to

multiply a list **[1,2,3,4,5] => 120**

multiply a list of **[1,2,3,4,5]** with initial value of **0.5** => 60


## Max Arguments

**Write a function that can be called with any number of arguments.**
```python
func = max_arguments()
func(1)
func(1,2,3,4,5)
func()
func(1,2) 
```



The function should return **the maximum number of arguments that it was called with**.

For Example:
```python
print(func())           # 0
print(func(1,2,3,7))    # 4
print(func(9,2))        # 4
print(func(1,2,3,4,5))  # 5 
```


## Increase

**Write a function that will generate functions that will increase a specific key of an object.**


The generating function will receive a key parameter to specify the key in the object that should be increased, and an optional argument amount that will specify how much should it increase in each call, the default is 1. It should return a function that given an object will increase the relevant field by the relevant amount.


Now let's test it.


Given an employee:
```python
employee = {
  "name": "Momo",
  "age": 61,
  "salary": 10000
} 
```

Generate 2 functions:

1. Increase the employee **age by 1**
2. Increase the employee **salary by 1000**


Momo works in a company that gives a 1000 raise every 2 years.

Momo will retire in the age of 70.

Run the code that will check what will be Momo's salary when he retires.


<details>
  <summary>
     Hint ..
  </summary>
    It should be 14,000
</details>
