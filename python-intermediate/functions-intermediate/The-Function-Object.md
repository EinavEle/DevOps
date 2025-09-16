Functions are Objects.

They have attributes and methods, and they can be assigned to variables.


Here is a function:
```python
def hello(name = "Margo"):
  """this is a greeting function"""
  print(f'Hello {name.capitalize()}!') 
```

Let's examine some cool properties:
```python
print("Documentation: ", hello.__doc__)
print("Name: ", hello.__name__)
print("Code at: ", hello.__code__)
print("defaults : ", hello.__defaults__) 
```

Through the function object we can access some meta data, such as the documentation of the function(__doc__), the name of the function (__name__) and the default arguments (__defaults__).


Alright. Cool.

Let's continue.
