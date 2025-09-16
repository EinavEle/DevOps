
Kubernetes is shipped by [many different distributions](https://nubenetes.com/matrix-table/#), each aimed for a specific purpose.
Throughout this tutorial we will be working with Elastic Kubernetes Service (EKS), which is a Kubernetes cluster managed by AWS.  

## Elastic Kubernetes Service (EKS)

> ### Attention!
> This tutorial let you feel how a production ready Kubernetes cluster can be easily provisioned using EKS, but since this resource is quite expensive, **you should delete your EKS clusters after creation**. 
> 

To provision an EKS cluster using the AWS Management Console, follow the below docs:   
https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html

Cluster provisioning takes several minutes.

Upon successful creation, configure `kubectl` to communicate with your cluster by adding a new context to the `kubeconfig` file.

```shell
aws eks --region <region> update-kubeconfig --name <cluster_name>
```

Change `<region>` and `<cluster_name>` accordingly.
