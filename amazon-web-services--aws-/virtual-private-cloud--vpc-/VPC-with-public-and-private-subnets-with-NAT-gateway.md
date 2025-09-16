![.guides/img/vpc2](./vpc2.png)


This architecture is suitable if you want to run a public-facing web application, while maintaining back-end servers that aren't publicly accessible.
A common example is web servers in a public subnet and the database in a private subnet.
You can set up security and routing so that the web servers can communicate with the database servers.

The instances in the public subnet can send outbound traffic directly to the internet, whereas the instances in the private subnet can't.
Instead, the instances in the private subnet can access the internet by using a network address translation (NAT) gateway that resides in the public subnet.
The database can connect to the internet for software updates using the NAT gateway, but the internet cannot establish connections to the database.


The configuration for this scenario includes the following:
+ A VPC with a size /16 IPv4 CIDR block: 10\.0\.0\.0/16\. This provides 65,536 private IPv4 addresses\.
+ A public subnet with a size /24 IPv4 CIDR block: 10\.0\.0\.0/24\. This provides 256 private IPv4 addresses\. A public subnet is a subnet that's associated with a route table that has a route to an internet gateway\.
+ A private subnet with a size /24 IPv4 CIDR block: 10\.0\.1\.0/24\. This provides 256 private IPv4 addresses\.
+ An internet gateway\. This connects the VPC to the internet and to other AWS services\.
+ A NAT gateway with its own Elastic IP address\. Instances in the private subnet can send requests to the internet through the NAT gateway over IPv4 \(for example, for software updates\)\.
+ A custom route table associated with the public subnet\. This route table contains an entry that enables instances in the subnet to communicate with other instances in the VPC, and an entry that enables instances in the subnet to communicate directly with the internet over IPv4\.
+ The main route table associated with the private subnet\. The route table contains an entry that enables instances in the subnet to communicate with other instances in the VPC, and an entry that enables instances in the subnet to communicate with the internet through the NAT gateway.

## Spot check 

Why does the NAT gateway should be located in the public subnet, instead the private one? 


<details>
  <summary>
     Solution
  </summary>
    Because the NAT gateway should access the internet on behalf the instances located in the private subnet. 
</details>


## Create another subnet

As per the above section, create another subnet within your VPC with CIDR block of `10\.0\.1\.0/24`. This subnet should be associated with the main route table.

## Create and attach a NAT gateway

NAT Gateway must be associated with an Elastic IP Address (static IP reservation service of AWS)

## Allocate an Elastic IP Address


1. Open the Amazon EC2 console at [https://console\.aws\.amazon\.com/ec2/](https://console.aws.amazon.com/ec2/)\.

2. In the navigation pane, choose **Network & Security**, **Elastic IPs**\.

3. Choose **Allocate Elastic IP address**\.

4. For **Public IPv4 address pool**, choose **Amazon's pool of IPv4 addresses**

5. Add a **Name** tag\.

6. Choose **Allocate**\.

## Create a NAT Gateway


1. Open the Amazon VPC console at [https://console\.aws\.amazon\.com/vpc/](https://console.aws.amazon.com/vpc/)\.

2. In the navigation pane, choose **NAT Gateways**\.

3. Choose **Create NAT Gateway** and do the following:

    1. Specify a name for the NAT gateway\. This creates a tag where the key is **Name** and the value is the name that you specify\.

    2. Select the subnet in which to create the NAT gateway\.

    3. For **Connectivity type**, select **Public** \(the default\) to create a public NAT gateway\.

    4. For **Elastic IP allocation ID**, select the Elastic IP address to associate with the NAT gateway\.

    5. Choose **Create a NAT Gateway**\.

## Add NAT Gateway as a target in the main route table

1. Select the main route table of your VPC\. The details pane displays tabs for working with its routes, associations, and route propagation\.

2. On the **Routes** tab, choose **Edit routes**, **Add route**, and add the following routes as necessary\. Choose **Save changes** when you're done\.
    + For IPv4 traffic, specify `0.0.0.0/0` in the **Destination** box, and select your NAT gateway ID in the **Target** list\.


**Please delete the NAT gateway when done**

