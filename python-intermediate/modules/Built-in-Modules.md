In most languages you can use common functions out of the box.

For example: `print`

```python
print("Don't need to do anything.") 
```

Another common use case is standard mathematical operations, `sqrt`, `power`...

Some of these were available to us as built-in functions:

For example: `abs` (absolute value):
```python
abs(-1) # 1 
```

The `abs` function is built-in, so we don't need to do anything if we want to use it, it comes with the Python interpreter.

Other mathematical operations are also available, but in a slightly different way.

They are grouped together as a module called math.


### What is a module?
 **A module is any `*.py` file. The name of the file is the name of the module.**

`math` is a special module, a built-in module, meaning it is compiled into the Python interpreter, and therefore does not have a *.py file.

Python comes with many ready made modules we can use.

If we want to find the factorial sum of a number, we want to write something like:
```python
factorial(5) 
```

But Python doesn’t have access to the factorial function yet.

First we need to import the relevant module:
```python
import math


math.factorial(5) 
```

Behind the scene Python runs all of the code in the module file.

All of the objects and functions that are defined in the module are made available.

Note that now we can use any function in the math module:
```python
import math


math.ceil(1.2)
math.sqrt(25) 
```

If we want to use only one function we can use this syntax:
```python
from math import sqrt


sqrt(25) 
```

Now we don’t have to write `math.sqrt(25)`

We can import several functions at the same time:
```python
from math import sqrt, factorial, isqrt 
```

We can also use an alias for an imported function, to give it a different name:
```python
from math import factorial as fact


fact(6) 
```

In general the syntax is:
```console
from <module> import <function> as <alias> 
```

If we want to import all the functions in a module we can use the `*`:
```python
from math import * 
```

Of course it is not very efficient, so don't use it if you don't have a good reason :)
