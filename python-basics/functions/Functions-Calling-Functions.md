Though it might be a little tricky at first, we can invoke functions from within functions, and even use their return values as arguments for other function invocations - whew! That's a mouthful, let's see some code:


```
from random import randint

def get_random_name():
    names = ["Angela", "Nelly", "David", "Hubert", "Shira", "Michael"]
    return names[randint(0, len(names) - 1)]

def get_random_age():
    ages = [10, 24, 13, 14, 15, 26, 28, 22, 31]
    return ages[randint(0, len(ages) - 1)]

def generate_random_user():
    name = get_random_name()
    age = get_random_age()

    print(name + " is " + str(age) + " years old")

generate_random_user()
```

That's quite a bit of code so take a minute to read over it and see what you understand from it.

**Remember**: functions don't do anything until they are invoked.



### Breakdown

The first thing that happens in the code above is the `generate_random_user` invocation - even though it's the last line, it's the first operation that our code executes.



Invoking this function brings us into its body where we:

- invoke `get_random_name` and store whatever it returns inside of `name`, and
- invoke `get_random_age` and store whatever it returns inside of `age`


This is another nice thing about functions: we can often treat them as **black boxes** - that is, some input-output machine that gives us something. In other words, we don't really care how `get_random_name` or `get_random_age` work! All we care is that they `return` a string value that we store in `name`, and an int value that we store in `age`



We then use those two variables - `name` and `age` - and execute our final `print`, which outputs a sentence about our random user.



So in effect, this is what we care about from the code above:
```
def generate_random_user():
    name = get_random_name()
    age = get_random_age()

    print(name + " is " + str(age) + " years old")

generate_random_user()
```

The two invocations inside this function - `get_random_name()` and `get_random_age()` - could be our code, someone else's code; it doesn't matter so long as it returns what we expect it to.



That's nice.