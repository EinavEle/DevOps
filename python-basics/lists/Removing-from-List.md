Python provides a straightforward operation to remove items from a list: remove

This operation will find the first occurrence of the item you're trying to remove, then remove it:


```python
devices = ["Computer", "Phone", "Tablet", "Phone", "Smartwatch", "Fitbit", "Smart Speaker"]

devices.remove("Fitbit") 
print(devices) 
# outputs: ["Computer", "Phone", "Tablet", "Phone", "Smartwatch", 'Smart Speaker']

devices.remove("Phone")
print(devices) 
# outputs: ["Computer", "Tablet", "Phone", "Smartwatch", "Smart Speaker"]
```

Notice that in the first case `remove` will get rid of the "Fitbit" and it's then gone from the list entirely.

However, since the second `remove` is getting rid of a "Phone", and there are two "Phones" in the list, we are still left with one after the operation.



<hr/>

One limitation to the `remove` command is that the item has to exist in the list for you to remove it, otherwise there will be an error.

To be safe, you can use the `in` keyword to first check if the item is in the list before you try to remove it:


```
devices = ["Computer", "Phone", "Tablet", "Phone", "Smartwatch", "Fitbit", "Smart Speaker"]

if "Deadly Laser" in devices:
  devices.remove("Deadly Laser")
```



If instead of removing by value you want to remove by index, you can use the `pop` command:


```python
devices = ["Computer", "Phone", "Tablet", "Phone", "Smartwatch", "Fitbit", "Smart Speaker"]

devices.pop(6)
print(devices) 
# outputs: ["Computer", "Phone", "Tablet", "Phone", "Smartwatch", 'Fitbit']
```

Similarly to the limitations of `remove`, you have to make sure the index exists before you access it.



Because we can use `len` to determine the length of the list, we could do something like this before using `pop`:


```
index_to_remove = 3
if index_to_remove < len(devices):
	devices.pop(index_to_remove)
```

This code will make sure we're never accessing an index that is outside the bounds of the list.