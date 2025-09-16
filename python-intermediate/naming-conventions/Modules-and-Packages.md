Module names should be all lower case. Underscores are allowed to improve readability.


```
products.py
math_utils.py
```
 


**You are not allowed to use:**
- dot
- dash
- Capital letters
- cannot start with a number


Not allowed:

    math.utils.py # dot
    math-utils.py # dash
    Users.py # capital letter
    2users.py # start with a digit 

Packages should also have short, all-lowercase names, although **the use of underscores is discouraged.**



### Bad Practice

A general note about programming.

It is a bad practice to use spaces in file names and folders. This might cause problems in the future, when trying to run the files or using the path of the file.



```
my file.py
my folder/file.py 
```


Make sure to avoid spaces when creating files and folders.



### Modules that contain a class

In the case of your file containing only a class you


```
class Manager:
  pass
```


The file that contains this code is still a module and should still be named `manager.py`, all lowercase.
