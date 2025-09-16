To access an S3 bucket from an EC2 instance, you need to create an IAM role with the appropriate permissions and attach it to the EC2 instance. 
The role should have policies that grant the necessary permissions to read from and write to the S3 bucket, and the EC2 instance needs to be launched with this IAM role.
IAM role will be taught soon. But for now, just follow the instructions below.

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the navigation pane, choose **Roles**, **Create role**\.

1. On the **Trusted entity type** page, choose **AWS service** and the **EC2** use case\. Choose **Next: Permissions**\.

1. On the **Attach permissions policy** page, search for **AmazonS3FullAccess** AWS managed policy\.

1. On the **Review** page, enter a name for the role and choose **Create role**\.


**To replace an IAM role for an instance**

1. In EC2 navigation pane, choose **Instances**.

1. Select the instance, choose **Actions**, **Security**, **Modify IAM role**.

1. Choose your created IAM role, click **Save**.

## Spot check 

Has the IAM role assignment enabled the instance to communicate with S3 immediately, or is it necessary to stop or reboot the instance for the changes to take effect?

<details>
  <summary>
     Solution
  </summary>
    
No instance stop/reboot is needed!

</details>
