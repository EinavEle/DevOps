**A Closure is an inner function that has access to variables in the outer (enclosing) functions even after the outer function finish its execution.**


So when we talk about closures we're just talking about regular functions that are nested inside some outer function. What makes them special is their persistent access to variables from the outer function, even when that function has finished executing.


When a function is finished executing, usually the local variables that were declared in it are no longer available. However, if those variables are being accessed outside the function's scope somewhere else, they will stay around. This is closure. Let's look at an example:

```python
def foo():
  x = 1
  
  def inner():
    print(x)    # notice this inner function using the outer function's variable
  
  return inner

baz = foo()     #out here, x doesn't exist
baz()           #but when we invoke baz, we're printing x! 
```

Run this code, then try to `print(x)` - it's not defined, but baz is using it! Here's what's going on:


The python interpreter get's into action:

- It starts by setting the variable `baz` to the result of calling the function foo
- The function foo gets called, initializing the variable `x` and the function inner (in its scope)
- Finally, `foo` returns the function `inner` back to baz


Now `baz` is referencing the function `inner` 

When `baz` (inner) gets invoked, since it uses the variable `x`, `foo`'s scope sticks around even though normally it would disappear. 

The number `1` is logged. Closure observed.


Let's look at another example.

```python
def setCounter(step):
  counter = 0
  def count():
    nonlocal counter
    counter += step
    print(counter)
  return count

increment = setCounter(2)
increment() 
```

2 will be printed, that makes sense. Try to invoke the `increment()` function again. This time 4 is printed. The `counter` variable has been remembered via the closure.


Now, try to print `counter` in the global scope:
```python
def setCounter(step):
  counter = 0
  
  def count():
    nonlocal counter
    counter += step
    print(counter)
  
  return count
  
print(counter) 
```

What happens?

Again, you get an error because `counter` is only available inside the `setCounter` scope **except** through our closure.
