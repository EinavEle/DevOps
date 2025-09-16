Want to run the same test against multiple set of arguments? Pytest can give you that. All you have to do is to use `@pytest.mark`.parametrize.


Create a file called `test_parameterized.py` and add this code:
```python
@pytest.mark.parametrize("num1, num2, num3", [(1, 2, 3), (1, 2, 12)]) def test_sum(num1, num2, num3):   ﻿assert num1 + num2 == num3, "Got error in test_sum!" 
```

Run this command line:
```console
pytest test_parameterized.py 
```

The output will be:
```output
test_parameterized.py .F                                                                                                 [100%]
========================================================== FAILURES ===========================================================
______________________________________________________ test_sum[1-2-12] _______________________________________________________
num1 = 1, num2 = 2, num3 = 12
@pytest.mark.parametrize("num1, num2, num3", [(1, 2, 3), (1, 2, 12)])
      def test_sum(num1, num2, num3):
>       assert num1 + num2 == num3, "Got error in test_sum!"
E       AssertionError: Got error in test_sum!
E       assert (1 + 2) == 12   test_sum.py:5: AssertionError
================================================= 1 failed, 1 passed in 0.04s ================================================= 
```

The `test_sum` will be execute twice:
1. **First time** with num1 = 1, num2 = 2, num3 = 3 - and the assertion will pass.
2. **Second time** with num1 = 1, num2 = 2, num3 = 12 - and the assertion will fail.
