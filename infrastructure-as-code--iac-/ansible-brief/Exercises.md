
### Exercise 1 -  Nginx Logs rotation 

In this exercise, we perform log rotation for Nginx using the `logrotate` tool.

- Add task that installs the latest version of `logrotate` on your hosts.
- Using the `ansible.builtin.template` module, create a task that copies the below template file into `/etc/logrotate.d/nginx`:

```text
/var/log/nginx/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 0640 www-data adm  # Changes NGINX log permissions
    sharedscripts
    postrotate
{% if ansible_facts['os_family'] == "Debian" %}
        if [ -f /var/run/nginx.pid ]; then
            kill -USR1 $(cat /var/run/nginx.pid)
        fi
{% else %}
        nginx -s reopen
{% endif %}
    endscript
}
```

- You can start the log rotation job by `logrotate -f /etc/logrotate.d/nginx`. Use the `ansible.builtin.command` module to execute this command on your hosts (once the configuration file has been copied).

Apply the playbook, make sure Nginx rotates logs file properly. 


### Exercise 2 -  Dynamic inventory

Follow:    
https://docs.ansible.com/ansible/latest/plugins/inventory.html#inventory-plugins

