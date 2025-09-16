
Let's create another new Jenkins pipeline that **deploys** the image we've just built to a Kubernetes cluster.

We would like to **trigger** the Deploy pipeline after every successful running of the Build pipeline.

1. In the app repo, create another `Jenkinsfile` called `deploy.Jenkinsfile`. In this pipeline we will define the deployment steps for the roberta app:
```text
pipeline {
    agent any
    
    stages {
        stage('Deploy') {
            steps {
                // complete this code to deploy to real k8s cluster
                sh '# kubectl apply -f ....'
            }
        }
    }
}
``` 

2. In the Jenkins dashboard, create another Jenkins **Pipeline** (can be named `RobertaDeploy`), fill it similarly to the Build pipeline, but **don't trigger** this pipeline as a result of a GitHub hook event (why?).

We now want that every **successful** Build pipeline running will **automatically** trigger the Deploy pipeline. We can achieve this using the following two steps: 

3. In `build.Jenkinsfile`, add the [Pipeline: Build](https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/) function that triggers the Deploy pipeline:

```text
stage('Trigger Deploy') {
    steps {
        build job: '<deploy-job-name>', wait: false, parameters: [
            string(name: 'ROBERTA_IMAGE_URL', value: "<full-url-to-docker-image>")
        ]
    }
}
```

Where:
- `<deploy-job-name>` is the name of your Deploy pipeline (should be `RobertaDeploy`).
- `<full-url-to-docker-image>` is a full URL to the Docker image you've just built. You environment variable to make it dynamically according to the image tag. E.g. : `value: "${IMAGE_NAME}:${IMAGE_TAG}"`.

4. In the `deploy.Jenkinsfile` define a [string parameter](https://www.jenkins.io/doc/book/pipeline/syntax/#parameters) that will be passed to this pipeline from the Build pipeline:

```text
pipeline {
    agent ..
    
    # add the below line in the same level an `agent` and `stages`:
    parameters { string(name: 'ROBERTA_IMAGE_URL', defaultValue: '', description: '') }

    stages ...
}
```

Test your simple CI/CD pipeline end-to-end.
