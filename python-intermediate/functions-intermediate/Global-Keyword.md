Variables that are declared in the global scope of the module (i.e. outside inner definitions like functions and classes) are called global variables.

Variables with the same name inside such inner definitions will hide the global ones by default:

```python
g = 'I am global'

def func():
  g = 'I am local'
  print('func: ', g)

func()
print('outside: ', g) 
```

If `global` is specified, func will affect the global g:

**If we want to update a global variable from within a function we will have to specify the `global` keyword**:

```python
g = 'I am global'

def func():
  global g
  g = 'overrideing global'
  print('func: ', g)

func()
print('outside: ', g) 
```
