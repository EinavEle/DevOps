The reason we use the term **dictionary** is because that is exactly how a dict works: we have a **key** that represents some **value**, just like in a dictionary:



- **Apple**: a red, round fruit filled with nutrients
- **Butterfly**: a winged insect that many consider beautiful


Where the key is on the left, and the value is on the right. In code, it looks like this:


```python
user = {
	"name": "Karolin",
	"username": "ksmart3",
	"age": 27,
	"has_purchased": False
}
```

The keys in the above object are `name`, `username`, `age`, and `has_purchased`, and each has its value after their respective colons.

In Python, when we write plain dicts like this, the key **is usually a string** unless your key is an integer. The value, however, depends on the type.


<hr/>


We can also use other variables as the values in our dicts, which looks like this:


```
favorite_city = "Edoras"
number_of_people = 4000

info = {
	"city": favorite_city,
	"population": number_of_people
}

# The above is exactly equivalent to:
info = {
	"city": "Edoras",
	"population": 4000
}
```

It may look silly, but there are certainly many cases where we receive data from other sources, and need to create dicts using that data.

<hr/>

Not only can we use variables for the values, we can also use them for the keys - though this is a little less common:


```python
student1 = "Vivian"
student2 = "Leeroy"
student3 = "Wayne"

student_statuses = {
    student1: True,
    student2: False,
    student3: False
}

print(student_statuses) 
# outputs: {'Vivian': True, 'Leeroy': False, 'Wayne': False}
```

There are good reasons to do this sometimes; we'll see an example eventually.

Notice that when we use a variable for the key, it is the key is the value of the variable, not the variable name (`student1`, etc.)


<hr/>

Final note about dict basics: they are **orderless**, that means that when we print this dict:


```python
user = {
	"name": "Karolin",
	"username": "ksmart3",
	"age": 27,
	"has_purchased": False
}
```

We might see
```python
{
  'username': 'ksmart3', 
  'age': 27, 
  'has_purchased': False, 
  'name': 'Karolin'
}
```
Or
```python
{
  'age': 27,  
  'username': 'ksmart3', 
  'name': 'Karolin', 
  'has_purchased': False 
}
```

It doesn't matter! These are key-value pairs; **they have no order**.