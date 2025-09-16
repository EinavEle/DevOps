Given the fact that the docker client and the daemon are communicating using a socket located under `/var/run/docker.sock`, why is `sudo` required to execute `docker` command?
<details>
  <summary>
     Solution
  </summary>

This is because the Docker daemon runs with root-level permissions for security reasons, and the default Unix socket file (`/var/run/docker.sock`) is only accessible by the root user or users in the `docker` group.

</details>