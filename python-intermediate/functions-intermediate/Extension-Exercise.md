

## Splice Challenge

Implement the Javascript array splice method *(Don't worry you don't need to know javascript :) )*

You can read about it here: [splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

Try to be precise and thorough, read all the small details, and implement all functionalities.


You can use the following code template:
```python
def splice():
  # write your code here    
```


1. Define parameters for the functions (make sure it corresponds with the tests)

2. Note that you need to pass the list as a parameter too!

3. Use basic features. You are not allowed to use any packages or special features.

4. **Bonus:** *Do not use slice.*


Make sure the tests pass!!


Tests:

```python
# remove 1 element
nums = [1, 2, 3]
nums, deleted = splice(nums, 0, 1);
assert nums == [2, 3]

# add 1 element
nums = [1, 2, 3]
nums, deleted = splice(nums, 0, 0, 0);
assert nums == [0, 1, 2, 3]

# add 2 elements
nums = [1, 2, 3]
nums, deleted = splice(nums, 0, 0, -1, 0);
assert nums == [-1, 0, 1, 2, 3]

# replace 1 element
nums = [1, 2, 3]
nums, deleted = splice(nums, 1, 1, 55);
assert nums == [1, 55, 3]

# delete all elements from index to end
nums = [1, 2, 3, 4, 5]
nums, deleted = splice(nums, 1);
assert nums == [1]

# returns list of deleted elements as the second parameter
nums = [1, 2, 3]
nums, deleted = splice(nums, 1);
assert deleted == [2, 3]

# returns an list of the deleted element (1 element)
nums = [1, 2, 3]
nums, deleted = splice(nums,1, 1);
assert deleted == [2]

# returns an empty list when no elements are deleted
nums = [1, 2, 3]
nums, deleted = splice(nums,1, 0, 5);
assert deleted == []

# delete all but 2 last ones
nums = [1, 2, 3, 4]
nums, deleted = splice(nums, -2);
assert deleted == [3, 4] 
```

**Good Luck!**


