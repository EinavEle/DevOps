
You can retrieve or discover information (known as **Facts**) about your remote systems. 

For example, with facts variables you can use the IP address of a machine as a configuration value on another system. 
Or you can perform tasks based on the specific host OS.

Let's run the `setup` ad-hoc command to print all facts ansible collects on a given host:

```shell
ansible -i hosts --private-key /path/to/private-key-pem-file frontend -m setup
```

Let's assume your `frontend` group contains both Ubuntu and RedHat servers. 
In such case, the usage of `ansible.builtin.apt` module doesn't fit the RedHat family servers.

We would like to add a condition for this task to use the appropriate package manager based on the OS:

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
      when: ansible_facts['pkg_mgr'] == 'apt'
        
    - name: Ensure nginx is installed
      ansible.builtin.yum:
        name: "nginx={{ nginx_major_version }}.*"
        state: present
      when: ansible_facts['pkg_mgr'] == 'yum'
          
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
