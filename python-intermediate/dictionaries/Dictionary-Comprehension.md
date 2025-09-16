We saw that we can create new lists with list comprehension, but you probably noticed that in Python we can do the same operation over different types.

Yes you guessed right!

We are going to create new dictionary using dictionary comprehension:
```
nums = [2,4,6]
numbers = { str(value): value for value in nums }
print(numbers)
```

Amazing!

Let's see another example that uses the 2 values of an enumerate:
```
names = ["koko", "momo", "bobo"]


result = {"name" + str(i): v for i,v in enumerate(names)}
print(result)
```

Of course that also here we can add a condition:
```python
names = ["koko", "mimi", "bobo", "fifi"]

{"n"+ str(i): names[i] for i in range(len(names)) if names[i][1] == "i"}


# {'n1': 'mimi', 'n3': 'fifi'}
```
Here we create a dictionary of the names that their second character is "i".