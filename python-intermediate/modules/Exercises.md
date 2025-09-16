
## Exercise 1

Import module `calendar`, and use its functions to write the following:
- Find whether `2010` is a leap year. And `2020`?
- Find how many leap years there will be between `2020 - 2080` (inclusive).
- Find which day of the week `March 14, 2028` will be.


## Exercise 2

You want precise control over the symbols that are exported from a module or package when a user uses the from module import * statement.

Assuming the following module:

```Python
# module1.py

def func1():
  pass


def func2():
  pass


num = 42  
```

Add some code so the statement `from module1 import *` (from any other module), only import `func1` and `func2`, without `num`.

**Hint:** Read about `__all__` or using `_` before variable name.


## Exercise 3


Assuming you have the following package `utils` :

      - utils   
        - module1.py   
        - math_utils     
          - f1.py     
          - f2.py     
          - f3.py   
        - string_utils     
          - s1.py     
          - s2.py 


Add the following imports using relative imports:

- If the module `utils.math_utils.f1` wants to import the module `f2` located in the same directory, which import statement should it include?
- If the module `module1` wants to import the module `s1` located in `string_utils` package, which import statement it should include?


## Exercise 4

You have a module that you would like to split into multiple files. A program module can be split into separate files by turning it into a package.

Consider the following simple module:
```Python
# my_module.py
class A:
  def foo(self):
    print('A.foo')

class B(A):
  def bar(self):
    print('B.bar') 
```
Suppose you want to split my_module.py into two files, one for each class definition. To do that, start by replacing the my_module.py file with a directory called my_module. In that directory create the relevant files so the following code will run without errors:
```
# main.py
import my_module
a = my_module.A()
a.foo()
b = my_module.B()
b.bar() 
```

**Note:** We didn't write:
```Python
from my_module.a import A
from my_module.b import B 
```

<details>
  <summary>
     Hint 1
  </summary>
    The directory will contain the following files: <code>__init__.py</code>, <code>a.py</code> (for class A), and <code>b.py</code> (for class B).
</details>

<details>
  <summary>
     Hint 2
  </summary>
    Use <code>__init__.py</code> file (read again the init file activity if needed).
</details>

