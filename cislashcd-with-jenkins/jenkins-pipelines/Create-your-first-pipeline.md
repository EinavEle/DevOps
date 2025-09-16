### The `Jenkinsfile`

A Jenkins pipeline is defined in a file usually called `Jenkinsfile`, stored as part of the code repository.
In this file you instruct Jenkins on how to build, test, and deploy your application by specifying a series of stages, steps, and configurations.  

There are two main types of syntax for defining Jenkins pipelines in a Jenkinsfile: [Declarative Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline) and [Scripted Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/#scripted-pipeline).

- Declarative syntax is a more structured and easy. It uses a predefined set of functions (a.k.a [directives](https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-directives)) to define the pipeline's structure.
- Scripted syntax provides a more flexible and powerful way to define pipelines. It allows you to use Groovy scripting to customize and control every aspect of the pipeline. This pipelines won't be covered in this course.

The `Jenkinsfile` typically consists of multiple **stages**, each of which performs a specific **steps**, such as building the code as a Docker image, running tests, or deploying the software to Kubernetes cluster.

Let's create a declarative pipeline that builds aa docker image for the Roberta app.  

1. In your repository, in branch `main`, create a file called `build.Jenkinsfile` in the root directory as the following template:

```text
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'echo building...'
            }
        }
    }
}
```

The Jenkinsfile you've provided is written in Declarative Pipeline syntax. Let's break down each part of the code:

- `pipeline { ... }`: This is the outermost block that encapsulates the entire pipeline definition.
- `agent any`: This directive specifies the [agent](https://www.jenkins.io/doc/book/using/using-agents/) where the pipeline stages will run. The `any` keyword indicates that the pipeline can run on any available agent (Jenkins agent or worker). Agents are the compute resources where the pipeline stages are executed.
- `stages { ... }`: The [stages block](https://www.jenkins.io/doc/book/pipeline/syntax/#stages) contains a series of stages that define the major steps in the pipeline. Stages represent different phases of the software delivery process.
- `stage('Build') { ... }`: This directive defines a specific stage named "Build." Each stage represents a logical phase of your pipeline, such as building, testing, deploying, etc.
- `steps { ... }:` Inside the stage block, the [steps block](https://www.jenkins.io/doc/book/pipeline/syntax/#steps) contains the individual steps or tasks to be executed within that stage.
- `sh 'echo building...'`: This directive is a step that executes a shell command. In this case, it uses the sh (shell) step to run the shell command 'echo building...'. This step prints "building..." to the console.

2. Commit and push your changes.

### Configure the pipeline in Jenkins

3. From the main Jenkins dashboard page, choose **New Item**.
4. Enter the project name (e.g. `RobertaBuild`), and choose **Pipeline**.
5. Check **GitHub project** and enter the URL of your GitHub repo.
6. Under **Build Triggers** check **GitHub hook trigger for GITScm polling**.
7. Under **Pipeline** choose **Pipeline script from SCM**.
8. Choose **Git** as your SCM, and enter the repo URL.
9. If you don't have yet credentials to GitHub, choose **Add** and create **Jenkins** credentials.
   1. **Kind** must be **Username and password**
   2. Choose informative **Username** (as **github** or something similar)
   3. The **Password** should be a GitHub Personal Access Token with the following scope:
      ```text
      repo,read:user,user:email,write:repo_hook
      ```
      Click [here](https://github.com/settings/tokens/new?scopes=repo,read:user,user:email,write:repo_hook) to create a token with this scope.
   4. Enter `github` as the credentials **ID**.
   5. Click **Add**.
10. Under **Branches to build** enter `main` as we want this pipeline to be triggered upon changes in branch main.
11. Under **Script Path** write the path to your `build.Jenkinsfile` defining this pipeline.
12. **Save** the pipeline.
13. Test the integration by add a [`sh` step](https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/#linux-bsd-and-mac-os) to the `build.Jenkinsfile`, commit & push and see the triggered job.

Well done! You've implemented an automated build pipeline for the Roberta app.


## Spot check 

In the above settings, where are the `sh` commands executed, and what is the security concern about that?
<details>
  <summary>
     Solution
  </summary>
    The `sh` command are executed on the Jenkins machine itself (a.k.a Jenkins Controller). This approach introduces serious security issues, as attacker can potentially execute any random code on the Jenkins server and get access to sensitive data.  
</details>
 

