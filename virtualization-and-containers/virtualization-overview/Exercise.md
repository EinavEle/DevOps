# Exercise - Remote Docker Daemon
As you may know, Docker is designed in client-server architecture, where both sides are not necessarily running on the same machine. Your goal is to run the docker daemon (the server) of a different machine, and communicate with it from your local machine.

Feel free to find useful tutorials either in Docker's official docs or any other resource. You can use some EC2 instances as the remote machine.

<details>
  <summary>
     Solution
  </summary>

Create a directory in which we will create our custom daemon exec command:
```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
```
Use `nano` to open the `options.conf` file:
```bash
sudo nano /etc/systemd/system/docker.service.d/options.conf
```
Add the below lines:
```bash
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H unix:// -H tcp://0.0.0.0:2375
```
Reload the daemon and check the service status:
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl status docker
```
From you local machine:
```bash
export DOCKER_HOST=tcp://<remote-machine-ip>:2375
```
Make sure port `2375` is accessible from outside the remote machine.

Run `docker info` and make sure you identify details of the remote daemon machine.

</details>