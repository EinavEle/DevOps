# Instructions for course staff to prepare infrastructure for students. 

We want students to practice on EKS clusters. Budget-wise, we can not afford each student to deploy their own EKS. Hence, we create a single cluster in which each student works in their own namespace. 

- Create an EKS cluster named `k8s-main` in `us-east-1`. Create a node group with 2 `medium` instances. Later, students can increase the ng size if needed. 
- Deploy a dashboard using `k8s/k8s_dashboard.yaml` in the shared repo (this dashboard allows anonymous access).
- Deploy Nginx ingress controller as done in class.
- Check if there is a registered domain in Route53 named `atech-bot.click`. Students should create a subdomain alias record and point it to the NLB associated with the Nginx ingress controller. This domain will be used as the Common Name in the self signed certificate when configuring TLS for their Ingress. If you don't find any such domain in Route53, just register a cheap public domain.
-  EKS limits the number of Pods per EC2 instance type (because the VPC CNI plugin assigns ENI for each pod in the instance). For `medium` size instances, it's only 17 pods per instance, which cause students waste a lot of idle compute resources. To increase this limit:
    - Create a new launch template, use the existed LT (the one created for your node group, it should start with `eks-....`) as a **source** for your new LT.
    - In your LT, in User Data, change `--max-pods` to 110 (the maximum allowed value in k8s).
    - Save your launch template and create a **new** node group based on your launch template. Delete the node group based on the old LT.
    - Execute the following command: 
  
      ```bash
      kubectl set env daemonset aws-node -n kube-system ENABLE_PREFIX_DELEGATION=true
      ```

      Make sure the cluster can now run more than 17 Pods per node.


**Don't forget to cleanup the cluster when done.**