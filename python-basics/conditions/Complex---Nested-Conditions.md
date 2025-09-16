The statement in an `if` condition is not limited to one condition; it is certainly possible (and common) to use logical operators when creating an `if` condition.



Here is some code that determines whether to go buy more bananas:


```
bananas_left = 3
desired_bananas = 4
price_of_banana = 2
banana_budget = 10

if (bananas_left < 5) and (desired_bananas * price_of_banana < banana_budget):
	print("Buy bananas")
```

In this case, we will only buy bananas if we have fewer than 5 bananas, **and** we have enough money to buy bananas (in this economy...)

Notice that we use parentheses to separate the two conditions - it's not a must, but it will help you avoid logical bugs.



The limitation of writing a condition like this is that if we wanted to add an `else`, we couldn't tell which condition caused the statement to fail. We could do something like this:


```
if (bananas_left < 5) and (desired_bananas * price_of_banana < banana_budget):
	print("Buy bananas")
else:
    print("Either we have enough bananas or don't have enough money")
```

But that's not great because the output is not 100% clear. The alternative solution is to use nested conditions.



## Nested Conditions

Inside of an `if`'s block, we can write effectively any code - including more `if` statements!

Check out the banana example with a nested statement:


```
if bananas_left < 5:
	if(desired_bananas * price_of_banana < banana_budget):
		print("Buy bananas")
	else:
		print("Want bananas, but not enough money")
else:
	print("You have enough bananas")
```

The code may look a little more complicated, but this makes our logic more explicit. If you read the code slowly, you'll see that all we're saying is:



- If we don't have enough bananas left,
  - And if we can afford them
    - Then get some
   - Otherwise too bad, we don't have enough money
- Otherwise there is no need to buy bananas


Notice that nested conditions (like the second `if` in the above code) will only be checked **if their "parent" condition is `True`**.

In the above code, we will **not** check the budget if we have at least 5 bananas.