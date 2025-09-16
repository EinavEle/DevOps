### Exercise 1 -  Connect to minikube node using ssh 

This short exercise demonstrates and stresses the fact that k8s is just **containers orchestrator**,
and under the hood, there are nothing but running docker containers in each cluster's node. 

In real k8s cluster, nodes are usually virtual machines, like EC2 instances.
But in Minikube node are virtualized within the machine minikube is running on. 
Nevertheless, minikube nodes have an IP address, and you can connect them via ssh as if you are connecting to a real server. 

Connect to one of your cluster's nodes using the `ssh` command (don't use the `minikube ssh` utility):

- The cluster name (profile name) and node IP can be found in `minikube profile list`.
- The username is `docker`.
- The private key identity file can be found in `~/.minikube/machines/<CLUSTER_NAME>/id_rsa`.

Inside the node, use `docker` command to list the running containers on that node. 
Can you recognize the containers running the Online Boutique app?

### Exercise 2 - Provision multi-node cluster with Minikube 

Start a new minikube cluster named `multinode-demo` with 2 **worker** nodes. 

- Make sure there are two worker nodes and one control plane node in the cluster. 
- Observing the kubeconfig file, what is the API's server IP of the cluster?
- Delete the cluster at the end. How does the kubeconfig look like after the deletion? 

These commands might help:

```bash 
minikube stop
kubectl get nodes
minikube status -p multinode-demo
minikube profile list
```

### Exercise 3 -  Minikube addons 

Minikube includes a set of built-in addons that can be enabled, disabled and opened in the local Kubernetes environment.

List the currently supported addons:

```bash
minikube addons list
```

Enable an addon, the `metrics-server` addon:

```bash
minikube addons enable metrics-server
```

[Metrics Server](https://github.com/kubernetes-sigs/metrics-server) is an application (running in a container within your cluster) that collects metrics (e.g. Pod CPU and Memory utilization) from the cluster node and exposes them in Kubernetes apiserver.

To be able to pull images from an ECR repository, [configure credentials for ECR using `registry-creds` addon](https://minikube.sigs.k8s.io/docs/tutorials/configuring_creds_for_aws_ecr/).

### Exercise 4 -  Working with `kubectl` against multiple clusters

Utilize [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) throughout this exercise. 

1. Start a new Minikube cluster name `minikube-dev` with Kubernetes version `v1.22.0`.
1. Start a new Minikube cluster name `minikube-prod` with Kubernetes version `v1.27.0`.
1. Set up the autocomplete functionality for `kubectl`. 
1. Take a look on the kubeconfig file by `kubectl config view`. Make sure you have at least 2 available clusters.
1. List your kubeconfig contexts
1. Switch to work with `minikube-dev` cluster, `describe` your cluster nodes. 
1. Switch to work with `minikube-prod` cluster, `describe` your cluster nodes. 


### Exercise 5 -  The `kubectl proxy` command and k8s dashboard

The **Kubernetes Dashboard** we've seen during the tutorial is itself an web application running on your cluster.
You can see the dashboard's Pods in the `kubernetes-dashboard` namespace:

```bash
kubectl get pods -n kubernetes-dashboard
```

Follow the [tutorial](https://kubernetes.io/docs/tasks/extend-kubernetes/http-proxy-access-api/) from k8s docs.
Then try to visit the k8s dashboard using `kubectl proxy` command. Make sure the `minikube dashboard` is not running.

### Exercise 6 -  Working with kubeconfig files

Follow:    
https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/


### Exercise 7 -  Access minikube cluster from remote machine using Nginx reverse proxy

To be done in Minikube running on an EC2 instance. 

By design, minikube create k8s cluster with which you can communicate only from within the machine the cluster is running on. 
If you want to communicate with your cluster (i.e. running `kubectl` commands) from a remote machine, you should use expose the cluster's API server using method like reverse proxy. 

In this exercise we will expose your cluster using an Nginx reverse proxy.

<img src=".guides/img/minikube-remote.png" width="50%">

Start a minikube cluster by `minikube start -p test-cluster`.

Get the kubeconfig content:

```bash 
kubectl config view
```

Under `users` entry, indicate the user used to connect to `test-cluster` and copy its `client-certificate` and `client-key` files to some directory on the minikube host machine.

Create a directory in which the Nginx server configuration file would be located:

```bash 
sudo mkdir -p /etc/nginx/conf.d/
```

Inside the directory, create the following `minikube.conf` file:

```text
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;  
    
    location / {   
        proxy_pass https://MINIKUBE_IP:8443;
        proxy_ssl_certificate /etc/nginx/certs/minikube-client.crt;
        proxy_ssl_certificate_key /etc/nginx/certs/minikube-client.key;
    }
}
```

From the minikube host machine, launch a (containerized) Nginx server:

```bash

docker run -d --name nginx -p 8080:80 -v MINIKUBE_CLIENT_KEY_PATH:/etc/nginx/certs/minikube-client.key -v MINIKUBE_CLIENT_CERT_PATH:/nginx/certs/minikube-client.crt -v /etc/nginx/conf.d/:/etc/nginx/conf.d nginx
```

Use again the `kubectl config view` command to create a `custom-kubeconfig.yaml` file **in your local machine**. 
Change the `server:` entry to the `http://<INSTANCE_IP>:80`, as well as other entries related to authentication. 

At the end, communicate with the minikube cluster form your local machine:

```bash
kubectl get pods --kubeconfig custom-kubeconfig.yaml
```