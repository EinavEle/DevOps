We know that we can check the equality of 2 variables like this:

```python
a = [1,2]
b = [1,2]
print(a == b) # True 
```

But there is an additional check that we can perform to check if 2 references point to the same object.

`is` verifies if the identity of 2 **references** is the same.

```python
a = [1,2]
b = [1,2]
print(a == b) # True
print(a is b) # False 
```

Now, let's see what is the behaviour for `mutable` and `immutable` types.


We saw that when we create 2 lists with the same values they have different ids. This is the behaviour for all mutable types.

Since strings are immutable, when we will create 2 items with the same values both of these variables will have the same id.
```python
s1 = "Kush"
s2 = "Kush"
print(s1 == s2)           # True
print(s1 is s2)           # True
print(id(s1), id(s2))     # same numbers
```

Not the same with lists!

```python
l1 = [1, 2] 
l2 = [1, 2] 
print(l1 == l2)           # True
print(l1 is l2)           # False
print(id(l1), id(l2))     # different numbers
```
