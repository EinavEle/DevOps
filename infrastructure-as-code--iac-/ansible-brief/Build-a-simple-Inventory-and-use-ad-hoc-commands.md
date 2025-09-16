Ansible works against multiple nodes or "hosts" using a list or group of lists known as [Inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html).

An **ad-hoc command** is a single, one-time command that you run against your inventory, without actually specifying the command or the configuration "as code".
Ad-hoc commands are useful for performing quick and simple tasks, such as checking the uptime of a server or installing a package.

Before starting, make sure you **two** up and running Ubuntu instances.

1. In our shared repo, under `ansible_workdir`, create a simple `hosts` Inventory file as follows:

```ini
<host-1-ip>
<host-2-ip>
```

Change `<host-1-ip>` and `<host-2-ip>` to your instances public IP addresses.

We will use the [`ping` module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) to ping our hosts.

> [!NOTE]
> **Ansible modules** are small units of code (written in Python) that perform specific tasks on target systems.
> Examples of modules include those for executing commands, copying files, managing packages, and configuring services.
> Ansible is shipped with hundreds of [built-in modules](https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html) available for usage.


2. Run the below command from the `ansible_workdir` dir. Investigate the returned error and use the `--user` option to fix it.

```shell
ansible -i hosts --private-key /path/to/private-key-pem-file all -m ping
```

As you may see, under the hood, ansible is trying to connect to the machines via SSH connection. 

To disable the SSH authenticity checking, you can configure the following env var:

```bash
export ANSIBLE_HOST_KEY_CHECKING=False
```

3. Let's say the hosts are running a frontend app, we can arrange hosts under groups, and automate tasks for specific group:

```ini
[frontend]
web1 ansible_host=<host-ip-1> ansible_user=<host-ssh-user>
web2 ansible_host=<host-ip-2> ansible_user=<host-ssh-user>
```

There are two more default groups: `all` and `ungrouped`. 
The `all` group contains every host. 
The `ungrouped` group contains all hosts that don’t have another group aside from `all`.

4. Let's check the uptime of all servers listed under the `frontend` group:

```shell
ansible -i hosts --private-key /path/to/private-key-pem-file frontend -m command -a "uptime"
```
