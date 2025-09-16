By default, all files created inside a container are stored on a writable container layer. This means that the data doesn’t persist when that container no longer exists.

Docker has two options for containers to store files on the host machine, so that the files are persisted even after the container stops: **volumes** and **bind mounts**.

# Bind Mounts
**Bind mounts** provide a way to mount a directory or file **from the host machine into a container**. Bind mounts directly map a directory or file on the host machine to a directory in the container.

Let's take the good old `nginx` image:
```bash
docker run --rm -p 8080:80 -v /path/on/host:/usr/share/nginx/html --name my-nginx nginx:latest
```
In this example, we're running an Nginx container while the `-v /path/on/host:/usr/share/nginx/html` flag specifies the bind mount. It maps the directory `/path/on/host` on the host machine to the `/usr/share/nginx/html` directory inside the container.

Whenever the `my-nginx` container is accessing `/usr/share/nginx/html` path, the directory it actually sees is `/path/on/host` on the host machine. More than that, every change the container makes to the `/usr/share/nginx/html` directory will reflect in the corresponding location on the host machine, `/path/on/host`, due to the bind mount. The other way also applies, changes made on the host machine in `/path/on/host` will be visible inside the container under `/usr/share/nginx/html`.

As you may know, `/usr/share/nginx/html` is the location from which Nginx serves static content files. In that way, files you'll place in `/path/on/host` on your host machine, will be served by the running nginx container, without the need to copy those files to the container during build time.

Bind mounts are commonly used for development workflows, where file changes on the host are immediately reflected in the container without the need to rebuild or restart the container. They also allow for easy access to files on the host machine, making it convenient to provide configuration files, logs, or other resources to the container.

# Spot Check
1. In your host machine, create a directory and put some sample `index.html` file in it (search for sample file on the internet).
1. Run an nginx container while mapping the path `/usr/share/nginx/html` within the container to your created directory.
1. Open up your browser and visit the nginx webserver: `http://localhost:8080`. Make sure the nginx serves your file.
1. On your host machine, delete `index.hmtl`.
1. Refresh the server and make sure the nginx is responding with `404` page not found error.

<details>
  <summary>
     Solution

This spot check is a simple follow-up.

</details>

# Volumes
**Docker volumes** are another way to persist data in containers. While bind mounts are dependent on the directory structure and OS of the host machine, volumes are logical space that is completely managed by Docker. Volumes offer a higher level of abstraction, allowing us to work with different kinds of storages, e.g. volumes stored on remote hosts or cloud providers. Volumes can be shared among multiple containers.

**Create and manage volumes**
Unlike a bind mount, you can create and manage volumes outside the scope of any container.
```bash
docker volume create my-vol
```
Let's inspect the created volume:
```bash
$ docker volume inspect my-vol
[
    {
        "CreatedAt": "2023-05-10T14:28:15+03:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/my-vol/_data",
        "Name": "my-vol",
        "Options": {},
        "Scope": "local"
    }
]
```
Inspecting the volume discovers the real location that the data will be stored on the host machine: `/var/lib/docker/volumes/my-vol/_data`.

The `local` volume driver is the default built-in driver that stores data on the local host machine. But docker offers [many more](https://docs.docker.com/engine/extend/legacy_plugins/#volume-plugins) drivers that allow you to create different types of volumes that can be mapped to your container. For example, the [Azure File Storage plugin plugin](https://github.com/Azure/azurefile-dockervolumedriver) lets you mount Microsoft Azure File Storage shares to Docker containers as volumes.

The following example mounts the volume `my-vol` into `/usr/share/nginx/html` in the container.
```bash
docker run --rm --name my-nginx -v my-vol:/usr/share/nginx/html nginx:latest
```
Essentially we've got the same effect as the above example, but now the mounted volume is not just a directory in the OS, but logically managed by docker.

Can you see how elegant is it? Volumes provide a seamless abstraction layer for persisting data within containers. The container believes it reads and writes data from some location in his file system (`/usr/share/nginx/html`), without any knowledge of the underlying storage details (of the `my-vol` volume). If we would have used the Azure File Storage plugin, the data would be actually stored in the cloud.

Remove a volume:
```bash
docker volume rm my-vol
```
**More about volumes**
- A given volume can be mounted into multiple containers simultaneously.
- When no running container is using a volume, the volume is still available to Docker and is not removed automatically.
- If you mount an **empty volume** into a directory in the container in which files or directories exist, these files or directories are **propagated (copied)** into the volume.
- Similarly, if you start a container and specify a volume which does not already exist, an empty volume is created for you. This is a good way to pre-populate data that another container needs.
- If you mount a **bind mount** or **non-empty volume** into a directory in the container in which some files or directories exist, these files or directories are **obscured by the mount**.

**Read-only volumes**
Sometimes, the container only needs read access to the data, so multiple containers can safely mount the same volume without write race condition. You can simultaneously mount a single volume as read-write for some containers and as read-only for others.

The following example mounts the directory as a read-only volume, by adding `ro` to the `-v` flag:
```bash
docker run -d \
  --name=nginxtest \
  -v nginx-vol:/usr/share/nginx/html:ro \
  nginx:latest
```
Other possible options are:
1. `ro` (Read-Only): Mounts the volume in read-only mode, allowing only read operations.
1. `rw` (Read-Write): Mounts the volume in read-write mode, allowing both read and write operations (the default).
1. `Z` (Shared): Marks the volume as shared, allowing it to be **safely** shared between multiple containers.
1. `nocopy` (No Copy): Indicates that the volume should not be copied from the container image but instead be created as an empty volume.
1. `delegated` (Delegated Copy): Specifies that the volume should be created as an empty volume but be populated with data from the container image on-demand.

Where multiple options are present, you can separate them using commas.

# Spot Check
Run the above container with the `ro` option:
```bash
docker run -d \
  --name=nginxtest \
  -v nginx-vol:/usr/share/nginx/html:ro \
  nginx:latest
```
Then connect to the container using the `docker exec` command, try to write some data to the read only location. What error are you facing?

<details>
  <summary>
     Solution
  </summary>

```bash
docker run -d --name=nginxtest -v nginx-vol:/usr/share/nginx/html:ro nginx:latest
docker exec -it nginxtest /bin/bash
```
From within the container, exec:
```bash
root@be4e62c6c9ba:/# touch /usr/share/nginx/html/test
touch: cannot touch '/usr/share/nginx/html/test': Read-only file system
```

</details>

# tmpfs Mounts
Volumes and bind mounts let you share files between the host machine and container so that you can persist data even after the container is stopped.

As opposed to volumes and bind mounts, a **tmpfs mount** is a temporary file system, and only persisted in the host memory (RAM). When the container **stops**, the tmpfs mount is removed, and files written there won’t be persisted.

This is useful to temporarily store sensitive files that you don’t want to persist in either the host or the container writable layer.

To use a tmpfs mount in a container, use the `--tmpfs` flag. There is no source for tmpfs mounts. The following example creates a tmpfs mount at `/app` in a Nginx container.
```bash
docker run -d \
  -it \
  --name tmptest \
  --tmpfs /app \
  nginx:latest
```