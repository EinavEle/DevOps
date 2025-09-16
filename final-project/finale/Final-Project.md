# Final Project 

The final project can be done in 2-3 groups.

## Project objective

Your objective is to design and implement a comprehensive CI/CD pipeline for a service deployed in a microservices architecture within Kubernetes.

## Guidelines

- You can use the Python service used during the course, or come up with your own application.
- The service should be composed by different microservices:
  - Frontend (customer facing) microservice.
  - Database (you can use DB managed by AWS).
  - Some background microservices. 
- Communication between microservices should be both **synchronous** (using HTTP request/response) and **asynchronous** (using queues or topics). 
- The service will be deployed in k8s.
- You should implement full CI/CD pipeline (build, test, deploy) for both **Development** and **Production** environment. You are free to choose any CI server you wish (Jenkins, GitHub actions, etc...) 
- All microservices code, configuration files and pipelines definition should be stored in a single Git repo in GitHub. You should strive to follow IaC practices as much as you can.  
- You should use AWS services as infrastructure. You are highly encouraged to provision the infrastructure in AWS using IaC tool (like Terraform and CloudFormation), and automated it using your CI server. 
- The service should be monitored by Kibana/Grafana. Collect metrics and logs from any microservice and create/import nice dashboards.  
- You are highly encouraged to develop/extend the service with some tool that was not taught during the course (see tools bazaar below).

## Project evaluation criteria 

Your projects would be evaluated according to the below list, in order of priority:

1. Showcasing a **live**, **working** demo of your work.
2. Applying DevOps practics - containerized applications, deployed to k8s, full CI/CD pipeline in multiple envs, IaC for cloud resources.
3. Demonstrating deep understanding of your system.
4. Successful integration of a new tool, idea, or extension within the DevOps workflow (see ideas below). Be creative!
5. Project complexity. E.g. security measures, scalability, zero-downtime, cost-efficient architecture.

# DevOps Tools Bazaar

- [safety](https://pyup.io/safety/) to scan vulnerabilities in Python packages.
- [Bandit](https://bandit.readthedocs.io/en/latest/) to find security issues in your Python code.
- [Pre-commit](https://pre-commit.com/) to enforce some policy before committing a new code.
- [Black](https://github.com/psf/black) as a linting tool.
- [Chef InSpec](https://docs.chef.io/inspec/) to apply security and compliance policies.
- [Argo CD](https://argoproj.github.io/argo-cd/) to improve the continuous deployment in Kubernetes. 
- [Vault](https://www.vaultproject.io/docs) to store secrets.
- [Nexus](https://help.sonatype.com/repomanager3) to manage and store artifacts.
- [Argo Workflow](https://argoproj.github.io/argo/) to build pipelines in Kubernetes.
- [Prometheus Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) to create an alerting system.
- [KEDA](https://keda.sh/docs/) to configure an even driven autoscaling in Kubernetes.
- [Istio](https://istio.io/latest/docs/) to create service mesh in Kubernetes. 
- [Calico](https://docs.projectcalico.org/) to enforce network policies in Kubernetes.
- [SonarQube](https://docs.sonarqube.org/) to find security vulnerabilities in your artifacts.
- [Karpenter](https://karpenter.sh/) for better node autoscaling in EKS. 

## Submission 

Deliver a 35-minute demo to the class showcasing your work (30 minutes for presenting, 5 minutes for questions).

- Ensure that your presentation includes a live and functioning demonstration of your project. 
- Begin your presentation by providing an overview of the system at a high level, and then progressively dive into the finer details.
- Highlight your use of DevOps practices.
- Demonstrate a deep understanding of your system by explaining the architecture, design choices, and technical components clearly and comprehensively. Be prepared to answer questions about your project.
- Discuss some complex topic of your project.