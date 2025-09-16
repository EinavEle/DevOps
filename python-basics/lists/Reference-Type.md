The way Python stores/manages memory is outside the scope of this lesson, but there is something important to understand about lists: they are **reference types**.

To understand what that means, here is an example:


```
numbers = [1, 2, 3]
nums = numbers

nums.append(4)

print(nums)
print(numbers)
```

When we say lists are **reference types**, we mean that any time we make a copy of a list (such as `nums = numbers`) - we're not really making a copy, we're actually just creating a `reference` to the original list.



Because of this, if you run the above code you will find that the number 4 was added to **both** `nums` and `numbers`, even though we only did `nums.append(4)` - that's because `nums` and `numbers` are the same - one is just a reference to the other.

<hr/>



One way to avoid this issue with lists is to use some special list syntax when making a copy, like this:


```
nums = numbers[:] 
```

What the above is doing is making an actual copy of each element in `numbers`, and adding it to `nums` - so now they won't be references of one another.



There is more to the idea of reference types, but it is outside the scope of this lesson.