[Pylint](https://pylint.pycqa.org/en/latest/) is a [static code analyser](https://en.wikipedia.org/wiki/Static_program_analysis) for Python.
Pylint analyzes your code without actually running it. It checks for syntax errors, enforces a coding standard, and can make suggestions about how the code could be refactored.

1. Install `pylint` using `pip`.
2. In the root directory of your repo, generate a default template for `.pylintrc` file which is a configuration file used to customize and enforce coding standards, styles, and static analysis checks.

```shell
pylint --generate-rcfile > .pylintrc
```

3. Lint your code locally by:

```shell
python3 -m pylint *.py
```

How many warnings do you get? If you need to ignore some unuseful warning, add it to `disable` list in the `[MESSAGES CONTROL]` section in your `.pylintrc` file.

4. Integrate the linting check in `pr-testing.Jenkinsfile` under the **Lint** stage.
5. Add Pylint reports to Jenkins pipeline dashboard:
   1. Install the [Warnings](https://plugins.jenkins.io/warnings-ng/) plugin.
   2. Change your linting stage to be something like (make sure you understand this change):
   ```text
   steps {
     sh 'python3 -m pylint -f parseable --reports=no *.py > pylint.log'
   }
   post {
     always {
       sh 'cat pylint.log'
       recordIssues (
         enabledForFailure: true,
         aggregatingResults: true,
         tools: [pyLint(name: 'Pylint', pattern: '**/pylint.log')]
       )
     }
   }
   ```
