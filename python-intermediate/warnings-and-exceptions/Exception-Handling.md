# Exceptions

Whenever the interpreter encounters an error of any kind, an exception is raised.

Unlike other programming languages such C++, in which exceptions are used to signal special situations which essentially are not errors, exceptions in Python are used to signal any kind of error, including syntax error, bad values and so on. These exceptions reflect a natural path of the program in Python.


When raised, exceptions break the direct program flow and are transferred downstream the stack until being handled. In case they are not catches (or re-thrown), the program will be terminated.

Exceptions provide a very easy and elegant way to separate between the "good path" and the "bad path" of a program; They overcome the messy logic often caused by using many return values; Since Python is interpreted "on-the-fly", exceptions become the major and sometimes the only tool to reflect language-based mistakes, which couldn't be noticed in advance, unlike pre-compiled languages.


There is a wide range of built-in exceptions which can be categorized in groups of subjects. All of them inherit from Exception base class.

The basic syntax for exception handling is the keyword try, except and raise:

```python
# 'raise' throws the specified exception:
raise ValueError("It is a common hobby to terminate Python programs!") 
```

```console
Traceback (most recent call last):
File "/Users/shiranusboim/PycharmProjects/untitled/warning.py", line 2, in <module>
raise ValueError("It is a common hobby to terminate Python programs!") ValueError: It is a common hobby to terminate Python programs! 
```


Since the raise above is not a part of any try and except code block, the exception is not caught, leading to termination. In case we don't want to terminate our program but to catch the error and handle it, that way or another, we will use try-except block:

```python
try:
  raise ValueError("It is a common hobby to terminate Python programs!")
except ValueError:
  print("Caught you!") print("Caught you!") 
```

**The output will be:**
Caught you! Caught you! 

Can you explain why "Caught you!" is being printed twice?
<details>
<summary>Click here to see the answer</summary>

The first print comes from the except scope and the second print comes from the print("Caught you!") since in the except block we just print a message and then the program keeps on running.

</details>

---


We are catching the exception as an event without handling the thrown object itself, which can provide us more information. We could write:

```python
try:
  raise ValueError("It is a common hobby to terminate Python programs!")
except ValueError as exp:
  print("Caught ValueError exception: ", exp.args) 
```

and we get
```console
Caught ValueError exception:
('It is a common hobby to terminate Python programs!',)
```

We could catch the exception in a more generic way, not by aiming specifically to ValueError, but aiming to more general cases:

```python
try:
  raise ValueError("It is a common hobby to terminate Python programs!")
except Exception as exp:
  print("Caught any type of exception object: ", exp.args) 
```

In the console we should see:
```console
Caught any type of exception object:
('It is a common hobby to terminate Python programs!',) 
```

We could do even:
```python
try:
  raise 4 except:
    print("Caught any kind of Python object, not necessarily an exception object")  
```

In the console:
```console
Caught any kind of Python object, not necessarily an exception object 
```

Catching just any kind of exception (or even worse: any kind of object) is considered to be a very bad idea, because we handle our program in a very irresponsible and inaccurate manner. It can lead us to catch exceptions that were not aimed to us. In case an exception was raised and we do not know (or should not know) how to handle it, we should leave it for others. Other parts of the program are designed, and therefore are responsible, to handle it.
