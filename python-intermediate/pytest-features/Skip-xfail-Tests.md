## Skip



There can be some situation in which we don't want to execute one test or more. In those situation we can use skip as marker.


Adding `@pytest.mark.skip` to the test means that Pytest will **skip** it and the test will not be executed.


Create new file called `test_skip_xfail.py` and add this code to it:
```python
import pytest

@pytest.mark.skip
def test_sum1():
  assert 1 + 2 == 3

def test_sum2():
  assert 1 + 2 == 4 
```

Run this line in the terminal:
```console
pytest test_skip_xfail.py  
```

The output will be:
```output
test_sum.py sF  
```

Explain that output. 

<details>
<summary>Click here to see the answer ... </summary>
The output means that one test has been skipped (s) and one test failed (F)
</details>


## xfail


In case we want a test to be executed but not to be count as part of the failed or passed tests we can use `xfail` marker by adding `@pytest.mark.xfail`.


Add this code to test_skip_xfail.py file:
```python
@pytest.mark.xfail
def test_sum3():
  assert 10 + 20 == 31 
```

In the terminal run:
```
pytest test_skip_xfail.py  
```

Output:
```output
test_sum.py sFx  
```
Can you explain that output?

<details>
<summary>Click here to see the answer ... </summary>
The output means that one test has been skipped (s), one test has been failed (F), and one test was xfail(x).
</details>