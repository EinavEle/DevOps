In this lesson we covered

- The for in loop
- The in range loop
- And the while loop


For the following exercises, some will allow you to choose any of the loops, while for others you will probably have to use a specific one.







## Exercise 1

Create two lists of the same length. One with `names`, and one with `ages`.

Using **one** for loop, print out "X is Y years old" for each pair.


<details>
<summary>Hint</summary>
<div> 
since you want to access items from different list at the same index... which loop should you use? Also, you'll be concatenating again.
</div>
</details>



<details>
<summary>Solution</summary>
<div> 

```python
names = ["Daniel", "Michael", "Benjamin"]
ages = [11, 22, 33]

for i in range(0, len(names)):
    print(names[i], "is", ages[i], "years old")
```
</div>
</details>



## Exercise 2

Create an empty list called `nums`

Write a loop that adds the numbers 1, 2, 3,..., 100 to the list

<details>
<summary>Solution</summary>
<div> 

```python
nums = list()

for num in range(1, 101):
    nums.append(num)

print(nums)
```
</div>
</details>


## Exercise 3

Using the `nums` list from the previous exercise, write some code that finds the sum of the numbers that are less than 20 **or** greater than 80.

If you do this right, you should find the sum to be 2,000, which is pretty cool.


<details>
<summary>Solution</summary>
<div> 

```python
nums = list()

for num in range(1, 101):
    nums.append(num)

sum = 0
for num in nums:
    if num < 20 or num > 80:
        sum += num

print(sum)
```
</div>
</details>



## Exercise 4

The following code has a logical bug in it.

Run the code, understand the problem, and fix it:


```
equipment = ["hammer", "ruler", "torch", "scissors", "screwdriver", "scissors", "torch", "hammer", "hammer", "ruler"]
most_common_item = ""
highest_count = 0

for item in equipment:
	count_of_item = equipment.count(item)
	if count_of_item > highest_count:
		most_common_item = item

print("The item that appears the most in the list is " + most_common_item)
```

The code should find that the most common item is `hammer`


<details>
<summary>Solution</summary>
<div> 

```python
equipment = ["hammer", "ruler", "torch", "scissors", "screwdriver", "scissors", "torch", "hammer", "hammer", "ruler"]
most_common_item = ""
highest_count = 0

for item in equipment:
    count_of_item = equipment.count(item)
    if count_of_item > highest_count:
        most_common_item = item
        highest_count = count_of_item       # should add this line

print("The item that appears the most in the list is " + most_common_item)

```
</div>
</details>



## Exercise 5

Given this list of numbers between 0 and 100:


```
print("Useless processes should be removed")
idle_process_ids = [17, 18, 32, 6, 41, 8, 23, 88, 91]
```

Write some code that removes random numbers from this list until it only has 5 elements in it.

You should:

- Generate a random number using randint*
- Check if it exists inside of idle_process_ids
- If it does, remove it


Print the `idle_process_ids` list after your loop to make sure you did it right.

\* Add this line to the top of your code:


```
from random import randint
```

<details>
<summary>Solution</summary>
<div> 

```python
from random import randint

print("Useless processes should be removed")
idle_process_ids = [17, 18, 32, 6, 41, 8, 23, 88, 91]

while len(idle_process_ids) > 5:
    random_num = randint(0, 100)
    if random_num in idle_process_ids:
        idle_process_ids.remove(random_num)

print("The process list is now", idle_process_ids)
```
</div>
</details>


## Exercise 6

Add some code to the previous exercise that determines and outputs how many iterations the loop took to complete.

You'll have to create a counter variable and increment it in the loop.

<details>
<summary>Solution</summary>
<div> 

```python
from random import randint

print("Useless processes should be removed")
idle_process_ids = [17, 18, 32, 6, 41, 8, 23, 88, 91]

iterations_counter = 0

while len(idle_process_ids) > 5:
    iterations_counter += 1
    random_num = randint(0, 100)
    if random_num in idle_process_ids:
        idle_process_ids.remove(random_num)

print(f"it took {iterations_counter} iterations")
print("The process list is now", idle_process_ids)

```
</div>
</details>


## Exercise 7 

Given the following list of salaries:


```
salaries = [1200, 2500, 1800, 1600, 1800, 700, 3200, 1500, 1300, 1300, 850, 1900]
```

Write some code that does the following:

- Determine the average salary
- Create a new list of salaries that are above average
- Determine the average of the salaries that are above average
   - If you do this right, you should find the average to be 2,240


You may use code you've written previously, or do this from scratch for the challenge.

<details>
<summary>Solution</summary>
<div> 

```python
salaries = [1200, 2500, 1800, 1600, 1800, 700, 3200, 1500, 1300, 1300, 850, 1900]

average_salary = sum(salaries) / len(salaries)
print (average_salary)

above_average = [x for x in salaries if x > average_salary]   
print (above_average)

high_average = sum(above_average) // len(above_average)
print(high_average)
```
</div>
</details>


## Exercise 8

Given the following list of words:


```
lyrics = ["I", "am", "a", "rock,", "I", "am", "an", "island.", "I", "am", "also", "a", "couch,", "a", "mirror,", "and", "I", "am", "best", "known", "for", "being", "a", "letter", "of", "the", "alphabet.", "On", "some", "days,", "I", "am", "everything,", "on", "others", "I", "am", "nothing.", "I", "am", "both", "and", "I", "am", "neither.", "I", "am,", "whatever", "you", "say", "I", "am", "-", "if", "I", "wasn't,", "then", "why", "would", "I", "say", "I", "am?"]
```

Determine how many time the word "I" appears, **without** using the `count` operation. You can later use `count` to check your result.

Remember to think about how you would solve this as a human first:



1. Go through each word
2. If the word is I, keep track of it by increasing some counter variable
3. At the end of the loop, output the counter

<details>
<summary>Solution</summary>
<div> 

```python
lyrics = ["I", "am", "a", "rock,", "I", "am", "an", "island.", "I", "am", "also", "a", "couch,", "a", "mirror,", "and", "I", "am", "best", "known", "for", "being", "a", "letter", "of", "the", "alphabet.", "On", "some", "days,", "I", "am", "everything,", "on", "others", "I", "am", "nothing.", "I", "am", "both", "and", "I", "am", "neither.", "I", "am,", "whatever", "you", "say", "I", "am", "-", "if", "I", "wasn't,", "then", "why", "would", "I", "say", "I", "am?"]

counter = 0

for word in lyrics:
    if word == "I":
        counter += 1

print(counter)
```
</div>
</details>
