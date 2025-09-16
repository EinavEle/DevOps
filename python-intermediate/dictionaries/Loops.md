By default, if we run a for loop over a dictionary:
```
person = {
    "name": "koko",
    "age": 17,
    "is vegan": True
}


for key in person:
    print(key)
```
then Python will iterate over the dictionary **keys**:

meaning it will print:

- name
- age
- is vegan



You can also use the function keys() to get a list of the keys in the dictionary:
```
person.keys()
```



Of course it is not the only option.

We can also iterate the values of the dictionary using the dictionary values() method:
```
for value in person.values():
    print(value)
```

and we will get:

```shell
koko
17
True
```


If we need both keys and values we can use the `items()` method that returns a key, value pair:
```
for key,value in person.items():
    print(key, value)
```
We will get:


```bash
name koko
age 17
is vegan True
```