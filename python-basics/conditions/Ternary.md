We already saw how to handle conditions with if else:

```
import random

num = random.randint(1, 100)

if num > 80:
    print("num > 80")
else:
    print("num <= 80")
```

The ternary is another way, a different syntax to write the same condition in a single line:

```
print("num > 80") if num > 80 else print("num <= 80")
```

Usually will will use the ternary to store a value based on a condition, and then use it.

So a cleaner way to write the same thing is:
```
message = "num > 80" if num > 80 else "num <= 80"
print(message)
```