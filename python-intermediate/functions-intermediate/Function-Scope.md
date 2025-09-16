Although there can be various unique namespaces defined, we may not be able to access them all from every code section of the program.

What limits this access is what call a scope: The portion of the program code from where a namespace can be accessed directly without any prefix.


At any given moment, there are at least the following three nested scopes:

1. Scope of the current function which has local names
2. Scope of the module which has global names
3. Outermost scope which has built-in names


When reaching a certain name, the interpreter looks for this name in the local namespace, then in the global namespace and finally in the built-in namespace.

```python
global_var = 5

def foo():
  local_var = 8 
```

If we were to define 2 variables with the same name in 2 different scopes:
```python
name = "global"

def foo():
  name = "local"
  print(name)

foo()
```


What will be printed?

When we invoke foo the interpreter will reach the printing statement: `print(name)`

It will start by looking for name in the function scope, since we have a variable name = "local" in the function scope it will print local.


What about now:
```python
name = "global"

def foo():
  print(name)

foo() 
```

Again the interpreter will reach the printing statement: `print(name)`

It will look for a name variable in the function scope, and since there is none, it will look for a name variable in the global scope. There we have a `name = "global"` so it will print global.


