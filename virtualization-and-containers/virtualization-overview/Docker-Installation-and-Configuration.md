Please [install Docker](https://docs.docker.com/engine/install/ubuntu/) if you haven't done it yet.

**Tip**: You can add your user to the docker group, so you can use the docker command without `sudo`:
```bash
sudo usermod -aG docker $USER
```
Upon up and running the `docker` installation, the docker version command output may look like this:
```bash
Client: Docker Engine - Community
 Version:           20.10.22
 API version:       1.41
 Go version:        go1.18.9
 Git commit:        3a2c30b
 Built:             Thu Dec 15 22:28:02 2022
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.22
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.18.9
  Git commit:       42c8b31
  Built:            Thu Dec 15 22:25:51 2022
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.14
  GitCommit:        9ba4b250366a5ddde94bb7c9d1def331423aa323
 runc:
  Version:          1.1.4
  GitCommit:        v1.1.4-0-g5fd4c4d
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```
Note that docker is running as a service on your system, and hence can be controlled by `systemctl`:
```bash
$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; disabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-05-07 09:56:45 IDT; 5min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 261600 (dockerd)
      Tasks: 123
     Memory: 209.5M
     CGroup: /system.slice/docker.service
             └─261600 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

May 07 09:56:39 hostname dockerd[261600]: time="2023-05-07T09:56:39.509330916+03:00" level=warning msg="Your kernel does not support CPU realtime scheduler"
May 07 09:56:39 hostname dockerd[261600]: time="2023-05-07T09:56:39.509350949+03:00" level=warning msg="Your kernel does not support cgroup blkio weight"
May 07 09:56:39 hostname dockerd[261600]: time="2023-05-07T09:56:39.509365744+03:00" level=warning msg="Your kernel does not support cgroup blkio weight_device"
May 07 09:56:39 hostname dockerd[261600]: time="2023-05-07T09:56:39.533460844+03:00" level=info msg="Loading containers: start."
May 07 09:56:42 hostname dockerd[261600]: time="2023-05-07T09:56:42.942065068+03:00" level=info msg="Default bridge (docker0) is assigned with an IP address 172.17.0.0/16. Daemon option --bip can be used to set a preferred IP address"
May 07 09:56:43 hostname dockerd[261600]: time="2023-05-07T09:56:43.248511892+03:00" level=info msg="Loading containers: done."
May 07 09:56:44 hostname dockerd[261600]: time="2023-05-07T09:56:44.943477277+03:00" level=info msg="Docker daemon" commit=42c8b31 graphdriver(s)=overlay2 version=20.10.22
May 07 09:56:44 hostname dockerd[261600]: time="2023-05-07T09:56:44.972157071+03:00" level=info msg="Daemon has completed initialization"
May 07 09:56:45 hostname dockerd[261600]: time="2023-05-07T09:56:45.533037228+03:00" level=info msg="API listen on /var/run/docker.sock"
May 07 09:56:45 hostname systemd[1]: Started Docker Application Container Engine.
```
From docker's service status output we can learn a few important properties of the docker client and daemon.

When the Docker client (`docker`) and daemon (`dockerd`) are on the same machine (usually the case), they communicate using a UNIX socket located in `/var/run/docker.socket`, typically via RESTful API endpoints.

When the client and daemon are not on the same machine, they communicate over the internet via HTTPS protocol.

What else can we learn about the docker daemon? That it does not run containers itself! Docker relies on the `containerd` service to manage container lifecycle. Containerd is an open-source container runtime that provides a **high-level interface** for managing container lifecycle and execution. It serves as the underlying runtime for various container platforms, including Docker. Containerd, in turn, uses `runc` as the default OCI-compliant runtime for actually running containers. Containerd utilizes `runc` to execute the container processes, manage resource isolation, and handle **low-level interface** container operations according to the OCI specification.

To summarize, containers are not exclusive to Docker, they are a broader technology and concept that existed before Docker's popularity. Docker popularized and simplified the adoption of containers by providing a user-friendly interface and tooling, but there are alternative container runtimes and platforms available, such as Podman, that leverage containers for application deployment and management.

Under the hood, `runc` does the dirty job of running containers:
![.guides/img/runc](./runc.png)
In a moment, you'll run you first container, this is the execution order of the different components that responsible for the container execution:
![.guides/img/order](./order.png)