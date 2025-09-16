# Exercise 1 - Push an Image to DockerHub
[Create a free account](https://docs.docker.com/docker-id/) in DockerHub.

Push the built `my_flask_app:0.0.1` image to your registry.

<details>
  <summary>
     Solution
  </summary>

You need to log in to Docker Hub using the docker login command:
```bash
docker login
```
Enter your Docker Hub credentials when prompted.

Tag your local image with the repository information:
```bash
docker tag my_flask_app:0.0.1 your-dockerhub-username/my_flask_app:0.0.1
```
Replace `your-dockerhub-username` with the same information used in the previous docker build command.

Finally, push the image to Docker Hub:
```bash
docker push your-dockerhub-username/my_flask_app:0.0.1
```

</details>

# Exercise 2 - Practicing Images Building
The "Build with Docker" is a great official tutorial that covers basic topics such as image build, as well as advanced topics such as multi-stage builds.

Follow it and complete steps 1 (Introduction), 2 (Layers), 3 (Multi-stage): https://docs.docker.com/build/guide/

# Exercise 3 - Containerize an App
The 2048 game source code is available in this git repo: https://github.com/gabrielecirulli/2048

Use the `nginx:1.23.3-alpine-slim` base image to pack this game in a docker image. Run a container from the newly built image, and make sure you can play the game:
```bash
docker run -p 8080:80 my-2048-game
```

<details>
  <summary>
     Solution
  </summary>

1. Clone the repo by:
    ```bash
    git clone https://github.com/gabrielecirulli/2048
    ```
1. In the 2048 directory, create the following Dockerfile:
    ```bash
    FROM nginx:1.23.3-alpine-slim
    RUN apk --update add
    RUN rm -f -r /usr/share/nginx/html/*
    COPY . /usr/share/nginx/html
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    ```
1. Build the image by `docker build -t my-2048-game .`.
1. Run a container from the image by `docker run -p 8080:80 my-2048-game`.

</details>

# Exercise 4 - Generalize Dockerfile Using ARG
The [ARG instruction](https://docs.docker.com/engine/reference/builder/#arg) in Dockerfile allows you to define variables that users can pass at build-time to customize the build process. These variables can be used during the build to define defaults or pass values into the image at build-time. `ARG` variables do not persist in the final image and are only available during the build process.

Use `ARG` to generalize the build process of the `my_flask_app` image you've built in the last module. Allow to specify a dynamic python value in the build command, for example:
```bash
docker build -t my_flask_app:0.0.1 --build-arg PY_VERSION=3.9.16 .
```
Will build the app image with a base Python image `python:3.9.16`. Another example:
```bash
docker build -t my_flask_app:0.0.1 --build-arg PY_VERSION=3.8.0-slim-buster .
```
Will build the app image with a base Python image `python:3.8.0-slim-buster`.

<details>
  <summary>
     Solution
  </summary>

```bash
ARG PY_VERSION
FROM python:${PY_VERSION}
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
```

</details>

# Exercise 5 - Fix Vulnerability Scanning
Use the `snyk container test` command to perform a vulnerability scan on your `my_flask_app` image.

How many issues were found in total? How critical, high, medium, low? Follow the **Recommendations for base image upgrade** section in Snyk's report to build another version of `` image with another base image to mitigate critical and high vulnerabilities.

<details>
  <summary>
     Solution
  </summary>

```bash
snyk container test my_flask_app:0.0.1 --file=Dockerfile
```
We can build the image with the `python:3.8-slim` base image with 0 critical, 0 high, 0 medium, 52 low (as of May 2023):
```bash
FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
```
And the build command (note the new image tag version):
```bash
docker build -t my_flask_app:0.0.2 .
```

</details>