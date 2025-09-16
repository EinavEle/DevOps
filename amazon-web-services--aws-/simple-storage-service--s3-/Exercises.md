# Exercise 1 - Objects deletion in bucket versioning enabled

In this exercise we will explore the versioning enables bucket you've created. 

1. In the **Buckets** list, choose you bucket.
2. Choose **Upload** and upload an object multiple times under the same key, such that it has non-current versions.
3. In the bucket console, choose the **Objects** tab, and delete the object you have just uploaded.
4. After the deletion action, can you see the object in the bucket's objects list?

We will examine through AWS CLI what happened.

5. From your local machine, open a command terminal with [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed.

   ```shell
   aws --version
   ```

6. List the versions of you object. Replace `<bucket-name>` by you bucket name and `<object-key>` by the object key:
   
   ```shell
   aws s3api list-object-versions --bucket <bucket-name> --prefix <object-key>
   ```
   
   Can you confirm that you object has not been deleted? Inspect `DeleteMarkers`.

7. Delete the _delete mark_ by:

   ```shell
   aws s3api delete-object --bucket <bucket-name> --key <object-key> --version-id <delete-mark-version-id>
   ```
   
8. Can you see the object in the bucket's object list in the AWS Web Console? Can you confirm that the object was "deleted softly"?
9. How can you **permanently** delete an object (and its non-current versions) from a version-enabled bucket?

<details>
  <summary>
     Solution
  </summary>

No solution provided as this is a straight forward follow up. 

</details>


# Exercise 2 - Simple UPPERCASE ETL

ETL stands for Extract, Transform, and Load, which is a process used to extract data from various sources, transform it into a more useful format, and then load it into a destination system. 
Amazon S3 is often used as the source and destination for transformed data in ETL pipelines due to its durability, scalability, and cost-effectiveness.

Implement a simple ETL Python script that transform text objects to UPPERCASE. 
The script lists objects under `data/` "directory" in the bucket, processes them by changing their characters to uppercase, and uploads the processed objects to a `data_processed/` "directory" in the same bucket.

Test your script against real bucket and objects. 

<details>
  <summary>
     Solution
  </summary>


```python
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the bucket name and prefix for the source and destination objects
bucket_name = 'my-bucket'
source_prefix = 'data/'
destination_prefix = 'data_processed/'

# List the objects in the source prefix
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=source_prefix)

# Process each object
for obj in response['Contents']:
   # Get the object key
   obj_key = obj['Key']

   # Download the object to a local file
   download_path = '/tmp/' + obj_key
   s3.download_file(bucket_name, obj_key, download_path)

   # Transform the object data (change something in this example)
   with open(download_path, 'r') as f:
      data = f.read()
      transformed_data = data.upper()  # Change to upper case in this example

   # Upload the transformed data to the destination prefix
   destination_key = destination_prefix + obj_key[len(source_prefix):]
   s3.upload_file(download_path, bucket_name, destination_key)

   # Delete the local file
   s3.Object(bucket_name, obj_key).delete()
```

</details>

# Exercise 3 - Host static website 

Follow:  
https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html


# Exercise 4 - Create pre-signed URL 

Follow (You should do it **Using the S3 console**):   
https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html

# Exercise 5 - Verify object integrity using checksum

Follow:   
https://aws.amazon.com/getting-started/hands-on/amazon-s3-with-additional-checksums/?ref=docs_gateway/amazons3/checking-object-integrity.html

# Exercise 6 - Using customer SSE 

Inspired by the [following example](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#uploading-downloading-files-using-sse-customer-keys) from `boto3` official docs, write Python code that generates 32 bytes key and upload objects to S3 using SSE-C server-side encryption. 

Try to download the object from both the web console, and your Python script.

# (optional) Exercise 7 - implement point in time restore in Python

Write Python script to perform a point-in-time restore for an object stored in a version-enabled S3 bucket.

Usage example:

```bash
python point_in_time_restore.py mybucket myobject 2023-05-01T13:45:00.000Z
```

In this specific example, the script is being run with the following arguments:

- `mybucket`: This is the name of the S3 bucket that contains the object to be restored.
- `myobject`: This is the key (or filename) of the object that needs to be restored.
- `2023-05-01T13:45:00.000Z`: This is the timestamp representing the point in time to which the object should be restored.

When the script is executed with these arguments, it will first check if versioning is enabled on the S3 bucket. 
If versioning is not enabled, the script will exit and print an error message.
If versioning is enabled, the script will search for the closest previous version of the specified object based on the given timestamp.

If a previous version of the object is found, the script will perform a restore operation on that version, which will overwrite the current version of the object with the selected version.
If no previous version of the object is found, the script will exit and print a message indicating that no previous version was found.

So in this specific example, the `myobject` object in the `mybucket` S3 bucket will be restored to the version that was saved closest to May 1, 2023, at 1:45 PM (UTC).
