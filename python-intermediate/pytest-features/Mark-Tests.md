Pytest allows us to tag our test functions using `@pytest.mark`.

In this way we can decide to run or to skip group of tests according to their tags.

We already saw an example with `skip` and `xfails`.

```python
@pytest.mark.skip
def test_sum1():
  assert 1 + 2 == 3 
```

Another example is when we want to run a group of specific tests. For instance a sanity suit. We can imagine that when we have a large code base we will also have many tests. Many tests = a lot of time to run them all. What if we changed a small thing that probably won't affect our whole code, but we still want to make sure all our important features work. For that we can create a group of tests that will include all the basic important ones.

create a `test_sum.py` file and write into it:

```python
@pytest.mark.sanity
def test_sum1():
  assert 1 + 2 == 3
  
def test_sum2():
  assert 1 + 1 == 2

@pytest.mark.sanity
def test_sum3():
  assert 1 + 0 == 1
  
def test_sum4():
  assert 1 + 5 == 6 
```

Now we can run the sanity tests using the following command in the terminal:
```console
pytest test_sum.py -m sanity 
```

The output we get:                                
```output
collected 4 items / 2 deselected / 2 selected
test_sum.py ..                                                                                [100%]
============================================= 2 passed, 2 deselected in 0.01s =============================================
```

**How awesome!!** Only 2 tests ran and passed!!
The ones we marked with the sanity tag. The others were ignored.


You might noticed that we also got a warning:

```output
PytestUnknownMarkWarning: Unknown pytest.mark.sanity - is this a typo?
You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
PytestUnknownMarkWarning, -- Docs: https://docs.pytest.org/en/latest/warnings.html 
```

This is because we created the `sanity` mark, but pytest doesn't know it.

In order to add our own custom marks, create a `pytest.ini` file in your root folder, and add your own markers.

Here is an example of adding the sanity marker:
```python
[pytest]
markers =
  sanity: minimal amount of basic tests to run   
```

Save the file, and run the sanity group of tests again.

There should be no warning now.


More about markers [here](https://doc.pytest.org/en/latest/example/markers.html)
