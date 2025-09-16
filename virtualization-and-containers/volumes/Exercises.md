# Exercise 1 - Understanding User File Ownership in Docker
When running a container, the default user inside the container is often set to the `root` user, and this user has full control of the container's processes. Since containers are isolated processes in general, we don't really care that `root` is the user operating within the container.

But, when mounting directories from the host machine using the `-v` command, it is important to be cautious when using the root user in a container. Why?

We will investigate this case in this exercise...
1. On your host machine, create a directory under `~/test_docker`.
1. Run the `ubuntu` container while mounting `/test` within the container, into `~/test_docker` in the host machine:
    ```bash
    docker run -it -v ~/test_docker:/test ubuntu /bin/bash
    ```
1. From your host machine, create a file within the `~/test_docker` directory.
1. From the `ubuntu` container, list the mounted directory (`/test`), can you see the file you've created from your host machine? Who are the UID (user ID) and GID (group ID) owning the file?
1. From within the container, create a file within `/test`.
1. List `~/test_docker` from your host machine. Who are the user and group owning the file created from the container?
1. Try to indicate the potential vulnerability: "If an attacker gains control of the container, they may be able to..."
1. Repeat the above scenario, but instead of using `-v`, use docker volumes. Start by creating a new volume by: `docker create volume testvol`. Describe how using docker managed volume can reduce the potential risk.

<details>
  <summary>
     Solution
  </summary>

1. From your host machine: `mkdir ~/test_docker`
1. From your host machine: `docker run -it -v ~/test_docker:/test ubuntu /bin/bash`
1. From your host machine: `touch ~/test_docker/myfile.txt`
1. From the ubuntu container: `ls -l /test`. The UID and GID owning the file will correspond to the user and group IDs on the host machine.
1. From the ubuntu container: touch `/test/container_file.txt`
1. From your host machine: `ls -l ~/test_docker`. The file container_file.txt, created within the container, should be visible. The user and group owning the file will correspond to the user and group IDs inside the container, which is `root`!!!
1. If an attacker gains control of the container, they may be able to manipulate or access files within the mounted directory on the host machine, potentially compromising sensitive data or introducing malicious files.
1. From the host machine:
    ```bash
    docker volume create testvol
    docker run -it -v testvol:/test ubuntu /bin/bash
    ```

When using Docker managed volumes, the potential risk is reduced because Docker handles the volume management and ensures proper access control. The files within the volume are isolated from the host machine, providing an additional layer of security.

</details>

# Exercise 2 - Persist MongoDB Database
Your goal is to run MongoDB container persistently. Running a Mongodb container persistently means that data stored in the container will be preserved even if the container is stopped or restarted.

You need to store the data in a location outside the container, using either bind-mounts or volumes, to your choice.

Here are general guidelines:
1. Review the [Mongo official image](https://hub.docker.com/_/mongo) in DockerHub. Specifically, read the **Start a mongo server instance** section to get an idea of how to run the Mongo container. Then read the **Where to Store Data** section to see where Mongo stores its data and think about how to persist the data stored in this path.
1. Run the container with the relevant environment variables and volume mounting.
1. Watch the container logs, make sure the database is up and running (search for the `ready for connections` log).
1. Exec to your running container by: `docker exec -it <container-id-or-name> /bin/bash`:
    1. Within the container, start a Mongo shell session by: `mongosh`. The `mongosh` terminal session is used for interacting with a Mongo database server from the command line.
    1. Switch to work against some experimental database: `use mydatabase`
    1. Write some data by: `db.myCollection.insertOne({ name: "John Doe", age: 30 })`.
    1. Exit the terminal.
1. Kill the container: `docker kill <container-id-or-name>`.
1. Start a new Mongo container, with the same volume mapping.
1. Exec to your new running container by: `docker exec -it <container-id-or-name> /bin/bash`:
    1. Within the container, start a Mongo shell: `mongosh`.
    1. Switch to work against your previous db: `use mydatabase`.
    1. Verify that the data was successfully survived container kill, by: `db.myCollection.find()`.
    1. You should see the inserted data.

<details>
  <summary>
     Solution
  </summary>

In order to successfully persist the data, the following volume mapping can be set:
```bash
docker run --name some-mongo -v ~/mongotest:/data/db -d mongo
```
The `-v ~/mongotest:/data/db` option binds the directory `~/mongotest` on the host machine to the `/data/db` directory inside the container, the directory where Mongo stores its data.

</details>

# Exercise 3 - Investigate Volume Mounting
Use the `ubuntu` container to experiment with volume mounting and answer the following questions:
1. What happens when you mount an **empty docker volume** into a directory in the container in which files or directories exist?
1. What happens when you start a container and specify a docker volume name that does not exist?
1. What happens when you mount a path using a **bind mount** of a non-empty directory in the container?
1. What happens when you start a container and specify paths (both in the host machine and the container) that do not exist?

<details>
  <summary>
     Solution
  </summary>

1. The existing files and directories are copied to the empty volume and remain accessible within the container.
1. An empty volume is created for you.
1. These files or directories are obscured by the mount.
1. If you specify a host path that does not exist, docker will attempt to create the directory or file at that location. If the parent directory of the specified path doesn't exist either, docker will return an error. If you specify a container path that does not exist, docker will create the directory or file inside the container at that location. If the parent directory of the specified path doesn't exist within the container, docker will create the entire directory structure.

</details>