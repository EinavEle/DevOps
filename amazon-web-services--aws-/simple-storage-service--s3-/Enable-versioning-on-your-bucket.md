
So far we've created an S3 bucket and communicat with it from within EC2 instance. 

You've probably noticed that in S3, objects can be easily lost by object override because the default behavior when uploading an object with the same key as an existing object is to replace the old object with the new one. If this happens unintentionally or due to a bug in the application code, it can result in the permanent loss of data.

The risk of data loss can be mitigated by implementing versioning in S3. When versioning is enabled, each object uploaded to S3 is assigned a unique version ID, which can be used to retrieve previous versions of the object. This allows you to recover data that was accidentally overwritten or deleted, and provides a safety net in case of data corruption or other issues.

**To enable bucket versioning**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

2. In the **Buckets** list, choose the name of the bucket that you want to enable versioning for\.

3. Choose **Properties**\.

4. Under **Bucket Versioning**, choose **Edit**\.

5. Choose **Enable**, and then choose **Save changes**\.

6. Upload multiple object with the same key, make sure versioning is working.

## Spot check

Is bucket versioninig affect the bucket cost? 

<details>
  <summary>
     Solution
  </summary>
    Yes. Each version of an object in a versioned bucket is stored separately. This means that if you upload multiple versions of the same object, you will be charged for the storage of each version. This can lead to higher storage costs compared to non-versioned buckets.
</details>