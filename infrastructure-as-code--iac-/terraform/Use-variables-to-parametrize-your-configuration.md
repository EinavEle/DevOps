
The current configuration includes a number of hard-coded values.
[Terraform variables](https://developer.hashicorp.com/terraform/language/values/variables) allow you to write configuration that is flexible and easier to re-use.

1. In the workspace dir, create a new file called `variables.tf` with a block defining a new `env` variable, which will be used to indicate the environment that the infrastructure will be provisioned.
   ```terraform
   variable "env" {
   description = "Deployment environment"
   type        = string
   default     = "dev"
   }
   ```
2. In `main.tf`, update the `aws_instance.app_server` resource block to use the new variable. The `env` variable block will default to its default value ("dev") unless you declare a different value.
   ```text
    tags = {
   -    Name = "<instance-name>"
   +    Name = "<instance-name>-${var.env}"
    }
   ```
   
   Now you know that this instance belongs to Development environment, for example. 

   You can also define configurations dynamically using a variable value:

   ```text
   - instance_type = "t2.micro"
   + instance_type = var.env == "prod" ? "t2.micro" : "t2.nano"
   ```

   In your `main.tf` file, change the line denoted by `-` with the line denoted by `+`. The [conditional expression](https://www.terraform.io/language/expressions/conditionals) (among over many more [expressions](https://www.terraform.io/language/expressions)) uses the value of a boolean expression to select one of two values.

3. Plan and apply the configuration.

### Extend your EC2

Terraform infers dependencies between resources based on the given configurations, so that resources are created and destroyed in the correct order. 
Let's create a Security Group for our EC2:

1. Add another variable to `variables.tf`:
   ```terraform
   variable "resource_alias" {
     description = "Your name"
     type        = string
     default     = "=<your-name>"
   }
   ```

   Change `<your-name>` to your alias.

2. Create a Security Group resource
   ```terraform
   resource "aws_security_group" "sg_web" {
     name = "${var.resource_alias}-${var.env}-sg"
   
     ingress {
       from_port   = "8080"
       to_port     = "8080"
       protocol    = "tcp"
       cidr_blocks = ["0.0.0.0/0"]
     }
   
     tags = {
       Env         = var.env
       Terraform   = true
     }
   }
   ```

3. To attach the created security group to your EC2 instance, add the following attributes to the `aws_instance.app_server` instance:

   ```text
     vpc_security_group_ids = [aws_security_group.sg_web.id]
     key_name = "<your-key-pair-name>"
   ```

4. Plan and apply.

You can use the `depends_on` meta-argument to handle hidden resource dependencies that Terraform cannot automatically infer (e.g. S3 bucket should be ready before an EC2 instance can store data in it).

5. Create the following S3 bucket resource:

   ```terraform
   resource "aws_s3_bucket" "data_bucket" {
     bucket = "<bucket-name>"
   
     tags = {
       Name        = "${var.resource_alias}-bucket"
       Env         = var.env
       Terraform   = true
     }
   }
   ```

6. Assuming the `aws_instance.app_server` EC2 instance read/write data from the `data_bucket`, we can say that there is an implicit dependency between the EC2 to the bucket.
   Add the following `depends_on` meta-attribute to `aws_instance.app_server`:
   ```text
   depends_on = [
      aws_s3_bucket.data_bucket
   ]
   ```
   
7. Plan and apply.
