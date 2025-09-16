When it comes to Docker images as part of [microservices architecture](https://microservices.io/), big is bad! Images should be as small as possible. Big images are hard to work with by means of the time it takes to pull an image and run it as a container.

Another critical reason is potential vulnerabilities. Containers are designed to run just one application or service, so they only include the necessary code and dependencies for that specific purpose. The bigger your images are, the larger your attack surface, because your image contains more binaries and packages that can potentially have security vulnerabilities.

The [official Alpine Linux](https://hub.docker.com/_/alpine/tags) Docker image is about 3.25MB in size and is an extreme example of how small Docker images can be.

Build your images only with what you need to run the application.