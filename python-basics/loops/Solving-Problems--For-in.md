Say we had this array:


```
salaries = [1200, 2500, 1800, 1600, 1800, 700, 3200, 1500, 1300, 1300, 850, 1900]
```

And we wanted to determine what the sum of all the numbers in `salary` is.
Loops allow us to do this fairly simply.



Check out this code:
```
sum = 0
for salary in salaries:
	sum = sum + salary

print(sum) # outputs: 19650
```

Here is a break down of what the code is doing:



1. First we create a variable called `sum` whose initial value is 0
   1. We need this variable so that the computer can "remember" the sum as we iterate
2. Then we start to loop through all the `salaries`
3. For each salary we want to add it to the `sum`, so we reset the value of `sum` to be itself (the current total) plus the next `salary` from the list


As a human, you would probably solve this problem the same way:

I start with 0, then add 1200; now I have 1200
Next I add 2500 to 1200; now I have 3700
Next I add 1800 to 3700; now I have 5500
Next I add 1600 to 5500; now I have 7100

etc...



A loop just automates this process for us into a few lines of code - powerful stuff!