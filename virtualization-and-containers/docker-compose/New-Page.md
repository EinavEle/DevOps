Are you tired of executing `docker run`, `docker build`? So are we...

[Docker Compose](https://docs.docker.com/compose/) is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Using Compose is essentially a three-step process:
1. Define your app’s environment with a `Dockerfile` so it can be reproduced anywhere.
1. Define the services that make up your app in `docker-compose.yml` so they can be run together in an isolated environment.
1. Run `docker compose up` and the Docker compose command starts and runs your entire app.

A `docker-compose.yml` looks like this:
```bash
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    depends_on:
      - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
```
The given Docker Compose file describes a multi-service application with two services: `web` and `redis`. Here's a breakdown of some components:
1. `version: "3.9"` specifies the version of the Docker Compose syntax being used.
1. `services`: begins the services section, where you define the containers for your application.
1. `web`: defines a service named `web`. This service is built from the current directory (`build: .`) using a Dockerfile.
1. `volumes`: defines volume mappings between the host and container.
1. `redis`: defines a service named `redis`. This service uses the official Redis image.