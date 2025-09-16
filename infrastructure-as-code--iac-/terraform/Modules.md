
Modules help you to package and reuse Terraform resources and configurations.
Modules are containers for multiple resources that are used together, consists of a collection of `.tf` files kept together in a directory.

For example, let's say you want to provision a VPC in your AWS account. Obviously, a complete VPC requires provisioning of many different Terraform resources (VPC, subnet, route table, gateways, etc..). 
But some must have already done it before, some have provisioned a well-defined VPC in AWS. Why not using her work?   

Modules can help.

#### The root module

Every Terraform configuration has at least one module, known as its root module, which consists of the resources defined in the `.tf` files in the main working directory.

#### Use the Terraform Registry

1. Open the [Terraform Registry page for the VPC module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws). Review the module **Inputs** and **Outputs**.

2. Add the below block into your `main.tf` file to use the VPC module:
   ```terraform
   module "app_vpc" {
     source  = "terraform-aws-modules/vpc/aws"
     version = "3.14.0"
   
     name = "${var.resource_alias}-vpc"
     cidr = var.vpc_cidr
   
     azs             = ["<az1>", "<az2>", "..."]
     private_subnets = var.vpc_private_subnets
     public_subnets  = var.vpc_public_subnets
   
     enable_nat_gateway = false
   
     tags = {
       Name        = "${var.resource_alias}-vpc"
       Env         = var.env
       Terraform   = true
     }
   }
   ```
   Make sure you specify a list of `azs` (availability zones) according to your region.

3. Add the following output in `outputs.tf`:

   ```terraform
   output "vpc_public_subnets" {
     description = "IDs of the VPC's public subnets"
     value       = module.app_vpc.public_subnets
   }
   ```

4. Edit `vpc-vars.tf` so you'll have two private, and two public subnets within your VPC.
5. Apply and inspect your VPC in AWS Console.

Let's migrate the EC2 and the security group into your VPC:

5. Add the following attribute to the `aws_security_group.sg_web` resource:
   ```text
     vpc_id      = module.app_vpc.vpc_id
   ```

6. Add the following attributes to the `aws_instance.app_server` resource:
   ```text
     subnet_id              = module.app_vpc.public_subnets[0]
   ```
