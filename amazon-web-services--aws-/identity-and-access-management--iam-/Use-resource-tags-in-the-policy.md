
Using resource tags in an AWS policy can help you implement more granular access controls based on the tags assigned to the resources. By using tags in the policy, you can specify permissions for specific tags or tag values, which can make it easier to manage access and automate resource management based on tags.

Let's see an example:

1. In IAM roles console, choose your role.
2. In **Tags** tab, add a tag with the key `BucketPrefix` and some value according to your choice.
3. Instead of allow operation on prefix `images/`, try to allow access on a dynamic prefix according to the principal tag:

```text
"Resource": ["arn:aws:s3:::<your-bucket-name>/${aws:PrincipalTag/BucketPrefix}/*"]
```

4. Test it.