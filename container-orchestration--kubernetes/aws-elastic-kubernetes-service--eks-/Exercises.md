### Exercise 1 - Karpenter

Karpenter is a flexible, high-performance Kubernetes cluster autoscaler that helps improve application availability and cluster efficiency. 
Karpenter launches right-sized compute resources in response to changing application load. This option can provision just-in-time compute resources that meet the requirements of your workload.

Follow the getting started guide:    
https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/

### Exercise 2 - EKS Pod Identities

EKS Pod Identities provide the ability to manage credentials for your applications, similar to the way that you assign IAM role to EC2 instances.
Instead of creating and distributing your AWS credentials to the containers or using the Node's role, you associate an IAM role with a Kubernetes service account and configure your Pods to use the service account.

Follow:    
https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html

### Exercise 3 - S3 CSI driver 

With the [Mountpoint for Amazon S3 Container Storage Interface (CSI) driver](https://github.com/awslabs/mountpoint-s3-csi-driver), your Kubernetes applications can access S3 objects through a file system interface
The CSI driver presents an Amazon S3 bucket as a volume.

Follow:     
https://docs.aws.amazon.com/eks/latest/userguide/s3-csi.html


