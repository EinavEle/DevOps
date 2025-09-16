Let's see some other useful instructions:

# The `ADD` instruction
The `ADD` [instruction](https://docs.docker.com/engine/reference/builder/#add), similar to `COPY`, copies new files and directories from the host machine to the built image. `ADD` has more advanced functionality that `COPY` doesn't have.

For example, `ADD` allows `<src>` to be a URL:
```bash
ADD --checksum=sha256:24454f830cdb571e2c4ad15481119c43b3cafd48dd869a9b2945d1036d1dc68d https://mirrors.edge.kernel.org/pub/linux/kernel/Historic/linux-0.01.tar.gz /
```

The instruction downloads the file located at the specified URL and adds it to the root directory (`/`) of the Docker image. The `--checksum` option ensures that the downloaded file's SHA256 checksum matches the specified value before adding it to the image.

# Executable Containers - the `ENTRYPOINT` Instruction

The `ENTRYPOINT` [instruction](https://docs.docker.com/engine/reference/builder/#entrypoint) is used to specify the main executable for the container. You can optionally provide additional arguments using the `CMD` instructions.

For example, the Nginx official Dockerfile specifies:
```bash
FROM debian:11-slim

# ...

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
```
In the above configurations, the executed command when running an nginx container is:
```bash
/docker-entrypoint.sh nginx -g daemon off;
```
In such a way, `ENTRYPOINT` sets the primary command that cannot be easily overridden, while `CMD` provides default arguments to the `ENTRYPOINT`. Since `CMD` can be overridden by the user running the `docker run`, using them together allows for defining a default behavior for the container, while still providing flexibility for customization.

Images built with the `ENTRYPOINT` instruction are commonly referred to as **executable containers** that can be run consistently across different environments, ensuring the application runs as intended without the need for manually specifying the command every time the container is started.

That's all for Dockerfile instructions.

While there are several [instructions available](https://docs.docker.com/engine/reference/builder/) to use within Dockerfiles, it's not necessary to learn every single instruction in detail, as familiarity with the commonly used instructions is sufficient for creating and customizing Docker images.