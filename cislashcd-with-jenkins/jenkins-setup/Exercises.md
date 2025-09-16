
### Exercise 1 - Install Jenkins plugins

The Jenkins community plugins are extensions that enhance the functionality of the Jenkins automation server. 

In the **Dashboard** page, choose **Manage Jenkins**, then **Manage Plugins**. In the **Available** tab, search and install:

- **Blue Ocean**
- **Docker Pipeline**
- **Configuration as Code**

Then restart jenkins by `http://<ip>:8080/safeRestart`

### Exercise 2 - Custom log recorder

Create [log recorder](https://www.jenkins.io/doc/book/system-administration/viewing-logs/#logs-in-jenkins) that track only INFO logs related to **GitHub webhook**. 

### Exercise 3 - Run Jenkins using Docker

Launch the Jenkins server in a docker container.

You may utilize the Jenkins [docker official docs](https://www.jenkins.io/doc/book/installing/docker/)
