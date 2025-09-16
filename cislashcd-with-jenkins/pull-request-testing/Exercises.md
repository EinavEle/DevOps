### Exercise 1 - Run tests in parallel 

Use [`parallel`](https://www.jenkins.io/doc/book/pipeline/syntax/#parallel) directive to run the test stages in parallel, while failing the whole build when one of the stages is failed.

### Exercise 2 - Implement Python dependency vulnerability testing

While Snyk scans vulnerabilities in the container OS level, it's also necessary to scan your Python code and the dependencies you use. 

Integrate [safety](https://pyup.io/safety/) and [bandit](https://bandit.readthedocs.io/en/latest/) into the `pr-testing.Jenkinsfile` pipeline. 

