
Let's narrow the above policy of your S3 bucket.

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. From the console, open the IAM user or role that should have access to only a certain bucket.
3. In the **Permissions** tab, remove the **AmazonS3FullAccess** AWS managed policy.
4. Click **Add permissions** and **Create inline policy**
5. Choose **Import manages policy** and import **AmazonS3FullAccess**, switch to the JSON view of your new policy.
6. Inspired by [policies examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html) in AWS IAM docs, try to change the given policy JSON such that it allows the user to list, read, and write objects with a prefix `images/`
7. Save your policy, test it.
8. Validate your changes using the [IAM Policy Simulator](https://policysim.aws.amazon.com/).