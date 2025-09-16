To add an item to a list, we can use the append command. This command will add the item to the end of the list:


```
modern_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
modern_billionaires.append("You")

print(modern_billionaires) 
```

Executing the above code will output 
```
["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett", "You"]
```


Of course, now the value of "You" will have its own index: 4



Another option is using the insert method.

The insert(index, value) method will insert a value in a specific index, meaning that unlike append we can insert at any place, while append only inserts at the end of the list.

```
nums = [1,3,4]
nums.insert(1, 2)
print(nums)
# [1,2,3,4]
```

`insert` will expand the list size and add an element in place of index 1, pushing the rest of the elements one place forwards.