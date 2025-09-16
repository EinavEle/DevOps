In our code there are times when we need to work on data that should be set before the tests start. Most of the times there will be more than one test that will need that setup, what will lead to duplicate code and this is... well, this is bad. So, instead of repeating the same code in every test Pytest gives us Fixtures.


Lets look at the following code:
```python
def did_student_fail(student):
  return any(grade < 60 for grade in student["grades"])

def get_passing_grades(student):
  return list(filter(lambda x: x >= 60, student["grades"])) 
```

We have here 2 functions that are expecting a dictionary parameter with a grades list attribute.
So we need a student object for both of these tests.
This is where the fixture comes in handy.


Let's define a student with grades as a fixture:
```python
@pytest.fixture
def student():
  return {
    "name": "Shushu",
    "grades": [70, 33, 93, 47]
  } 
```

Fixtures are in fact functions. We mark those function as fixtures using pytest decorator:
```python
@pytest.fixture 
```


Now let's write some tests:
```python
def test_student_failed():
  assert did_student_fail(student), "Student did not fail"

def test_student_pass():
  assert len(get_passing_grades(student)) == 2, "Passing grades are incorrect" 
```


In these tests we want to use a student object.
But how should we get it using the fixture we defined?



In order to use a fixture, the test method has to get the fixture return value as a **parameter**:
```python
def test_student_failed(student):
  assert did_student_fail(student), "Student did not fail" 
```

Let's take a closer look. Create a new file called test_fixture.py and add the following code:
```python
import pytest

@pytest.fixture
def student():
  return {
    "name": "Shushu",
    "grades": [70, 33, 93, 47]
  }
  
def did_student_fail(student):
  return any(grade < 60 for grade in student["grades"])

def get_passing_grades(student):
  return list(filter(lambda x: x >= 60, student["grades"]))   # tests

def test_student_failed(student):
  assert did_student_fail(student), "Student did not fail"

def test_student_pass(student):
  assert len(get_passing_grades(student)) == 2, "Passing grades are incorrect"﻿ 
```

When we run this line in the terminal:
```console
pytest test_fixture.py 
```

We get this output:
```output
lectures/pytest/tests/fixture.py ..                                                          [100%]
==================================================== 2 passed in 0.01s  
```

---

For more Pytest functionality we strongly recommend you to look here.
