
The first step is to run jobs **within a docker containers**. The containers will still be running on the Jenkins server itself, later on we will integrate other agents and execute the containers on them. 


## Spot check

Taking the factors mentioned above (performance, build environments and isolation), which of them have been achieved by running jobs in containers?

<details>
  <summary>
     Solution
  </summary>
    Build environments and Isolation
</details>

<br><br>

Let's create a Docker image that will be used as a **build agent** for our existed pipelines. One image for all pipelines. 
The image will be based on the [jenkins/agent](https://hub.docker.com/r/jenkins/agent/) image, 
which is suitable for running Jenkins jobs (with Java installed and other executable Jenkins uses).

What else do we need in this image to run our pipelines? We need `aws` cli, `docker`, `snyk`, `python`, and maybe more... very rich and colorful Docker image! 
We are going to utilize Docker [multistage builds](https://docs.docker.com/build/building/multi-stage/) for that. 

Take a look on the following Dockerfile:

```dockerfile
FROM ubuntu:latest as installer
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN apt-get update \
  && apt-get install -y unzip \
  && unzip awscliv2.zip \
  && ./aws/install --bin-dir /aws-cli-bin/

# this is an example demostrating how to install a tool on a some Docker image, then copy its artifacts to another image
RUN mkdir /snyk && cd /snyk \
    && curl https://static.snyk.io/cli/v1.666.0/snyk-linux -o snyk \
    && chmod +x ./snyk

FROM jenkins/agent

# Copy the `docker` (client only!!!) from `docekr` image to this image.
COPY --from=docker /usr/local/bin/docker /usr/local/bin/
COPY --from=installer /usr/local/aws-cli/ /usr/local/aws-cli/
COPY --from=installer /aws-cli-bin/ /usr/local/bin/
COPY --from=installer /snyk/ /usr/local/bin/
```

The dockerfile starts with [`ubuntu:latest`](https://hub.docker.com/_/ubuntu) as an `installer` image in which we will install `aws` cli and [`snyk`](https://docs.snyk.io/snyk-cli).
After the `installer` image was built, we will copy the relevant artifacts to the main image, the one starting with `FROM jenkins/agent`.

1. Build the image.
2. Push your image to a dedicated container registry in ECR or DockerHub.
3. In the `build.Jenkinsifle`, replace `agent any` by:

```text
agent {
    docker {
        image '<image-url>'       
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
}
```

This directive tell Jenkins to run the pipeline on a docker container.

**Now pay attention!!!** Since as part of the build pipeline (`RobertaBuild`) we build a docker image, there is a [problem](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/) of building a docker image from within a docker container, also known as [**dind** - docker in docker](https://hub.docker.com/_/docker). 
To solve this, we want the use the docker client **within** the agent container, to send the `docker build` command to the daemon resides **outside** the container, on the Jenkins server. This way we bypass the docker-in-docker problem, as the image is actually being built outside the container. Only the build command is sent from within the container. How do we do that? 

- The `-v` mount the socket file that the _docker client_ is using to talk with the _docker daemon_. In this case the docker client **within** the container will talk with the docker daemon operates **outside** the container on Jenkins machine.  
- The `--user root` runs the container as `root` user, which is necessary to access `/var/run/docker.sock`.

4. Test your pipeline on the Docker-based agent.
