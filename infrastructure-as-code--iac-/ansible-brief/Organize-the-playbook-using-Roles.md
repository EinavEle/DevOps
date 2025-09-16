
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html) are collection of tasks, files, templates, variables and other Ansible artifacts that are organized in a structured way to perform a specific function.
Roles are used to create reusable and modular code, making it easier to manage complex configurations and deployments.

Rearrange your `ansible_workdir` dir according to the following files structure:

```text
ansible_workdir/
└── roles/
    └── nginx/
        ├── tasks/
        │   └── main.yaml
        ├── handlers/
        │   └── main.yaml
        ├── templates/
        │   ├── custom.conf.j2
        │   └── index.html.j2
        └── vars/
            └── main.yaml
```

- In `tasks/main.yaml`, copy the tasks (the content under the `tasks:` entry in the original `site.yaml` file).
- In `handlers/main.yaml` copy the handlers.
- Copy the content of `vars/nginx-custom-vars.yaml` into `vars/main.yaml`.

By default, Ansible will look in each directory within a role for a `main.yaml` file for configurations to apply.

Create a `site.yaml` file with the following content:

```yaml
---
- name: Frontend servers
  hosts: frontend
  become: yes
  roles:
    - nginx
  tasks:
    # ...
```

Ansible will execute roles first, then other tasks in the play.

Apply your playbook. Make sure it works properly. 
