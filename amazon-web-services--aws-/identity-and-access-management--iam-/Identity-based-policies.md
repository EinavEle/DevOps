
Identity-based policies are attached to an IAM user, group, or role. These policies let you specify what that identity can do (its permissions).

Throughout this unit, we will create different policies and associate them with the role you've created in the previous unit. 

If you haven't created a role yet, here is a short recap.

# Create IAM role with permissions over S3 and attach it to an EC2 instance

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

2. In the navigation pane, choose **Roles**, **Create role**\.

3. On the **Trusted entity type** page, choose **AWS service** and the **EC2** use case\. Choose **Next: Permissions**\.

4. On the **Attach permissions policy** page, search for **AmazonS3FullAccess** AWS managed policy\.

5. On the **Review** page, enter a name for the role and choose **Create role**\.
6. Attach the role to your EC2 instance. 
7. Test your policy.