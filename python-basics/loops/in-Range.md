We can also write loops in Python that are independent of a list, using the `in range(...)`` syntax, which looks like this:


```
for i in range(0, 10):
	print(i)
```

The above prints the numbers 0, 1, 2... 9 (i.e. 0 until, but not including, 10)



This syntax allows us to determine where the iteration begins and ends, and do something for each of those operations.

The `in range` approach is particularly useful when we know we only need to do a certain number of operations, for example: sending an email to the top 5 customers:


```
customers = ["Julia", "Kelly", "Leah", "Maurice", "Nigel", "Oscar", "Patricia"]

for i in range(0, 5):
	print("Send email to " + customers[i])
```

The above code will output:

- Send email to Julia
- Send email to Kelly
- ...
- Send email to Nigel


And that's it. Oscar and Patricia will not get an email - they're probably not loyal customers anyway.


<hr/>


There really is little difference between a normal `for in...` and a `in range(...)`` loop - the major different is the value of the placeholder variable being used:

- In a `for...in loop`, the variable is each value in the list we're iterating over.
- In a `in range(...)` loop, the variable is the numbers between the provided range