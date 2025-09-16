
## Exercise 1 - Clean the build artifacts from Jenkins server

Use the [`post` directive](https://www.jenkins.io/doc/book/pipeline/syntax/#post) and the [`docker image prune` command](https://docs.docker.com/config/pruning/#prune-images) to cleanup the built Docker images from the disk. 

## Exercise 2 - Fine tune the your pipelines

Review some additional pipeline features, as part of the [`options` directive](https://www.jenkins.io/doc/book/pipeline/syntax/#options). Add the `options{}` clause with the relevant features for the Build and Deploy pipelines.

## Exercise 3 - Clean the workspace after every build 

Jenkins does not clean the workspace by default after a build. 
Jenkins retains the contents of the workspace between builds to improve performance by avoiding the need to re-fetch and recreate the entire workspace each time a build runs.

Cleaning the workspace can help ensure that no artifacts from previous builds interfere with the current build.

Configure `stage('Clean Workspace')` stage to [clean the workspace](https://www.jenkins.io/doc/pipeline/steps/ws-cleanup/) before or after a build. 

## Exercise 4 - Security vulnerability scanning

Integrate `snyk` image vulnerability scanning into your build-deploy pipline.

#### Guidelines

- Create a **Secret text** Jenkins credentials containing the snyk API token.
- Use the [`withCredentials` step](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/), read your Snyk API secret as `SNYK_TOKEN` env var, and perform the security testing using simple `sh` step and `synk` cli.
- Sometimes, Snyk alerts you for a vulnerability that has no update available, or that you do not believe to be currently exploitable in your application. You can ignore a specific vulnerability in a project using the [`snyk ignore`](https://docs.snyk.io/snyk-cli/test-for-vulnerabilities/ignore-vulnerabilities-using-snyk-cli) command:

```text
snyk ignore --id=<ISSUE_ID>
```

- **Bonus:** use [Snyk Jenkins plugin](https://docs.snyk.io/integrations/ci-cd-integrations/jenkins-integration-overview) or use the [Jenkins HTML publisher](https://plugins.jenkins.io/htmlpublisher/) plugin together with [snyk-to-html](https://github.com/snyk/snyk-to-html) project to generate a UI friendly Snyk reports in your pipeline page.

## Exercise 5 - Backup pipeline

Create a new Jenkins pipeline and code the corresponding `Jenkinsfile`, to periodically backup the Jenkins server in S3.

- In the Jenkinsfile, use bash script that compresses the `/var/lib/jenkins` directory into a `.tar.gz` file, [excluding some files](https://www.jenkins.io/doc/book/system-administration/backing-up/#back-up-the-controller-key-separately).
- Push the `.tar.gz` file to an S3 bucket.
- The pipeline should be running periodically once a day. 

## Exercise 6 - Shared libraries

https://www.jenkins.io/blog/2017/02/15/declarative-notifications/