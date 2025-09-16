
AWS operates state-of-the-art, highly available data centers. Although rare, failures can occur that affect the availability of instances that are in the same location. If you host all of your instances in a single location that is affected by a failure, none of your instances would be available.

Each **Region** is designed to be isolated from the other Regions. This achieves the greatest possible **fault tolerance** and **stability**.

Here are a few available regions of AWS:

| Code      | Name |
| ----------- | ----------- |
| us-east-2      | US East (Ohio)       |
| us-east-1   | US East (N. Virginia)        |
| us-west-1    | US West (N. California)        |
| us-west-2   | US West (Oregon)        |
| eu-west-1  | 	Europe (Ireland)   |
| eu-central-1  | 	Europe (Frankfurt)   |
| eu-north-1  | 	Europe (Stockholm)   |

Each Region has multiple, isolated locations known as **Availability Zones**. The code for Availability Zone is its Region code followed by a letter identifier. For example, `us-east-1a`.
