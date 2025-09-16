# Exercise 1 - practice policies 

Create the below policies following the Principle of the [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).

1. IAM policy with permissions to start and stop EC2 instance.
2. IAM policy with permissions read object from S3 buckets except objects starting with "internal/"
3. IAM policy with permissions to upload objects from STANDARD and STANDARD_IA storage classes only.
4. IAM policy with permissions to attach EBS to EC2.
5. IAM policy with permissions to attach EBS to EC2 from us-east-1 region only.
6. IAM policy with permissions to attach EBS to EC2 from all US and EU regions.
7. IAM policy which denying users to assign policies to and identity, which means, users under this policy cannot assign IAM policies to other users, groups, roles.


<details>
  <summary>
     Solution
  </summary>


IAM policy with permissions to start and stop EC2 instance:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StartStopEC2",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "*"
        }
    ]
}
```

IAM policy with permissions read object from S3 buckets except objects starting with `internal/`.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadS3Objects",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::my-bucket/*",
                "arn:aws:s3:::my-bucket"
            ],
            "Condition": {
                "StringNotLike": {
                    "s3:prefix": "internal/*"
                }
            }
        }
    ]
}

```

IAM policy with permissions to upload objects from STANDARD and STANDARD_IA storage classes only.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "UploadS3Objects",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "StringEquals": {
                    "s3:StorageClass": [
                        "STANDARD",
                        "STANDARD_IA"
                    ]
                }
            }
        }
    ]
}
```

IAM policy with permissions to attach EBS to EC2.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AttachEBSToEC2",
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes"
      ],
      "Resource": "*"
    }
  ]
}
```

IAM policy with permissions to attach EBS to EC2 from us-east-1 region only.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AttachEBSToEC2",
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ec2:Region": "us-east-1"
        }
      }
    }
  ]
}
```

IAM policy with permissions to attach EBS to EC2 from all US and EU regions.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AttachEBSToEC2",
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "ec2:Region": [
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-south-1",
            "eu-west-3",
            "eu-south-2",
            "eu-north-1",
            "eu-central-2"
          ]
        }
      }
    }
  ]
}
```

IAM policy which denying users to assign policies to and identity, which means, users under this policy cannot assign IAM policies to other users, groups, roles.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyPolicyAssignment",
            "Effect": "Deny",
            "Action": [
                "iam:AttachUserPolicy",
                "iam:AttachGroupPolicy",
                "iam:AttachRolePolicy",
                "iam:PutUserPolicy",
                "iam:PutGroupPolicy",
                "iam:PutRolePolicy"
            ],
            "Resource": "*"
        }
    ]
}
```


</details>


## Exercise 2 - S3 encrypt data at transit

As you may know, Amazon S3 offers encryption in **transit** and encryption **at rest**. Encryption in transit refers to HTTPS and encryption at rest refers to client-side or server-side encryption.

Since Amazon S3 allows both HTTP and HTTPS requests, encryption in transit may be violated.
We would like to create a resource-based policy that will we associated with an S3 bucket and will enforce HTTPS communication only. 

Use [this resource as a reference](https://repost.aws/knowledge-center/s3-bucket-policy-for-config-rule) to define the policy and attach it to your bucket. 


<details>
  <summary>
     Solution
  </summary>


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceHttpsOnly",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::your-bucket-name/*"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
```
  
</details>


## (optional) Exercise 3 - ABAC 

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes.
In AWS, these attributes are called **tags**.
You can attach tags to almost any AWS resource (EC2 instance, S3 bucket), including IAM entities (users or roles).

ABAC policies can be designed to allow operations when the principal's tag matches the resource tag.
ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

Follow:   
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html



