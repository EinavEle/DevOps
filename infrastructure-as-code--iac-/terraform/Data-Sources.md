Data sources allow Terraform to use information defined outside your configuration files.
Cloud infrastructure, applications, and services emit data, which Terraform can query and act on using **data sources**.
A data sources fetches information from cloud provider APIs, such as disk image IDs, availability zones etc...

You will use the [`aws_availability_zones`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/availability_zones) data source (which is part of the AWS provider) to configure your VPC's Availability Zones (AZs) dynamically according to the region you work on.
That way you can make your configuration files more modular, since AZs values would not be hard-coded, but fetched dynamically. 

1. List the AZs which can be accessed by an AWS account within the region configured in the provider.

```terraform
data "aws_availability_zones" "available_azs" {
  state = "available"
}
```

2. Change the following attribute in `app_vpc` module:

```text
- azs             = ["<az1>", "<az2>", ...]
+ data.aws_availability_zones.available_azs.names
```

3. Plan and apply.

Now your `app_vpc` block is region-agnostic! the same configuration can be applied on any region in AWS without changing the terraform code.

The `aws_instance` configuration also uses a hard-coded AMI ID, which is only valid for the specific region. 
Use an `aws_ami` data source to load the correct AMI ID for the current region.

4. Add the following `aws_ami` data source to fetch AMIs from AWS API:

```terraform
data "aws_ami" "ubuntu_ami" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical owner ID for Ubuntu AMIs

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}
```

5. Replace the hard-coded AMI ID with the one loaded from the new data source.

```text
-  ami = "<your-hard-coded-ami>"
+  ami = data.aws_ami.amazon_linux_ami.id
```

6. Add the following output in `outputs.tf`:

```text
output "app_server_ami" {
  description = "ID of the EC2 instance AMI"
  value       = data.aws_ami.amazon_linux_ami
}
```

7. Plan and apply.
