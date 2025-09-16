# Exercise 1 - Process new items with DynamoDB Streams and Lambda

### Enable Streams

1. In the navigation pane on the left side of the console, choose **Tables**.
2. Choose your table from the table list.
3. Choose the **Exports and streams** tab for your table.
4. Under **DynamoDB stream details** choose **Enable**.
5. Choose **New and old images** and click **Enable stream**.

### Create Lambda execution IAM role

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/).

2. In the navigation pane, choose **Roles**, **Create role**\.

3. On the **Trusted entity type** page, choose **AWS service** and the **Lambda** use case\.

4. On the **Review** page, enter a name for the role and choose **Create role**\.
5. Edit your IAM role with the following inline policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:<region>:<accountID>:function:<lambda-func-name>*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:<region>:<accountID>:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams"
            ],
            "Resource": "arn:aws:dynamodb:<region>:<accountID>:table/<dynamo-table-name>/stream/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Change the following placeholders to the appropriate values: `<region>`, `<accountID>`, `<dynamo-table-name>`, `<lambda-func-name>`

The policy has four statements that allow your role to do the following:

+ Run a Lambda function. You create the function later in this tutorial\.
+ Access Amazon CloudWatch Logs\. The Lambda function writes diagnostics to CloudWatch Logs at runtime\.
+ Read data from the DynamoDB stream.
+ Publish messages to Amazon SNS\.

### Create a Lambda Function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console\.

2. Choose **Create function**\.

3. Under **Basic information**, do the following:

    1. Enter **Function name**.

    2. For **Runtime**, confirm that **Node\.js 16\.x** is selected\.

    3. For **Permissions** use your created role.

4. Choose **Create function**\.
5. Enter your function, copy the content of `dynamodb_lambda_func/publishNewSong.js` and paste it in the **Code source**. Change `<TOPIC-ARN>` to your SNS topic ARN you created in the previous exercise.
6. Click the **Deploy** button.
7. On the same page, click **Add trigger** and choose your Dynamo table as a source trigger.
8. Test your Lambda function by creating new items in the Dynamo table and watch for new emails in your inbox.

