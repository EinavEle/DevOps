Run the `nginx` container by:
```bash
docker pull nginx
docker run nginx
```
When you run this command, the following happens (assuming you are using the default DockerHub registry configuration):
1. Docker pulls the `nginx` image from DockerHub.
1. Docker creates a new container from the `nginx` image. The `nginx` image is a ready-to-run container image that encapsulates the [NGINX web server](https://www.nginx.com/resources/glossary/nginx/) software, along with its dependencies and configuration. When the image is used to create a container, it provides a fully functional NGINX server environment, without the need to install and configure nginx on your machine.
1. Docker allocates a dedicated read-write filesystem to the container (which is completely different and isolated from the host machine fs). This allows a running container to create or modify files and directories in its local filesystem.
1. Docker creates a **virtual network interface** to connect the container to the network. This includes assigning an IP address to the container. By default, containers can connect to external networks using the host machine’s network connection.
1. Docker starts the container.
1. When you type `CTRL+c` the container stops but is not removed. You can start it again or remove it. When a container is removed, its file system is deleted.