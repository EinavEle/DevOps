### Installing `kubectl`

`kubectl` is a command-line tool used to interact with Kubernetes clusters.

Download and install the `kubectl` binary from [Kubernetes](https://kubernetes.io/docs/tasks/tools/#kubectl) official site.


Make sure `kubectl` successfully communicates with your cluster:

```console
$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   10h   v1.27.4
```

The tutorial was written for Kubernetes version >= v1.27.

### Enable k8s dashboard 

The k8s dashboard is a web-based user interface.
You can use the dashboard to troubleshoot your application, and manage the cluster resources.

To enable the k8s dashboard in minikube, perform:

```bash
minikube dashboard --port 30001
```

This command occupies the terminal, allowing you to access the dashboard from your local machine. The dashboard url will be printed to stdout. 

> Note:   
> If you run minikube on a remote machine, in order to access the dashboard, make sure to forward port 30001 when connecting over ssh:
> 
> ```bash
> ssh -i <pem-file> -L 30001:localhost:30001 ubuntu@<ip>
> ```

