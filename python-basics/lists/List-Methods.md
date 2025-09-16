We can do many great things with lists.

Let's look at some important methods that can help us.



### index

returns the index of the first appearance of the element:
```
nums = [1,3,4,3]
index = nums.index(3)
print(index)
```



### sort

sort the list in-place, meaning mutating the list in an ascending order.
```
nums = [11,3,42,3]
nums.sort()
print(nums)
```

in order to sort it in a descending order, add optional `reverse` parameter:
```
nums = [11,3,42,3]
nums.sort(reverse=True)
print(nums)
```

### count

counts the number of element appearances
```
nums = [11,3,42,3,3]
num_of_appearances = nums.count(3)
print(num_of_appearances)
```

### reverse

We can reverse the order of the items:
```
nums = [1,2,3]
nums.reverse()
print(nums)
```