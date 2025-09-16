A function always return something, but did you know that it can return more than one value?



In most languages if you want a functions to return a location with `x, y` values you will have to return an object of some kind.

Like this:


```python
def go_right(x,y):    
  return {       
    "x": x + 1,        
    "y": y    
  } 
```


But in Python a function can just return 2 values.

Let's see:
```python
def go_right(x, y):    
  return x + 1, y   


new_location = go_right(2,2) # 3, 2  
```
What does it mean to return 2 values?

Actually new_location is a tuple `(3,2)`.

So:
```python
print(type(go_right(2,2))) # <class 'tuple'> 
```

Now it is clear.

If we want to access the `x` value we could just do:
```python
new_location = go_right(2,2) 
print(new_location[0])  
```

But that is not so pretty ha?



You are absolutely right!



Luckily, Python has a **multiple assignment** ability.





## Multiple assignment
```python
m, n = 7, 10 ​ 
print(m) 
print(n)
``` 
We can assign 2 values in 1 line.

More specifically, we can break down a tuple into single values and assign them into different variables.



When combined with Python's ability to return multiple values, we get this wonderful behaviour:
```python
def go_right(x,y):     
  return x + 1, y   


x, y = go_right(2,2) 
```