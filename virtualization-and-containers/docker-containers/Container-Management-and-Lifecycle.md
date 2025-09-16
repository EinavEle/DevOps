To see your **running** containers, type:
```bash
docker container ls
```
or add `-a` flag to list also stopped containers:
```bash
$ docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                      PORTS     NAMES
d841a2fe07f9   nginx     "/docker-entrypoint..."   About a minute ago   Exited (0) 14 seconds ago             funny_blackburn
```
In the above output:
- `d841a2fe07f9` is the container ID - a unique identifier assigned to each running container in Docker.
- `/docker-entrypoint...` is the (beginning) of the actual linux command that has to run to initiate the process of the container.
- `funny_blackburn` is a random alphabetical name that docker assigned to the container.

# Spot Check
Pull and run the container `hello-world`.
1. What is the status of the container after some moments of running?
1. Use `docker images hello-world` to get some information about the image from which the container has run. What is the image size?
1. What is the command used to launch the container `hello-world`?

<details>
  <summary>
     Solutions
  </summary>

1. The container prints "hello world" to the screen and stops.
1. It depends on the image version, but the image size is not more than a few KBs.
1. `docker container ls -a` discovers the running command: `/hello`.

</details>

# Override the Default Command
When the nginx image was built (we will build our own images soon), Docker allows us to specify a default command that defines what is executed when a container is started from the image. However, you can override the default execution command by providing a new command as an argument when running the `docker run` command.

To override the default command, simply append the desired command to the **end** of the `docker run` command.

Let's say you want to run the same above `nginx` container, but you want to modify the default command so nginx is running in debug mode. You can override the default command by:
```bash
docker run nginx nginx-debug -g 'daemon off;'
```
In the above example, the `nginx` container will be initiated using the command `nginx-debug -g 'daemon off;'`.

Here is another very useful example:
```bash
docker pull ubuntu
docker run -it ubuntu /bin/bash
```
The command starts a new Docker container using the [Ubuntu image](https://hub.docker.com/_/ubuntu) and launches an interactive terminal session within the container.

Here's what each part of the command does:
1. `docker run` instructs Docker to create and start a new container.
1. `-it` is a combination of two flags: `-i` keeps STDIN open for the container, and `-t` allocates a pseudo-TTY to allow interaction with the container's terminal.
1. `-t` refers to the Ubuntu image, which is pulled from Docker Hub if not already available locally.
1. `/bin/bash` specifies the command to be executed within the container, in this case, launching a Bash shell.

When you run this command, a new container based on the Ubuntu image is created, and you are provided with an interactive, fresh and beloved `bash` terminal session inside the container. This allows you to directly interact with the Ubuntu environment, run commands, and perform operations within the isolated containerized environment.

Feel free to go wild, you are within a container :-)

# Spot Check
In your open Ubuntu container terminal session:
1. What is the current user?
1. What is the hostname?
1. Is the container connected to the internet? Can you ping `google.com`? Do you have the `ping` command? Install it inside the container!
1. What is the user's home directory?
1. How many processes are running in the container? What could that indicate?
1. Do you have `docker` installed in the container?

<details>
  <summary>
     Solution
  </summary>

1. `root`, as can be seen in the terminal prompt, or via `whoami`.
1. The hostname is the first 12 characters of the full container id. E.g. `7c0aaf2b641f`.
1. Install the ping command by `apt-get install iputils-ping`.
1. `echo $HOME` discovers that the home directory is `/root`.
1. `ps -aux` discovers only one running process (and another temporary process for the `ps` command itself). This indicates that we don't really run a full Ubuntu OS, including all background processes, but only a single poor terminal process.
1. Docker is not installed: type `docker` and get `bash: docker: command not found`.

</details>

# Interacting with Containers
In addition to starting a new container with an interactive terminal session using docker run `-it`, you can also interact with **running** containers using the `docker exec` command.

The `docker exec` command allows you to execute a command inside a running container. Here's the basic syntax:
```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```
Let's see it in action...
Start a new `nginx` container and keep it running. Give it a meaningful name instead of the one Docker generates:
```bash
docker run --name my-nginx nginx
```
Make sure the container is up and running. Since the running container occupying your current terminal session, open up another terminal session and execute:
```bash
$ docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS     NAMES
89cf04f27c04   nginx     "/docker-entrypoint...."   About a minute ago   Up About a minute   80/tcp    my-nginx
```
Now say we want to debug the running nginx container, and perform some maintenance tasks, or execute specific commands within the containerized environment. We can achieve this by:
```bash
docker exec -it my-nginx /bin/bash
```
And you're in... You can execute any command you want within the running `my-nginx` container.

**Tip**: if you don't know the container name, you can `exec` a command also using the container id:
```bash
docker exec -it 89cf04f27c04 /bin/bash
```
# Spot Check
How many running processes does the container run? Hint: you can use the `docker top` command. The first process is the nginx master process, and the rest are workers that should serve incoming requests to the web server.

You are told that the nginx configuration file is located under `/etc/nginx/nginx.conf`.

Install `nano` in the container, and edit the `nginx.conf` as follows:
```bash
- worker_processes  auto;
+ worker_processes  1;
```
Save the file. Stop and start the container again, did the number of workers change?
<details>
  <summary>
     Solution
  </summary>

To check the number of running processes you can perform: `docker top my-nginx`.
After editing the `/etc/nginx/nginx.conf` file, stop and start the container by:
```bash
docker stop my-nginx
docker start my-nginx
```
After restarting the container, you can once again use the `docker top` command to check the number of running processes. It should now show only one worker process.

</details>

# Inspecting a Container
The `docker inspect` command is used to retrieve detailed information about Docker objects such as containers, images, networks, and volumes. It provides a comprehensive JSON representation of the specified object, including its configuration, network settings, mounted volumes, and more.

The basic syntax for the docker inspect command is:
```bash
docker inspect [OPTIONS] OBJECT
```
where `OBJECT` represents the name or ID of the Docker object you want to inspect.

Inspect your running container by:
```bash
$ docker inspect my-nginx
....
```

# Spot Check
In the JSON output:
1. What are the command and arguments the `my-nginx` container runs with?
1. What is the PID (process ID) of the container in the host machine?
1. What are the environment variables that the container has?
1. Which ports does the container expose?
1. What is the container IP address?
1. What is the container default gateway to access the internet?

<details>
  <summary>
     Solution
  </summary>

1. The full command is `/docker-entrypoint.sh nginx -g daemon off;`
1. The `Id` key.
1. Under `Config.Env` keys:
    ```bash
    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "NGINX_VERSION=1.23.1",
    "NJS_VERSION=0.7.6",
    "PKG_RELEASE=1~bullseye"
    ```
1. Under `Config.ExposedPorts`, the exposed ports are `80/tcp`.
1. Under `NetworkSettings.IPAddress`.
1. Under `NetworkSettings.Gateway`.

</details>

# Running Containers in the Background
When running containers with Docker, you have the option to run them in the background, also known as **detached mode**. This allows containers to run independently from your current terminal session, freeing up your terminal for other tasks.

To run a container in the background, you can use the `-d` or `--detach` flag with the docker run command.

Let's run another nginx container:
```bash
$ docker run -d --name my-nginx-2 nginx
310f1c48e402648ce4db41817dd76027d4528e481b25e985296fccc83421ddcb
```
When a container is running in the background, Docker assigns a unique container ID and displays it as output. You can use this ID to reference and manage the container later.

To view the list of running containers, you can use the `docker ps` command. This command lists all the running containers along with their respective container IDs, names, and other information.

Since `my-nginx-2` is running in the background, the `docker logs` command can help you to view the logs generated by a running Docker container. It allows you to retrieve and display the standard output (stdout) and standard error (stderr) logs generated by the container's processes.
```bash
$ docker logs my-nginx-2
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
....
```
If you want a real-time view, add the `-f` (or `--follow`) flag:
```bash
$ docker logs my-nginx-2 -f
...
```

# Killing, Stopping, and Removing Containers
The `docker container stop` command is used to stop one or more running containers in Docker. It **gracefully stops** the containers by sending a `SIGTERM` signal to the main process running inside each container and then waits for a specified timeout (default is 10 seconds) before forcefully terminating them with a `SIGKILL` signal if needed.
```bash
docker container stop my-nginx-2
```
The `docker container kill` command is used to forcefully terminate one or more running containers in Docker. It immediately sends a `SIGKILL` signal to the main process running inside each container, causing them to stop abruptly without any graceful shutdown.

Stopped or killed containers can be restarted using the `docker container start` command, which resumes their execution from the point where they were stopped or killed.

# Restarting a Stopped Container
When you restart a stopped container using the docker container start command, it resumes execution from the point where it was previously stopped. The container retains its configuration and any changes made inside the container's file system prior to stopping.

# Restarting a Killed Container (you'll barely use it...)
When you restart a killed container using the docker container start command, it starts fresh from the beginning, as if it were a newly created container. It's essentially starting a new instance of the container based on the original image and configuration. The container does not retain any previous state or changes made inside the container before it was killed.

It's worth noting that the state of a container (stopped or killed) does not affect the Docker images associated with it. Docker images remain unchanged and can be used to create and start new containers as needed.

The docker container rm command is used to remove one or more stopped or killed containers from Docker. It allows you to delete containers that are no longer needed, freeing up disk space and cleaning up resources. It's important to note that the containers you wish to remove must be in a stopped state. If you attempt to remove a running container, you will encounter an error.
```bash
docker container stop my-nginx my-nginx-2
docker container rm my-nginx my-nginx-2
docker contianer ls -a
```
**Tip**: The `--rm` flag in the `docker run` command is used to automatically remove the container when it exits or stops running. It can be handy when you don't want to retain the container after it has served its purpose.
```bash
docker pull busybox
docker run --rm busybox wget google.com
```

# Spot Check
Docker stored container resources on the host machine under:
```bash
/var/lib/docker/containers/
```
Run some container and take a look on the `/var/lib/docker/containers/<container-id>` directory. Stop the container: does the directory still exist? Remove the container: what happened?

<details>
  <summary>
     Solution
  </summary>

Only when the container is removed, the directory `/var/lib/docker/containers/<container-id>` is removed.

</details>

# Start Containers Automatically
In Docker, the container restart policy determines the actions to be taken by the Docker daemon when a container exits or encounters an error. The restart policy can be specified during container creation using the `--restart` flag with the `docker run` command.
| Flag | Description  |
|---------|----------|
| `no` | Do not automatically restart the container. (the default)  |
| `on-failure[:max-retries]` | Restart the container if it exists due to an error, which manifests as a non-zero exit code. Optionally, limit the number of times the Docker daemon attempts to restart the container using the `:max-retries` option.  |
| `always` | Always restart the container if it stops. If it is manually stopped, it is restarted only when Docker daemon restarts or the container itself is manually restarted. (See the second bullet listed in [restart policy details](https://github.com/alonitac/DevOpsElv/blob/main/docker/02_docker_containers.md#restart-policy-details))  |
| `unless-stopped` | Similar to `always`, except that when the container is stopped (manually or otherwise), it is not restarted even after Docker daemon restarts.  |
The following example starts a nginx container and configures it to always restart unless it is explicitly stopped or Docker is restarted.
```bash
$ docker run -d --restart unless-stopped nginx
```

# Published Ports
By default, when you run a container using the `docker run` command, the container doesn’t expose any of its ports to the outside world. To make a port available to services outside of Docker, or to Docker containers running on a different network, use the `--publish` or `-p` flag. This creates a firewall rule in the container, mapping a container port to a port on the host machine to the outside world.
Here are some examples:
| Title 1 | Title 2  |
|---------|----------|
| `-p 8080:80` | Map TCP port 80 in the container to port `8080` on the host.  |
| -p 192.168.1.100:8080:80 | Map TCP port 80 in the container to port `8080` on the host machine for connections to host IP `192.168.1.100`.  |
| `-p 8080:80/udp` | Map UDP port 80 in the container to port `8080` on the host machine.  |
| `-p 8080:80/tcp -p 8080:80/udp` | Map TCP port 80 in the container to TCP port `8080` on the host machine, and map UDP port `80` in the container to UDP port `8080` on the host machine.  |

To run an `nginx` container with port `80` exposed (the default port in which nginx is listening port incoming requests), you can use the `docker run` command with the `-p` or `--publish` option. Here's the command:
```bash
docker run --name nginx3 -p 8080:80 nginx
```
`-p 8080:80` maps port 80 **in the container** to port 8080 **in the host machine**.

You can then access the nginx web server by opening a web browser and navigating to `http://localhost:8080`.

More docker networking topics will be covered in next chapters.

# Spot Check
Explore the running nginx container logs, can you see a log indicating your request you've just performed from the web browser?

Try to run the container without the `-p` flag and check that the nginx container is not accessible.

<details>
  <summary>
     Solution
  </summary>

Here are some logs sample for the user's request:
```bash
172.17.0.1 - - [14/May/2023:08:17:21 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0" "-"
2023/05/14 08:17:21 [error] 31#31: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [14/May/2023:08:17:21 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0" "-"
```

</details>

# Set Environment Variables For Containers
When running a container using the docker run command, you can specify environment variables using the `-e` or `--env` flag. For example:
```bash
docker run -d -e MY_VAR=my_value --name nginx4 nginx
```

# Spot Check
Run the above command and make sure the `MY_VAR` environment variable is accessible.

<details>
  <summary>
     Solution
  </summary>

```bash
docker exec -it nginx4 /bin/bash -c 'echo $MY_VAR'
```

</details>