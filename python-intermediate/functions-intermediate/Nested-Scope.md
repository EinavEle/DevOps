We can define an inner function inside a given function:
```python
def outer_func():
  print("in outer_func")
  
  def inner_func():
    print("in outer_func")
  
  inner_func()


outer_func() 
```

What happens if we use the same names within the functions?

```python
def outer_func():
  local_var = 11
  
  def inner_func():
    local_var = 21
    print("inner_func local_var = ", local_var) ​
  
  inner_func()
  print("outer_func local_var = ", local_var)


outer_func() 
```


In that case, each function has its own version of local_var. If we would remove `local_var = 21`  in `inner_func`, the value will be 11:

```python
def outer_func():
  local_var = 11
  
  def inner_func():
    print("inner_func local_var = ", local_var)​
  
  inner_func()
  print("outer_func local_var = ", local_var)

outer_func() 
```

If we want the inner_func to change the local_var in the outer_func we must use a special keyword `nonlocal`.

local_var variable is considered nonlocal, **as it is not completely local, and it is not global either**.

```python
def outer_func():
  local_var = 11
  def inner_func():
    nonlocal local_var
    local_var = 21
    print("inner_func local_var = ", local_var)
  inner_func()
  print("outer_func local_var = ", local_var)

outer_func() 
```

Now we will get 21 twice.


We can still use `global` keyword in nested function:

```python
global_var = 10

def outer_func():
  local_var = 11
  def inner_func():
    global global_var
    global_var = 21
    print("inner_func global_var = ", global_var) ​
  inner_func()
  print("outer_func global_var = ", global_var)

outer_func()
print('outside global_var = ', global_var) 
```
In this case we will update the global variable.
