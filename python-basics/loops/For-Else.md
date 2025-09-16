
Let's look at the following scenario. We have a list of names:
```
names = ["koko", "bobo", "gogo"]
```
And we want to check if a certain name exist in the list.
How should we do it?



With a for loop of course!

Let's say we want to check if `bobo` exist in the list, and print "found" if it is.

We could write something like this:
```
names = ["koko", "bobo", "gogo"]
for name in names:
    if name == student_name:
        print("found")
        break
```

The break is here so that once we found `bobo` we would stop the iteration.

But what happens if we try to look for `momo` in the list and we don't find it.

In this case we would want to print `not found`



How can we do that?



take a minute and try to do that.



After the for loop ends we need to know if we found the name or not.

We could use a flag to do that:
```
student_name = "momo"
names = ["koko", "bobo", "gogo"]
user_found = False

for name in names:
    if name == student_name:
        print("found")
        user_found = Truebreak
if not user_found:
    print("not found")
```

That works fine.

But python has a better way.



We can use the `else` keyword to make sure no breaks were encountered.

It would look like this:
```
student_name = "momo"
names = ["koko", "bobo", "gogo"]

for name in names:
    if name == student_name:
        print("found")
        break
else:
    print("not found")
```

Amazing no?

No need for the flag!!



We can also use the `else` clause with a while loop:
```
sum = 15
while sum < 30:
    sum += 4
    ﻿if sum % 8 == 0:
        break
else:
    print("got to 30")
```
If the while loop finished with no breaks, then the else part will be executed.