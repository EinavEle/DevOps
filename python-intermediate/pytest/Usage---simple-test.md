We will start with a simple test.


Pytest expects our tests to be located in **files** whose **names** begin with `test_` or end with `_test.py`.

Pytest will run only `functions` whose `name` begin with test.


Create a folder called tests in this folder create a file called `test_sum.py` and add the below code into it and save:
```python
def sum(num1, num2):
  return num1 + num2

def test_sum_with_zero():
  assert sum(0, 1) == 2, "Test failed! Wrong total when adding regular number with zero" 

def test_sum_regular():
  assert sum(1,2) == 3, "Test failed! Wrong total when adding two regular numbers" 
```

When running the test `test_sum_with_zero` , we are testing here that `sum(0, 1) == 2` using the key word **assert**.

If the test fails the error message will be: `"Test failed! Wrong total when adding regular number with zero"`


When running the test `test_sum_regular` , we are testing here that `sum(1, 2) == 3` using the key word **assert**.

If the test fails the error message will be: `"Test failed! Wrong total when adding two regular numbers"`


Run this code, using cmd navigate to the file path and write `pytest`
```console
pytest test_sum.py 
```

Let's look at it's output,

```output
test_sum.py F.                                                                                                   [100%]

====================================================== FAILURES =======================================================
_________________________________________________ test_sum_with_zero __________________________________________________

    def test_sum_with_zero():
>     assert sum(0, 1) == 2, "Test failed! Wrong total when adding regular number with zero"
E     AssertionError: Test failed! Wrong total when adding regular number with zero
E     assert 1 == 2
E      +  where 1 = sum(0, 1)

test_sum.py:5: AssertionError
=============================================== short test summary info ===============================================
FAILED test_sum.py::test_sum_with_zero - AssertionError: Test failed! Wrong total when adding regular number with zero
============================================= 1 failed, 1 passed in 0.03s =============================================
```

**In this output you can see:**


- One test failed and one test passed
```console
1 failed, 1 passed 
```

- The assertion error
```console
AssertionError: Test failed! Wrong total when adding regular number with zero 
```

- The failure reason:
```console
E     assert 1 == 2
E      +  where 1 = sum(0, 1)
```

- The line with the error
```console
test_sum.py:5: AssertionError 
```
