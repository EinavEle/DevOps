Up until now we had only one python file `my_test.py` in our project folder but what will happen if we have more than one file?

How will Pytest know what file to run? **The answer is the command line syntax.**


To run all the tests from all the files in folder tests_folder:
```console
pytest tests_folder/ 
```

To run all the tests in a specific file:
```console
pytest my_test.py 
```

**What if we want to run a specific test within a file?**


To run a specific test add `::test_name` :
```console
pytest my_test.py::test_get_name 
```
