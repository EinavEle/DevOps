Let's create MySQL RDS instance:

1. Add the following resources to your configuration file:

```terraform
resource "aws_db_subnet_group" "private_db_subnet" {
  subnet_ids = module.app_vpc.public_subnets
}

resource "aws_db_instance" "database" {
  allocated_storage = 5
  db_name              = "${var.resource_alias}mysql"
  engine            = "mysql"
  instance_class    = "db.t2.micro"
  username          = "admin"
  password          = "password"

  db_subnet_group_name = aws_db_subnet_group.private_db_subnet.name
  skip_final_snapshot = true
}
```

2. The database username and password are hard-coded. Refactor this configuration to remove these values:
   1. Explore the variables `db-vars.tf` (comment them in!). Notice that you've declared the variables as `sensitive`.
   2.  Now update main.tf to reference these variables:
   ```text
   -  username          = "admin"
   -  password          = "password"
   +  username          = var.db_username
   +  password          = var.db_password
   ```

If you were to run terraform apply now, Terraform would prompt you for values for these new variables since you haven't assigned defaults to them. 
However, entering values manually is time consuming and error prone. 
Next, you will use two different methods to set the sensitive variable values, and learn about security considerations of each method.

**Set values with a `.tfvars` file**

Terraform supports setting variable values with variable definition (`.tfvars`) files. 
You can use multiple variable definition files, and many practitioners use a separate file to set sensitive or secret values.

3. Create a new file called `secret.tfvars` to assign values to the new variables.
   ```text
   db_username = "admin"
   db_password = "password"
   ```
4. Apply by `terraform apply -var-file="secret.tfvars"`


<details>
<summary>Read more about `.tfvars` files</summary>

To set lots of variables, it is more convenient to specify their values in a variable definitions file (with a filename ending in .tfvars) and then specify that file on the command line with `-var-file`:
```text
terraform apply -var-file="testing.tfvars"
```

A variable definitions file uses the same basic syntax as Terraform language files, but consists only of variable name assignments:

```text
image_id = "ami-abc123"
availability_zone_names = [
  "us-east-1a",
  "us-west-1c",
]
```
</details>

**Set values using environment variables**

Set the database administrator username and password using environment variables:

3. Define the following env vars:

   ```text
   export TF_VAR_db_username=admin TF_VAR_db_password=password
   ```

4. Plan and apply.



### Protect your infrastructure from being destroyed

To prevent destroy operations for specific resources,
you can add the `prevent_destroy` attribute to your resource definition.
This [lifecycle](https://www.terraform.io/language/meta-arguments/lifecycle) option prevents Terraform from accidentally removing critical resources.

1. Add the `lifecycle` meta-argument by:
   ```
   lifecycle {
      prevent_destroy = true
   }
   ```
2. Apply the change, then apply a destroying change and test the rule.
