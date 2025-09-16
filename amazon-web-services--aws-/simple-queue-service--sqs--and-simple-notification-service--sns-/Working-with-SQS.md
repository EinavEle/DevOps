
## Create standard queue

1. Open the Amazon SQS console at https://console.aws.amazon.com/sqs/

1. Choose **Create queue**.

1. For **Type**, the **Standard** queue type is set by default. 

1. Enter a **Name** for your queue, e.g. `alonit-youtube-jobs`.

1. Under Configuration, set values for parameters according to the following characteristics:

    - We let consumer `60 seconds` to process single message.
    - The amount of time a single message will be stored in the queue until it's processed by one of the consumers is `1 day`.
    - We don't want any delay between the time the message is produced to the queue to the time it is consumed.
    - We know that the maximal message size is `256KB`.

2. Choose the Basic **Access policy**.
1. Choose **Create queue**. Amazon SQS creates the queue and displays the queue's Details page.

## Manually send a message to the queue

1. From the left navigation pane, choose **Queues**. From the queue list, select the queue that you created.
1. From **Actions**, choose **Send and receive messages**.
1. In the **Message body**, enter the message text.
1. For a standard queue, you can enter a value for **Delivery delay** and choose the units. For example, enter `60` and choose seconds.
1. Choose **Send message**.

## Purge a queue

If you don't want to delete an Amazon SQS queue but need to delete all of the messages from it, purge the queue. The message deletion process takes up to 60 seconds. 

1. Open the Amazon SQS console at https://console.aws.amazon.com/sqs/
1. In the navigation pane, choose **Queues**.
1. On the **Queues** page, choose the queue to purge.
1. From **Actions**, choose **Purge**.
1. In the **Purge queue** dialog box, confirm the purge by entering `purge` and choosing **Purge**.

All messages are purged from the queue. The console displays a confirmation banner.
