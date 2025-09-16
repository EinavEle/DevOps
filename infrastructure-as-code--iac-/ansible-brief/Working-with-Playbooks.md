
If you need to execute a task more than once, you should write a **Playbook** and put it under some source control (e.g. Git repo).
Ansible Playbooks offer a repeatable, re-usable and simple configuration management.

Playbooks are expressed in YAML format, composed of one or more "plays" in an **ordered** list.
A playbook "play" runs one or more tasks.

Let's create a task that verifies the installation of `nginx` (and install it if needed).

1. Create the following `site.yaml` file, representing an Ansible playbook:
2. 
```yaml
- name: Frontend servers
  hosts: frontend
  tasks:
    - name: Ensure nginx is at the latest version
      ansible.builtin.apt:
        name: nginx
        state: latest
```

In the above example, [`ansible.builtin.apt`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) is the module being used, `name` and `state` are module's parameters. 

2. Apply your playbook using the following `ansible-playbook` command.

```shell
ansible-playbook -i hosts --private-key /path/to/private-key-pem-file site.yaml
```

As the tasks in this playbook require `root` privileges, we add the `become: yes` to enable execute tasks as a different Linux user. We also use [variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#using-variables) to make the playbook more modular:

```yaml
- name: Frontend servers
  hosts: frontend
  become: yes
  vars:
    nginx_major_version: 1
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: "nginx={{ nginx_major_version }}.*"
        state: present
        update_cache: yes
```

Run the playbook again and make sure the task has been completed successfully.

We now want to modify our Nginx server configurations.

3. Add the following task to your playbook:

```yaml
- name: Frontend servers
  hosts: frontend
  become: yes
  vars:
    nginx_major_version: 1
  vars_files:
    - vars/nginx-custom-vars.yaml
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: "nginx={{ nginx_major_version }}.*"
        state: present
        update_cache: yes
          
    - name: Create a the server static files directory if it does not exist
      ansible.builtin.file:
        path: "{{ document_root }}"
        state: directory
        mode: '0755'
       
    - name: Copy custom index.html file
      ansible.builtin.template:
        src: index.html.j2
        dest: "{{ document_root }}/index.html"

    - name: Copy Nginx server template
      ansible.builtin.template:
        src: custom.conf.j2
        dest: /etc/nginx/conf.d/custom.conf
```

Ansible uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templating tool to copy files to hosts, while enable dynamic expressions according to the defined [variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#playbooks-variables).
The `templates/custom.conf.j2` and its corresponding variable file `vars/nginx-custom-vars.yaml` can be found in our shared repo.

4. Run the playbook. Connect to one of the hosts and make sure the configurations has been applied. Try to visit the server using one of the machine's public IP (don't forget to open the relevant port in the instance's security group).
5. For the new Nginx configs to be applied, it's required to restart the `nginx` service. Let's add a [Handler](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_handlers.html#handlers) that restarts the daemon after a successful configuration change:

```yaml
- name: Frontend servers
  hosts: frontend
  become: yes
  vars:
    nginx_major_version: 1
  vars_files:
    - vars/nginx-custom-vars.yaml
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: "nginx={{ nginx_major_version }}.*"
        state: present
        update_cache: yes
          
    - name: Create a the server static files directory if it does not exist
      ansible.builtin.file:
        path: "{{ document_root }}"
        state: directory
        mode: '0755'
       
    - name: Copy custom index.html file
      ansible.builtin.template:
        src: index.html.j2
        dest: "{{ document_root }}/index.html"

    - name: Copy Nginx server template
      ansible.builtin.template:
        src: custom.conf.j2
        dest: /etc/nginx/conf.d/custom.conf
        
      notify:
        - Restart Nginx

  handlers:
    - name: Restart Nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

7. Run the playbook and manually check the status of the `nginx` service in one of the hosts.

> #### Try it yourself
> 
> Change the server's port number to a value other than `8080`, apply the playbook and make sure the configurations have been applied. 

### Validating playbook tasks: `check` mode and `diff` mode

Ansible provides two modes of execution that validate tasks: **check** mode and **diff** mode.
They are useful when you are creating or editing a playbook, and you want to know what it will do.

- In `check` mode, Ansible runs without making any changes on remote systems, and report the changes that would have made.
- In `diff` mode, Ansible provides before-and-after comparisons.

Simply add the `--check` or `--diff` options (both or separated) to the `ansible-playbook` command:

```shell
ansible-playbook -i hosts --private-key /path/to/private-key-pem-file site.yaml --check --diff 
```
