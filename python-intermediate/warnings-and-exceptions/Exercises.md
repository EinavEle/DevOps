## Exercise 1
### Instructions:

Find all the possible errors in this code:

```Python
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))
quotient = dividend/divisor
print(math.floor(quotient)) 
```

Hint: there are at least three possible errors.


## Exercise 2
### Instructions:

Add a try-except statement to the body of this function which handles a possible IndexError and print an error message accordingly:

```Python
def get_list_element(my_list, index):
  print(my_list[index]) 
```

## Exercise 3
### Instructions:

Think about the specific possible error in the code above and add a try-except statement to the body of this function. Print an error message accordingly

```Python
age = int(input("How old are you? ")) 
```

## Exercise 4
### Instructions:

Given this code:

```Python
def divide(x, y):
  print(f'{x}/{y} is {x / y}')    
```

Add three possible errors in three different except blocks and three different error messages.
Rewrite the three possible errors in one except line.



Solution:

```Python
def divide(x, y):
  try:
    print(f'{x}/{y} is {x / y}')
  except ZeroDivisionError as e:
    print(e)
  except TypeError as e:
    print(e)
  except ValueError as e:
    print(e) 
```



