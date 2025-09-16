As many people are going to read the code that we write, it is important that the code that we write is **clear and readable**.

For that we include a few style guides that you should follow, so that your code is clean and tidy 😀



## Spacing


Use spacing when using operators:


**Do**
```
z = x + y if x > 5
```

**Don't Do**
```
z=x+y
if x>5 
```


## Indentation


When creating a dictionary use tab indentation for each level.


**Do**
```
person = {
  "name": "Mimi",
  "age": 39,
  "friend": {
    "name": "Titi",
    "age": 42
  }
} 
```

**Don't Do**
```
person = { "name": "Mimi", "age": 39, "friend": { "name": "Titi", "age": 42 } }﻿ 
```


## Spaces between code lines


We want to also have spaces between different parts of the code.

Keep in mind these 2 rules:


- **Two blank lines** between ***the import statements and other code***.
- **Two blank lines** between ***each function***.



**Do**
```
import math
import statistics


def foo1():
  print("hello")


def foo2():
  print("hello2") 
```

**Don't Do**
```
import math
import statistics
def foo1():
  print("hello")
def foo2():
  print("hello2") 
```

---

**For more python guidelines see [pep8](https://www.python.org/dev/peps/pep-0008/)**
