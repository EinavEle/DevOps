### Deploy single EC2 instance

The set of files used to describe infrastructure in Terraform is known as a **Terraform configuration files** (`.tf`).

Let's provision a single AWS EC2 instance.

1. Edit the configuration file in `tf_workspace/main.tf`. This is a complete configuration that you can deploy with Terraform.
   1. `<aws-region-code>` is the region in which you want to deploy your infrastructure.
   2. `<ec2-ami>` is the AMI you want to provision (choose an Ubuntu AMI according to your region).
   3. `<your-alias>` is the name of you EC2 instance.
   4. `<aws-course-profile>` is the profile account with which your local credentials are associated (the default profile is `default`, otherwise take a look on `~/.aws/credentials`).
2. When you create a new configuration — or check out an existing configuration from version control — you need to initialize the directory contains your `.tf` files with `terraform init`. This directory is known as **Terraform workspace dir**.
   Initializing a configuration directory downloads and installs the providers defined in the configuration, which in this case is the `aws` provider.
3. You can make sure your configuration is syntactically valid and internally consistent by using the `terraform validate` command.
4. Run `terraform plan` to create an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure.
5. Apply the configuration now with the `terraform apply` command.

When you applied your configuration, Terraform wrote data into a file called `terraform.tfstate`. Terraform stores the IDs and properties of the resources it manages in this file, so that it can update or destroy those resources going forward.
The Terraform state file is the only way Terraform can track which resources it manages, and often contains sensitive information, so you must store your state file securely, outside your version control.

5. Inspect the current state using `terraform show`.

### Explore the `terraform.lock.hcl` file

When you initialize a Terraform configuration for the first time, Terraform will generate a new `.terraform.lock.hcl` file in the workspace dir.
You should include the lock file in your version control repository to ensure that Terraform uses the same provider versions across your team and in ephemeral remote execution environments.

While initializing your workspace, Terraform read the dependency lock file and download the specified versions. If Terraform did not find a lock file, it would download the latest versions of the providers that fulfill the version constraints you defined in the `required_providers` block.

1. Change the version constrains of `aws` provider from `4.16` to `~> 4.16`.
2. Initialize the workspace with the `terraform init -upgrade` flag to upgrade the provider to a higher version.

### Change the deployed infrastructure

Let's update the `ami` of your instance.

Change the `aws_instance.app_server` resource under the provider block in `main.tf` by replacing the current AMI ID with a new one.

Plan and apply your changes.

The prefix `-/+` means that Terraform will destroy and recreate the resource, rather than updating it in-place.
The AWS provider knows that it cannot change the AMI of an instance after it has been created, so Terraform will destroy the old instance and create a new one.
