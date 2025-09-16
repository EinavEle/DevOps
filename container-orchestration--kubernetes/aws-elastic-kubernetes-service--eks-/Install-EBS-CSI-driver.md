
The [EBS CSI driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) allows you to create and manage EBS volumes as storage for the Kubernetes Volumes that you create. 

The Amazon EBS CSI plugin requires IAM permissions to make calls to AWS APIs on your behalf. For more information, see [Creating the Amazon EBS CSI driver IAM role](https://docs.aws.amazon.com/eks/latest/userguide/csi-iam-role.html).

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters
2. In the left navigation pane, choose **Clusters**.
3. Choose the name of the cluster that you want to configure the Amazon EBS CSI add-on for.
4. Choose the **Add-ons** tab.
5. Choose **Get more add-ons**.
6. On the **Select add-ons** page, do the following:

    - In the **Amazon EKS-addons** section, select the **Amazon EBS CSI Driver** check box.
    - Choose **Next**.
7. On the **Configure selected add-ons settings** page, select the name of an **IAM role** that you attached the Amazon EBS CSI driver IAM policy.
8. On the **Review and add** page, choose **Create**. 
