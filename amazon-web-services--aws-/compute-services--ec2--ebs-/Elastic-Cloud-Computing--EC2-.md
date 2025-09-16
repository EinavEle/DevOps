Amazon EC2 (Elastic Compute Cloud) is a web service that provides resizable compute capacity in the cloud.
It allows users to create and manage virtual machines, commonly referred to as "instances", which can be launched in a matter of minutes and configured with custom hardware, network settings, and operating systems.


## Launch a virtual machine (EC2 instance)

1. Open the Amazon EC2 console at [https://console\.aws\.amazon\.com/ec2/](https://console.aws.amazon.com/ec2/).
2. From the EC2 console dashboard, in the **Launch instance** box, choose **Launch instance**, and then choose **Launch instance** from the options that appear\.
3. Under **Name and tags**, for **Name**, enter a descriptive name for your instance\.
4. Under **Application and OS Images \(Amazon Machine Image\)**, do the following:

   1. Choose **Quick Start**, and then choose **Ubuntu**\. This is the operating system \(OS\) for your instance\.

5. Under **Instance type**, from the **Instance type** list, you can select the hardware configuration for your instance\. Choose the `t2.micro` instance type, which is selected by default. In Regions where `t2.micro` is unavailable, you can use a `t3.micro` instance.

6. Under **Key pair \(login\)**, choose **create new key pair** the key pair that you created when getting set up\.

   1. For **Name**, enter a descriptive name for the key pair\. Amazon EC2 associates the public key with the name that you specify as the key name\.

   2. For **Key pair type**, choose either **RSA**.

   3. For **Private key file format**, choose the format in which to save the private key\. Since we will use `ssh` to connect to the machine, choose **pem**.

   4. Choose **Create key pair**\.

   **Important**  
   This step should be done once! once you've created a key-pair, use it for every EC2 instance you are launching.

   5. The private key file is automatically downloaded by your browser\. The base file name is the name you specified as the name of your key pair, and the file name extension is determined by the file format you chose\. Save the private key file in a **safe place**\.

      **Important**  
      This is the only chance for you to save the private key file\.

   6. Your private key file has to have permission of `400`, `chmod` it if needed.

7. Keep the default selections for the other configuration settings for your instance\.

8. Review a summary of your instance configuration in the **Summary** panel, and when you're ready, choose **Launch instance**\.

9. A confirmation page lets you know that your instance is launching\. Choose **View all instances** to close the confirmation page and return to the console\.

10. On the **Instances** screen, you can view the status of the launch\. It takes a short time for an instance to launch\. When you launch an instance, its initial state is `pending`\. After the instance starts, its state changes to `running` and it receives a public DNS name\.

11. It can take a few minutes for the instance to be ready for you to connect to it\. Check that your instance has passed its status checks; you can view this information in the **Status check** column\.

## Connect to your instance

Open the terminal in your local machine, and connect to your instance by:

```shell
ssh -i "</path/key-pair-name.pem>" ubuntu@<instance-public-dns-name-or-ip>
```