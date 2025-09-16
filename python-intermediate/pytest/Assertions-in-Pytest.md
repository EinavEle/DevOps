Pytest allows us to use the standard python assert for verifying exceptions in two ways:

A. **With** assertion error message.

B. **Without** an assertion error message.

## A. With assertion error message
```python
def get_name():
  return "shoobert"

def test_get_name():
  assert get_name() == "Shoobert", "oops, i got a wrong name" 
```

Navigate to tests folder and run that command in the terminal:
```console
pytest my_test.py 
```

Output:                                                       
```output
my_test.py F                                                                                                            [100%]
========================================================== FAILURES ===========================================================
________________________________________________________ test_get_name ________________________________________________________
    def test_get_name():
>      assert get_name() == "Shoobert", "oops, i got a wrong name"
E      AssertionError: oops, i got a wrong name E       assert 'shoobert' == 'Shoobert'
E         - shoobert
E         ? ^
E         + Shoobert
E         ? ^  my_test.py:6: AssertionError
====================================================== 1 failed in 0.03s ====================================================== 
```

`my_test.py F`  means that there is one **failure** in `my_test.py` file, we can also see the test took **0.03s**.

## B. Without an assertion error message:
```python
def get_name():
  return "shoobert"

def test_get_name():
  assert get_name() == "Shoobert" 
```
Try it yourself. Can you see what has changed in the output?


In case of success:
```
def get_name():
  return "Shoobert"

def test_get_name():
  assert get_name() == "Shoobert" 
```

Run that command in the terminal:
```console
pytest my_test.py 
```

Output:
```output
my_test.py .                                                                                                            [100%]
====================================================== 1 passed in 0.01s ======================================================
```

dot `.` means **pass**, `my_test.py .` means that there is one **success** in `my_test.py` file, we can also see the test took **0.01s**.


Adding flag `-v` will displayed the specific test that has failed/passed. Run this command in the terminal:
```Configurations
pytest -v my_test.py 
```

The output will be:
```output
my_test.py::test_get_name PASSED                                         [100%]
============================== 1 passed in 0.01s =============================== 
```

Can you think what happen when some of the tests failed and some success?


Let's write this code in my_test.py:
```python
def get_name():
  return "Shoobert"

def test_get_name1():
  assert get_name() == "Shoobert"

def test_get_name2():
  assert get_name() == "shoobert" 
```

Run this command line:
```console
pytest -v my_test.py 
```

Now the output look like this:
```output
my_test.py::test_get_name1 PASSED                                                                                       [ 50%]
my_test.py::test_get_name2 FAILED                                                                                       [100%]
========================================================== FAILURES ===========================================================
_______________________________________________________ test_get_name2 ________________________________________________________
    def test_get_name2():
>     assert get_name() == "shoobert"
E     AssertionError: assert 'Shoobert' == 'shoobert'
E       - Shoobert
E       ? ^
E       + shoobert
E       ? ^  my_test.py:8: AssertionError
================================================= 1 failed, 1 passed in 0.03s ================================================ 
```

This is nice. Really nice.


Assertion examples:
```console
assert True # successful assertion
assert False # assertion failure 
```
