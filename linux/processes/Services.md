In Linux, services are **background processes** that run continuously and provide specific functions to the operating system or other applications. Here are some common Linux services:
1. `ssh`: A secure remote login protocol that allows users to log in to a remote computer securely.
1. `cron`: A service that executes scheduled tasks or commands at specified intervals.
1. `ufw`: An easy-to-use interface for configuring and managing firewall rules on a Linux system.
1. `apache`: A web server that serves HTML pages and other files over the internet.

The `systemctl` command is used to manage services in your system:
```bash
myuser@hostname:~$ sudo systemctl status ufw
● ufw.service - Uncomplicated firewall
     Loaded: loaded (/lib/systemd/system/ufw.service; enabled; vendor preset: enabled)
     Active: active (exited) since Sun 2022-01-01 07:25:58 UTC; 2h 16min ago
       Docs: man:ufw(8)
   Main PID: 338 (code=exited, status=0/SUCCESS)
        CPU: 1ms

Jan 01 07:25:58 hostname systemd[1]: Starting Uncomplicated firewall...
Jan 01 07:25:58 hostname systemd[1]: Finished Uncomplicated firewall.
myuser@hostname:~$ sudo systemctl stop ufw
myuser@hostname:~$ sudo systemctl start ufw
myuser@hostname:~$ sudo systemctl restart <service name>
```
Enable a service to start automatically at boot time by:
```bash
sudo systemctl enable <service name>
```
##### *Who manages Linux services?*
As can be seen in the output of `pstree`, **systemd** is the first process in many Linux distributions, which is a system and service manager that provides a way to manage and control system services. Systemd reads **unit files**, which are configuration files used by systemd to define system services.

Unit files can be found in the `/etc/systemd/system` directory:
```bash
myuser@hostname:~$ ls  /etc/systemd/system/*.service
/etc/systemd/system/sshd.service
/etc/systemd/system/mysql.service
/etc/systemd/system/jenkins.service
...
```
List all your system services:
```bash
myuser@hostname:~$ systemctl list-units --type=service
 UNIT                                              LOAD   ACTIVE SUB     DESCRIPTION                
  accounts-daemon.service                          loaded active running Accounts Service           
  acpid.service                                    loaded active running ACPI event daemon          
  alsa-restore.service                             loaded active exited  Save/Restore Sound Card 
....
```
In the above output, UNIT represents the unit name, LOAD indicates that the unit’s configuration has been read by systemd, ACTIVE is the state of the unit.