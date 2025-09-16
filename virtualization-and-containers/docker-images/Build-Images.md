t's time to learn how to build your own images. In the below example, we will build the Flask application under `simple_flask_webserver`.

A **Dockerfile** is a text document in which you tell docker how to containerize an application.

Assume you start with a clean version of Ubuntu and want to run a Python application. The natural approach might involve manual installation steps such as using `apt-get` to update the system, installing Python, installing app dependencies using `pip`, setting up the application environment, and configuring runtime settings.

A Dockerfile provides a declarative and automated way to define all these steps as instructions for docker to build. The final result after building an image according to a Dockerfile is a self-contained and portable artifact that encapsulates the application code, its dependencies, and the runtime environment. This image can be run as a container on any system that has Docker installed, ensuring consistent behavior and eliminating the need for manual setup and configuration.

Here's the Dockerfile you'll use as the starting point in order to pack our app into an image:
```bash
FROM python:3.8.12-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
```
Under `simple_flask_webserver`, create a file called `Dockerfile` (note the capital D) and copy the above content. We will explain each line soon. For now, let's build an image out of it.

Open up a terminal where the current working directory is `simple_flask_webserver`. Then build the image using the `docker build` command:
```bash
docker build -t my_flask_app:0.0.1 .
```
The working directory from which the image is built is called the **Build context**. In the above case, the `.` at the end of the command specifies to docker that the "current working directory" is the build context. The docker daemon looks by default for a file called `Dockerfile` and builds the image according to the instructions specified in the Dockerfile.