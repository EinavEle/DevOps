
So far, we've seen Pod horizontal autoscaling (HPA). 
But Kubernetes clusters have actually two levels of scaling - Pod level scaling (done using HPA), and Node level scaling. 

Amazon EKS supports two Node level autoscaling products:

1. [Karpenter](https://karpenter.sh/): Karpenter is a flexible, high-performance Kubernetes cluster autoscaler (see exercise below).
2. [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md):  automatically adjusts the number of nodes using Auto Scaling groups.

**No need to install any tool for now**. Just have them in mind when you deal with node autoscaling.  

