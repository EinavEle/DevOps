## Exercise 1

Given the following list:


```
songs = ["My Heart", "Her Brain", "The Light", "A Shadow", "One Dance", "Two Monkeys", "Happy Jumping"]
```

Create a `playlist` list by doing the following:



1. Add the first, third, and fifth songs ("My Heart", "The Light", "One Dance") from `songs`
2. Update "One Dance" inside of `playlist` to now be "One Dance - Together"
3. Remove the second song from `playlist`


When you're done, your `playlist` should look like this: `["My Heart", "One Dance - Together"]`

<details>
<summary>Solution</summary>
<div> 

```python
songs = ["My Heart", "Her Brain", "The Light", "A Shadow", "One Dance", "Two Monkeys", "Happy Jumping"]

playlist = list()

playlist.append(songs[0])
playlist.append(songs[2])
playlist.append(songs[4])

playlist[2] += " - Together"

playlist.pop(1)

print(playlist)
```
</div>
</details>




## Exercise 2

Given the following list:


```
print("Don't try to memorize this")

pi_digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7]
```

Write code that determines:

1. How many numbers are in `pi_digits`

You should find it to be 100
2. How many times does the number 6 appear in pi_digits

<details>
<summary>Hint</summary>
<div> 
use the count command for this; the syntax is similar to pop
</div>
</details>
<br/>

You should find it to be 9

3. What is the sum of all the numbers in pi_digits
<details>
<summary>Hint</summary>
<div> 
use the sum command for this; the syntax is similar to len
</div>
</details>
<br/>

You should find it to be 471


<details>
<summary>Solution</summary>
<div> 

```python
print("Don't try to memorize this")

pi_digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7]

print(len(pi_digits))
print(pi_digits.count(6))
print(sum(pi_digits))
```
</div>
</details>


## Exercise 3

Given the following list:


```
turtle_status = ["sick", "healthy", "healthy", "healthy", "sick", "sick", "healthy", "sick", "healthy", "healthy", "healthy", "healthy", "healthy", "sick"]
```

Write some code that does the following:



1. Determine how many sick turtles and how many healthy turtles there are
2. If there are more sick than healthy turtles, print "We have a shell of a problem"
   1. Otherwise, print "Let's shell-ebrate"

<details>
<summary>Solution</summary>
<div> 

```python
turtle_status = ["sick", "healthy", "healthy", "healthy", "sick", "sick",
                 "healthy", "sick", "healthy", "healthy", "healthy", "healthy", "healthy", "sick"]


sick_turtles = turtle_status.count("sick")
healthy_turtles = turtle_status.count("healthy")
if sick_turtles > healthy_turtles:
    print("We have a shell of a problem")
else:
    print("Let's shell-ebrate")
```
</div>
</details>



## Exercise 4

Create a list called `nums` and add some numbers (integers) to it.



- Define a variable called `num_to_remove` - give it any numeric value you like
- Remove the second occurrence of the number from `nums` **if** it exists in the list and it appears at least twice in the list

<details>
<summary>Solution</summary>
<div> 

```python
nums = [1, 9, 3, 2, 9, 10, 9, 5]

num_to_remove = 9

if nums.count(num_to_remove) > 2:
    first_occurence = nums.index(num_to_remove)
    second_occurence = nums.index(num_to_remove, first_occurence + 1)
    nums.pop(second_occurence)

print(nums)
```
</div>
</details>
