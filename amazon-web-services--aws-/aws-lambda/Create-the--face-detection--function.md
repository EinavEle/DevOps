
1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console\.
2. Choose **Create function**\.
3. Choose **Author from scratch**.
4. Create a `Python 3.9` runtime function from scratch.
5. Copy and deploy `face-blur-lambdas/face-detection/*.py` as the function source code (use the console code editor).
6. The IAM role of this function should have the following permissions: `AmazonS3FullAccess`, `AmazonRekognitionFullAccess` and `AWSStepFunctionsFullAccess`. It's recommended to use the same IAM role for all functions!
7. Configure a trigger for an **All object create** events for a given S3 bucket on objects with `.mp4` suffix (create a bucket and enable event notification if needed).
