Like the Linux OS, Kubernetes (or shortly, k8s) is shipped by [many different distributions](https://nubenetes.com/matrix-table/#), each aimed for a specific purpose.
Throughout this course we will be working with [Minikube](https://minikube.sigs.k8s.io/docs/), and later, with [Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/), which is a Kubernetes cluster managed by AWS.  

## Installing Minikube 

Minikube is a lightweight and single-node Kubernetes distribution that is primarily used for local development and learning.

Minikube is one of the preferred [learning tools](https://kubernetes.io/docs/tasks/tools/) in Kubernetes official documentation.  

Follow the [Get Started!](https://minikube.sigs.k8s.io/docs/start/) page in minikube docs to install it on your local machine. 
Your minikube cluster relies upon some virtualization platform, we will be using Docker as the minikube driver (install Docker if needed). 

> Note:    
> If your machine isn't strong enough to run minikube, you can run it on an `medium` Ubuntu EC2 instance with 30GB disk.   

You can start the cluster by:

```bash
minikube start --driver docker
```
