When we have piece of code that can throw any of several different exceptions that can be grouped together we can handle all using single except block of code using tuple:

```Python
while True:
  try:
    y = int(input('Please enter a number\n'))
    print(y)
  except (ValueError, TypeError) as e:
    print(f'Error is {e}') 
```

In case one of the exceptions has to be handled differently, we can and should put it into its own except clause:
```Python
def raising_exceptions_for_fun(num):
  if num == 1:
    raise StopIteration(f"Just because I can {num}")
  elif num == 2:
    raise KeyboardInterrupt(f"Just because I can {num}")
  elif num == 3:
    raise OSError(f"Just because I can {num}")
  else: # We do not have to provide a string
    raise FileNotFoundError
  
for i in range(4):
  try:
    raising_exceptions_for_fun(i)
  except StopIteration as exp:
    print("Got", exp)
  except KeyboardInterrupt as exp:
    print("Got", exp)
  except OSError as exp:
    print("Got", exp)
  except FileNotFoundError as exp:
    print("Got", exp)
```

In the console:
```console
Got 
Got Just because I can 1
Got Just because I can 2
Got Just because I can 3 
```

### Order matters
```Python
try:
  int(input("Please enter a number, and nothing but a number: "))
except Exception:
  print("Something is wrong, cannot tell exactly what...")
except ValueError:
  print("Bad choice, I said only numbers!") 
```

In the console
```console
Please enter a number, and nothing but a number: shoobert
Something is wrong, cannot tell exactly what...
```