A "container image" (or **image**) is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings. You can transfer images from one machine to the other. Every machine is able to "run the image" without the need to install the application dependencies, and define environment variables and networking settings.

A **container** is a single running instance of an image. You can create, start, stop, move, or delete a container, and they can be run easily and reliably from one computing environment to another. The computer that runs the container is frequently referred to as a **host machine**, because it "hosts" containers.

By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container's network, storage, or other underlying subsystems are from other containers or from the host machine.

A container, as we mentioned, is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that are not stored in persistent storage disappear.

### Containers Under Hoods
Under the hoods, containers are merely a **linux process**.

But they are unique processes that "live" in an isolated environment. By this means, the process "believes" that he is the only process in the system; he is **containerized**. Containers are a technology that leverages the Linux kernel's features to provide lightweight and isolated environments for running applications.

Linux containers utilize several key components:
- **Namespaces**: Linux namespaces provide process-level isolation by creating separate instances of various resources, such as the process ID namespace, network namespace, mount namespace, and more. Each container has its own isolated namespace, allowing processes within the container to have their own view of system resources.
- **Control Groups (cgroups)**: Control groups, or cgroups, enable resource management and allocation by imposing limits, prioritization, and accounting on system resources such as CPU, memory, disk I/O, and network bandwidth. Cgroups ensure that containers do not exceed their allocated resources and provide fine-grained control over resource utilization.