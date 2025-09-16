
The `terraform destroy` command terminates resources managed by your Terraform project.
This command is the inverse of `terraform apply` in that it terminates all the resources specified in your Terraform state.
It _does not_ destroy resources running elsewhere that are not managed by the current Terraform project.

1. Destroy the resources you created by `terraform destroy`.

The `-` prefix indicates that the instance will be destroyed.
Just like with `apply`, Terraform determines the order to destroy your resources. In this case, Terraform identified a single instance with no other dependencies,
so it destroyed the instance. In more complicated cases with multiple resources, Terraform will destroy them in a suitable order to respect dependencies.

You can destroy specific resource by `terraform destroy -target RESOURCE_TYPE.NAME`.

