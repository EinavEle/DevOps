
Unit testing is a software testing technique where individual components of code are tested in isolation to ensure they behave as expected, helping to identify and fix bugs before the code is built.

In Python, `unittest` is a testing framework that allows developers to write and run unit tests.

1. In the `roberta` directory, you are given directory called `tests`. This is a common name for the directory containing all unittests files. The directory contains a file called `test_cache.py` which implements unittest for the caching functionality of the app (the server caches the recent requested texts and their results). 

2. Run the unittest locally, check that all tests are passed:

```shell
cd roberta
python3 -m pytest --junitxml results.xml tests
```

**Note**: Usually the `unittest` package is used to execute unit tests in Python, but here we used the `pytest` package (has to be installed by `pip install pytest`). We did it because `pytest` allows to export the test results in a `.xml` file format that can be presented by Jenkins in a human friendly format.

3. Integrate the unittesting in the `pr-testing.Jenkinsfile` under the **Unittest** stage.

4. You can add the following `post` step to display the tests results in the readable form:

```text
post {
    always {
        junit allowEmptyResults: true, testResults: 'results.xml'
    }
}
```

5. Try to intentionally make the test fail, and make sure Jenkins is blocking the PR to be merged when the unittest stage fails!