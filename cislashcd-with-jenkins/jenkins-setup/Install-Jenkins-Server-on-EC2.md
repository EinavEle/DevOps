
Jenkins is typically run as a standalone application in its own process with the built-in Java servlet container/application.

1. Create a ***.medium, Ubuntu** EC2 instance with `30GB` disk.
2. Connect to your instance, install java by

```bash
sudo apt update
sudo apt install openjdk-11-jre
```

3. Download and install Jenkins as described [here](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu).
4. On Jenkins machine, [install Docker engine](https://docs.docker.com/engine/install/ubuntu/). You may want to add jenkins linux user the docker group, so Jenkins could run docker commands:
   ```shell
   sudo usermod -a -G docker jenkins
   sudo usermod -a -G docker $USER
   ```
5. Install `kubectl`. 
6. Install Git if needed.
6. You'll need your Jenkins server to have static public ip address. From the EC2 navigation pane, create an **Elastic IP** and associate it to your Jenkins instance.
7. Open port `8080` and visit your Jenkins server via `http://<static-ip>:8080` and complete the setup steps.
