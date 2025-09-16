A simple way to delete a property from a dictionary is with pop:
```
student = {
    "name": "koko",
    "age": 42,
    "level": "A"
}

deleted = student.pop("level")
print(deleted)
```

If we try to delete a property with a key that does not exists we will get a `KeyError`:
```
student = {
    "name": "koko",
    "age": 42
}


deleted = student.pop("hobies")
# Throws Error
```

Another way to delete a property is with del:
```
student = {
    "name": "koko",
    "age": 42,
    "level": "A"
}


del student["level"]
```