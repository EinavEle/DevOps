
Enforcing tagging policies for resources in AWS is considered a good practice. 
By enforcing a tagging policy, you can ensure that all resources are consistently labeled and organized, which makes it easier to identify, search, and manage resources and costs.

For example, you can use tags to label resources based on their project and environment. This can help you to quickly find and manage resources, monitor costs, and set up automation and policies based on tags.

1. We now want to force a tagging policy in our AWS account. We want all EC2 instances to be tagged with a key `Project` with allowed values of `CloudMate`, `PipelineX`, or `SecureStack` (three imagined project names).
2. According to the policy described in [Controlling access during AWS requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-requests), add a statement to the above inline policy, that enforces the tagging policy for EC2 instances belonging to different projects. 
3. Switch to your role and test your policy. 

