
### Configure a target group

Configuring a target group allows you to register targets such as EC2 instances\.

1. Open the Amazon EC2 console at [https://console\.aws\.amazon\.com/ec2/](https://console.aws.amazon.com/ec2/)\.

2. In the left navigation pane, under **Load Balancing**, choose **Target Groups**\.

3. Choose **Create target group**\.

4. In the **Basic configuration** section, set the following parameters:

    1. For **Choose a target type**, select **Instance** to specify targets by instance ID

    2. For **Target group name**, enter a name for the target group\.

    3. Leave the **Port** and **Protocol** as HTTP 8080.

    4. For VPC, select your virtual private cloud \(VPC\)

    5. For **Protocol version**, select **HTTP1**.

5. In the **Health checks** section, modify the default settings as needed to perform a health checks to the Flask webserver at endpoint `/status` (In our shared repo, `simple_flask_webserver/app.py`)\.

6. Choose **Next**\.
7. In the **Register targets** page, add one or more targets by selecting one or more instances, enter one or more ports, and then choose **Include as pending below**\.
8. Choose **Create target group**\.

### Configure a load balancer and a listener

To create an Application Load Balancer, you must first provide basic configuration information for your load balancer, such as a name, scheme, and IP address type\.
Then, you provide information about your network, and one or more listeners\.
A listener is a process that checks for connection requests\. It is configured with a protocol and a port for connections from clients to the load balancer\.

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**\.

2. Choose **Create Load Balancer**\.

3. Under **Application Load Balancer**, choose **Create**\.

4. **Basic configuration**

    1. For **Load balancer name**, enter a name for your load balancer\.

    2. For **Scheme**, choose **Internet\-facing**.
       An internet\-facing load balancer routes requests from clients to targets over the internet\.

    3. For **IP address type**, choose **IPv4**.

5. **Network mapping**

    1. For **VPC**, select the VPC that you used for your EC2 instances\. As you selected **Internet\-facing** for **Scheme**, only VPCs with an internet gateway are available for selection\.

    1. For **Mappings**, select two or more Availability Zones and corresponding subnets\. Enabling multiple Availability Zones increases the fault tolerance of your applications\.

6. For **Security groups**, select an existing security group, or create a new one\.

   The security group for your load balancer must allow it to communicate with registered targets on both the listener port and the health check port\. The console can create a security group for your load balancer on your behalf with rules that allow this communication\. You can also create a security group and select it instead\. See [recommended rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html#security-group-recommended-rules)

7. For Listeners and routing, the default listener accepts HTTP traffic on port 80. Choose different ones port according to your app. For Default action, choose the target group that you created.
9. Review your configuration, and choose **Create load balancer**\. A few default attributes are applied to your load balancer during creation\. You can view and edit them after creating the load balancer\. For more information, see [Load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes)\.

