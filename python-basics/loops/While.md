Sometimes we want to execute some code, but we don't know how many times the code needs to run.

For these cases, we have a `while` loop.



For example, say we want to generate random numbers and sum them until we get to a certain value. It could take 10 iterations, or 30 - we don't know how many, but we do know what the end condition is, and that's exactly what we check in a `while`



Check out this code and make sure to read the comments:
```python
from random import randint # will give us access to random numbers - this is built-in to Python

desired_sum = 50
current_sum = 0

# the "end condition" after the `while` keyword determines when the loop ends
# in other words, so long as `current_sum` is less than `desired_sum` - the loop keeps going!﻿
while current_sum < desired_sum:
	rand_num = randint(0, 10) # generate a random number between 0 and 10
	current_sum = current_sum + rand_num # updating the value of `current_sum` by adding the randomly generated number to it

print(current_sum) # outputs: at least 50
```

This might seem like a silly example - but imagine you want to give your clients gift cards valued at random amounts, but you want to cap your gift at a certain amount of money.



This is where a `while` loop is perfect: loop through clients and, so long as you haven't passed the cap, keep giving gift cards with random amounts of money.