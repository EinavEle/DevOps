
A backend defines where Terraform stores its [state](https://www.terraform.io/language/state) data files.
This lets multiple people access the state data and work together on that collection of infrastructure resources.
When changing backends, Terraform will give you the option to migrate your state to the new backend. This lets you adopt backends without losing any existing state.
Always backup your state!

1. To configure a backend, add a nested `backend` block within the top-level `terraform` block. The following example configures the `s3_backend` backend:
   ```text
   backend "s3" {
    bucket = "<bucket-name>"
    key    = "tfstate.json"
    region = "<bucket-region>"
    # optional: dynamodb_table = "<table-name>"
   }
   ```
2. Apply the changes and make sure the state is stored in S3.

This backend also supports state locking and consistency checking via Dynamo DB, which can be enabled by setting the `dynamodb_table` field to an existing DynamoDB table name.
The table must have a partition key named `LockID` with type of `String`.
