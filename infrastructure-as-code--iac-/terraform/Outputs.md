
### Add Outputs

[Terraform Output](https://developer.hashicorp.com/terraform/language/values/variables) values allow you to export structured data about your resources. 
You can use this data to configure other parts of your infrastructure with automation tools, or as a data source for another Terraform workspace. 
Outputs are also necessary to share data from a child module to your root module (modules will be discussed soon).

1. Create a file called `outputs.tf` with the below configuration:

```terraform
output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}
```

2. Apply and see the output values in the stdout. The instance IP values can now be used as an input in further terraform work.

