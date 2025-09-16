
1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.
2. In the left navigation pane, choose **Buckets**\.
3. Choose **Create bucket**.

   The **Create bucket** wizard opens.

4. In **Bucket name**, enter a DNS-compliant name for your bucket.

   The bucket name must:
    + Be unique across all of Amazon S3.
    + Be between 3 and 63 characters long.
    + Not contain uppercase characters.
    + Start with a lowercase letter or number.

5. In **Region**, choose the AWS Region where you want the bucket to reside.

   Choose the Region where you provisioned your EC2 instance.

6. Under **Object Ownership**, leave ACLs disabled. By default, ACLs are disabled\. A majority of modern use cases in Amazon S3 no longer require the use of ACLs\. We recommend that you keep ACLs disabled, except in unusual circumstances where you must control access for each object individually\. 

8. Enable Default encryption with `SSE-S3` encryption type.

9. Choose **Create bucket**.
