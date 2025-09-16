
### Exercise 1 - Execute your pipelines in a container in a Jenkins agent

Complete the above work to configure the `build.Jenkinsfile`, `deploy.Jenkinsfile` and `pr-testing.Jenkinsfile` pipelines to be running on the Jenkins agent, in a Docker container.

Notes:

- As the `pr-testing.Jenkinsfile` require Python as part of the pipeline execution, you have to re-build the agent docker image with Python in it. You are highly encouraged to use another "installer" image to create Python virtual environment (`venv`) within the image, and then to copy the created `venv` to the `jenkins/agent` image.
- You have to [install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) on the agent docker image.


### Exercise 2 - Autoscale the EC2 inatance agents nodes

Jenkins [EC2-plugin](https://plugins.jenkins.io/ec2/) allows Jenkins to start agents on EC2 on demand, and kill them as they get unused.
It'll start instances using the EC2 API and automatically connect them as Jenkins agents. When the load goes down, excess EC2 instances will be terminated.

1. Install the `Amazon EC2` Jenkins plugin. 
2. Once installed, navigate to the main **Manage Jenkins** > **Nodes and Clouds** page, and choose **Configure Clouds**.
3. Add an **Amazon EC2** cloud and configure it.
4. Test your configured "cloud" with some of your pipelines.

### Exercise 3 - Jenkins on k8s with agents as Pods

In this exercise, you will set up Jenkins on a Kubernetes cluster using Helm and configure Jenkins agents as pods to dynamically provision build environments.

1. [Install Jenkins](https://artifacthub.io/packages/helm/jenkinsci/jenkins) on your Kubernetes cluster using Helm.
2. Configure the [Kubernetes Plugin](https://plugins.jenkins.io/kubernetes/) in Jenkins to enable agent provisioning on the Kubernetes cluster.
3. Test the systems by running some pipeline. 