Jenkins Pipelines are used to define, manage, and automate the entire lifecycle of software delivery processes (a.k.a. CI/CD pipelines). 
These pipelines provide a structured way to define the steps and stages involved in **building**, **testing**, **deploying**, and **delivering** software applications. 

Jenkins Pipelines enable teams to automate repetitive tasks, and ensure consistent and reliable software releases.


### Motivation

Let's take the Docker images build process as an example...

In our development workflow, whenever we wanted to create a new version of our application, we had to manually run the `docker build` command to create a Docker image.
This process involved remembering the right set of build arguments, manually managing images, and we had no any mechanism to track the build history. 

With Jenkins Pipelines, we can automate the build process, which makes it consistent and reproducible process. 
In addition, Jenkins provides a clear view of the build status, logs, and any errors encountered during the build. 
