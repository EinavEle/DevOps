# Exercise 1 - Talk with AWS using CLI 

In this exercise, you will learn how to interact with the AWS API from your local machine using the AWS CLI (Command Line Interface). 
This will allow you to manage AWS resources and services programmatically, in addition of using the AWS Management Console.

1. Follow AWS's official docs to [install AWS cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) on your Ubuntu machine.  

2. You will then need to create credentials in the **IAM service** and configure them on your local machine before running CLI commands to interact with AWS services.
   1. Use your AWS account ID or account alias, your IAM user name, and your password to sign in to the [IAM console](https://console.aws.amazon.com/iam)\.
   2. In the navigation bar on the upper right, choose your user name, and then choose **Security credentials**\.   
   3. In the **Access keys** section, choose **Create access key**\. If you already have two access keys, this button is deactivated and you must delete an access key before you can create a new one\.
   4. On the **Access key best practices & alternatives** page, choose your use case to learn about additional options which can help you avoid creating a long\-term access key\. If you determine that your use case still requires an access key, choose **Other** and then choose **Next**\.
   5. Set a description tag value for the access key\. This adds a tag key\-value pair to your IAM user\. This can help you identify and rotate access keys later\. The tag key is set to the access key id\. The tag value is set to the access key description that you specify\. When you are finished, choose **Create access key**\.
   6. On the **Retrieve access keys** page, choose either **Show** to reveal the value of your user's secret access key, or **Download \.csv file**\. This is your only opportunity to save your secret access key\. After you've saved your secret access key in a secure location, choose **Done**\.

3. Open a new terminal session on your local machine, and type `aws configure`. Enter the access key id and the access secret key. You can also provide the default region you are working on, and the default output format (`json`). 
4. Test your credentials by executing `aws sts get-caller-identity`. This command returns details about your AWS user, which indicating a successful communication with API cli. 