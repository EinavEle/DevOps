
1. In `main` branch, create the `pr-testing.Jenkinsfile` as follows:
```text
pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                echo "testing"
            }
        }
        stage('Lint') {
            steps {
                echo "linting"
            }
        }
        stage('Functional test') {
            steps {
                echo "testing"
            }
        }
    }
}
```
2. Commit the Jenkinsfile and push it.
3. From the Jenkins dashboard page, choose **New Item**, and create a **Multibranch Pipeline** named `pr-testing`.
4. Under **Branch Sources** choose **GitHub**
5. In the **GitHub** source section, under **Behaviors**, delete all behaviors other than **Discover pull requests from origin**. Configure this behavior to **Merging the pull request with the target branch revision**.


### Test the pipeline

6. From branch `main` create a new branch called `sample_feature` and change some code lines. Push the branch to remote.
7. In your app GitHub page, create a Pull Request from `sample_feature` into `main`.
8. Watch the triggered pipeline in Jenkins. 

