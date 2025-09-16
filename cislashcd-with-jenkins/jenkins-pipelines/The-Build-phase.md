The Build phase builds the app source code and store the **build artifact** somewhere, make it ready to be deployed.
In our case, a docker image is our build artifact, but in general, there are many other build tools that can be used in different programming languages and contexts (e.g. [maven](https://www.jenkins.io/doc/tutorials/build-a-java-app-with-maven/#fork-and-clone-the-sample-repository-on-github), `npm`, `gradle`, etc...)


#### Guidelines 

We now want to complete the `build.Jenkinsfile` pipeline, such that on every run of this job,
a new docker image of the app will be built and stored in container registry (DockerHub or ECR).

- Modify the `build.Jenkinsfile` to build an docker image and push it. Your stage might look like:

```text
stage('Build') {
   steps {
       sh '''
            docker login ...
            docker build ...
            docker tag ...
            docker push ...
       '''
   }
}
```

- Feel free to create other `stage`s according to your needs.  
- Your image should be pushed either to DockerHub or [ECR](https://console.aws.amazon.com/ecr/repositories) repo.
- You can use the timestamp, or the `BUILD_NUMBER` or `BUILD_TAG` [environment variables](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables) to tag your Docker images, but don't tag the images as `latest`.
- If using ECR, give your EC2 instance an appropriate role to push an image to ECR.
- Use the [`environment` directive](https://www.jenkins.io/doc/book/pipeline/syntax/#environment) to store global variable and make your pipeline a bit more elegant. 
