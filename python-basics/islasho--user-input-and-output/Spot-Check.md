Write a "Guess my Number" game.

Choose a random number from 1-10.

Ask the user to guess your number.

If he was write print him a win message and finish the execution.

Else let the user know if your number is smaller or bigger.

Continue the game until the user guesses your number.



It should look something like this:
```
Guess what my number is!
3
Not yet. My number is smaller than 3. Try again
Guess what my number is!
1
Not yet. My number is Bigger than 1. Try again
Guess what my number is!
2
You got it!
```

Here is a solution to check.
<details>
<summary>Solution</summary>
<div> 

```python
from random import randint

random_number = randint(1, 10)

while True:
    input_number = int(input("Guess what my number is!\n"))
    if random_number == input_number:
        print("You got it!")
        break
    elif random_number < input_number:
        print(f"Not yet. My number is smaller than {input_number}. Try again")
    else:
        print(f"Not yet. My number is bigger than {input_number}. Try again")
```
</div>
</details>
