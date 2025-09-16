{Check It!|assessment}(multiple-choice-686207805)


Consider the below playbook:

```yaml
- name: deploy app config
  template:
    src: app.xml.j2
    dest: /etc/app.xml
  notify:
    - restart memcached
    - restart apache
    
- name: deploy httpd config
  template:
    src: httpd.conf.j2
    dest: /etc/httpd/conf/httpd.conf
  notify:
    - restart apache

- name: deploy httpd config
  template:
    src: site.conf.j2
    dest: /etc/httpd/conf/site.conf
  notify:
    - restart apache
```

Answer the below 2 questions:



{Check It!|assessment}(multiple-choice-986825428)
{Check It!|assessment}(multiple-choice-666189996)
{Check It!|assessment}(multiple-choice-2583512065)
