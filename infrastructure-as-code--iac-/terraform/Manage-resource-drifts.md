The `terraform.tfstate` file is a record of all resources Terraform manages.
You should not make manual changes to resources controlled by Terraform, because the state file will be out of sync, or "drift," from the real infrastructure.
By default, Terraform compares your state file to real infrastructure whenever you invoke `terraform plan` or `terraform apply`.

If you suspect that your infrastructure configuration has changed outside of the Terraform workflow, you can use a `-refresh-only` flag to inspect what the changes to your state file would be.

1. Run `terraform plan -refresh-only` to determine the drift between your current state file and actual configuration.    
   You should be synced: `No changes. Your infrastructure still matches the configuration.`
2. In the AWS Console, **manually** create a new security group within the `module.app_vpc` VPC (allow TCP access on port 22 for all IP addresses), attach this security group to `aws_instance.app_server` EC2 instance.
3. Run `terraform plan -refresh-only` again. As shown in the output, Terraform has detected differences between the infrastructure and the current state, and sees that your EC2 instance has a new security group attached to it.
4. Apply these changes by `terraform apply -refresh-only` to make your state file match your real infrastructure (**your `.tf` configuration file would not be updated accordingly, they remain un-synced**).

A refresh-only operation does not attempt to modify your infrastructure to match your Terraform configuration -- it only gives you the option to review and track the drift in your state file.
If you ran `terraform plan` or `terraform apply` without the `-refresh-only` flag now, Terraform would attempt to revert your manual changes.

Now, you will update your configuration to associate your EC2 instance with both security groups.

1. First, add the resource definition to your configuration by:

   ```terraform
   resource "aws_security_group" "sg_ssh" {
    name = "<your-security-group-name>"
    description = "<your-security-group-description>"
    vpc_id      = module.app_vpc.vpc_id
   
    ingress {
        from_port   = "22"
        to_port     = "22"
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
   }
   ```

   Make sure `<your-security-group-name>` is the same as your manually created security group.
2. Add the security group ID to your instance resource.

   ```text
   - vpc_security_group_ids = [aws_security_group.sg_ssh.id]
   + vpc_security_group_ids = [aws_security_group.sg_ssh.id, aws_security_group.sg_web.id]
   ```

3. Run `terraform import` to associate your resource definition with the security group created in the AWS Console:

   ```text
   terraform import aws_security_group.sg_ssh <sg-id>
   ```
   
   Where `<sg-id>` is your security group id.

