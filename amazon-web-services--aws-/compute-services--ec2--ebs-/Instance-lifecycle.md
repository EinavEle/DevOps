
When you stop an instance, AWS shut it down. They don't charge usage for a stopped instance, or data transfer fees, but do charge for the storage for any Amazon EBS volumes.

Each time you start a stopped instance, you are charged with a minimum of one minute for usage.
After one minute, AWS charge only for the **seconds** you use.

For example, if you run an instance for 20 seconds and then stop it, AWS charges for a full one minute.
If you run an instance for 3 minutes and 40 seconds, you are charged for exactly 3 minutes and 40 seconds of usage.

If you decide that you no longer need an instance, you can **terminate** it.


## Stop your instance

1. In the navigation pane, choose **Instances** and select the instance\.

1. Choose **Instance state**, **Stop instance**\. If this option is disabled, either the instance is already stopped or its root device is an instance store volume\.

1. When prompted for confirmation, choose **Stop**\. It can take a few minutes for the instance to stop\.

1. \(Optional\) While your instance is stopped, you can modify certain instance attributes\. For more information, see [modify\-stopped\-instance](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html)\.

1. To start the stopped instance, select the instance, and choose **Instance state**, **Start instance**\.

1. It can take a few minutes for the instance to enter the `running` state\.
