Up until now we ran only one file each time but in a real scenario, we have a number (a big number) of tests files and each file has many tests methods. Most of the time we would like to run them all, which can lead to a large execution time if ran in sequential order.

To overcome this, we can use `-n` flag when running Pytest, which allows us to **run tests in parallel**.


First, we need to install **pytest-xdist**:
```console
pip3 install pytest-xdist 
```

Now, we can run this command:
```console
pytest test_sum.py -n 3 
```

`-n [num]` runs the test by using multiple processes.

Try it on a test with large number of tests to see the difference.
