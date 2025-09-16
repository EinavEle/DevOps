
In this section we are going to create a role which can start/stop EC2 instances belong to Development environment only.

1. In IAM console, **Roles** page, create a new role with **AWS account** trusted entity type.
2. According to the policy described in [Controlling access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources), create an inline policy for your role, that allows the principal assumed this role to start/stop EC2 instances that was tagged
   with key `Env` and value `Dev`.
3. Save the role.
4. Tag some of your EC2 instance with `Env=Dev`.
5. Now we would like to switch our AWS IAM user to assume the created role. 
   1. In the IAM console, choose your user name on the navigation bar in the upper right\. It typically looks like this: ***username*@*account\_ID\_number\_or\_alias***\.
   2. Choose **Switch Role**
   3. On the **Switch Role** page, type the account ID number and the role.
6. Test your policy by trying to start/stop EC2 instances with/without appropriate `Env` tag.
7. Switch back to your IAM user. 