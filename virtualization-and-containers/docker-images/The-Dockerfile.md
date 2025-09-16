A Docker build consists of a series of ordered build instructions.

# Base Image - the `FROM` Instruction
All Docker images start with a **base image**, and as changes are made and new content is added to the image, new layers are added on top of the base image. The `FROM` [instruction](https://docs.docker.com/engine/reference/builder/#from) uses the official `python:3.8.12-slim-buster` image as the base image upon which our image will be built. This base image is a docker image itself (based on the `debian` image), which provides a lightweight and minimalistic version of the Python runtime environment, allowing developers to build and run Python applications without the need to install Python in the image from scratch.

So, our image is based on a Python base image, which in turn is based on a Debian base image. What is the Debian image based on?

Based on [Hindu mythology](https://en.wikiquote.org/wiki/Turtles_all_the_way_down), the Debian image rests on the back of an elephant which rested in turn on the back of a turtle, what did the turtle rest on? Another turtle. And that turtle? 'Ah, Sahib, after that it is turtles all the way down.'.

Back to the Docker world... all images are based on the `scratch` "image". The `FROM scratch` is a special instruction used in a Dockerfile to indicate that you are starting the image from scratch, without using any existing base image. When `FROM scratch` is specified, it means you are creating the image from the bare minimum, without including any pre-built operating system or runtime environment.

# Working dir - the `WORKDIR` Instruction
The `WORKDIR` [instruction](https://docs.docker.com/engine/reference/builder/#workdir) in a Dockerfile is used to set the working directory for any subsequent instructions within the Dockerfile. It allows you to define the directory where commands such as `RUN`, `CMD`, `COPY`, and `ADD` will be executed.

In our example, we set the working directory inside the container to `/app`.

By setting the working directory, you avoid having to specify the full path for subsequent instructions, making the Dockerfile more readable and maintainable.

# Copying Files From the Build Machine into the Image - the `COPY` Instruction
The `COPY <src> <dst>` instruction copies new files or directories from the `<src>` path in the host machine, and adds them to the filesystem of the image at the path `<dst>`.
In our example, we copy the file under the `.` path, which is the current working directory **relative to the build context**, into the image's file system working directory, which is `/app` according to what is specified in `WORKDIR`.

# The `.dockerignore`
The `.dockerignore` file is used to specify which files and directories should be excluded from the Docker build context when building an image. It works similarly to `.gitignore`, where you can list patterns to match files and directories that should be ignored.

# Spot Check
According to the `.dockerignore` located under `simple_flask_webserver/.dockerignore`, which files wouldn't been copied?

<details>
  <summary>
     Solution
  </summary>

```bash
.git
.vscode
Makefile
README.md
```

</details>

# Execute Commands in the Image - the `RUN` Instruction
The `RUN` [instruction](https://docs.docker.com/engine/reference/builder/#run) in a Dockerfile is used to execute commands during the image build process. It allows you to run any valid command or script inside the image that is being created.

Naturally, after you've copied the application files, you need to install the Python dependencies specified in the `requirements.txt` file. The `RUN pip install -r requirements.txt` instruction does so.

Note that `pip` is already available for you as part of the Python base image.

**Define the command to run a container - the `CMD` instruction.**

The `CMD` [instruction](https://docs.docker.com/engine/reference/builder/#cmd) in a Dockerfile is used to specify the default command to run when a container based on the image is started. It defines the primary executable or process that should be executed within the container.

In our example, we specify the command to run when the container starts, which is `python3 app.py`.