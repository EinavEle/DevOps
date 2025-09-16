For the most part, a `while` loop is used when solving problems related to optimization or finding maximum/minimum values.

These types of problems are outside the scope of this lesson, so we will see how we can use a `while` loop to solve other problems that could also be solved with regular loops.



Say we have a list of people:

```
people = ["Holly", "Irene", "Jessica", "Kyle", "Mike", "Nadine", "Olly"]
```

And our goal is to find the index of one of the people. We could use a while loop like this:

```
person_of_interest = "Jessica"
index = 0
found = False

while not found:
	if people[index] == person_of_interest:
		found = True
	else:
		index = index + 1

print(person_of_interest + "'s index in the list is: " + str(index))
```

The code is fairly straightforward: so long as we haven't found the person (which we test with the `found` variable), keep looping.

In the loop, either:

- Set found to True once we have the right index, or
- Increase the value of index by 1, so that on the next iteration we look at the next person in the list


<hr/>

**Be Warned!** `while` loops are susceptible to a problem known as **infinite loops** - if the condition in the `while` is not met, the loop will continue to run forever and potentially freeze/crash your app and computer.