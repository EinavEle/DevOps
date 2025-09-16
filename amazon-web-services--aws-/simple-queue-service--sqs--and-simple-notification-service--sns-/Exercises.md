
## Exercise 1 - Queues retry mechanism and dead letter queues

In `retry_queue` you are provided with simplified Python code snippets for a producer and consumer for an SQS queue. 
The producer sends messages (jobs) to the queue, and the consumer processes these jobs. 

In this scenario, 30% of the jobs that the consumer processes will intentionally **fail**.

You should implement a **retry mechanism**.

When the consumer fails to process a job, re-send the job to the queue with a **delay exponentially growing depending on the retry number**.

For example, given the job:

```python 
message_body = {
    'retry': 0,
    'job_id': 'ecdce74b-50ef-4218-a46b-a1c7122fa958'
}
```

- For the first time the job will fail, it will be sent to the queue with a `DelaySeconds` of 2 seconds.
- For the second time the job will fail, it will be sent to the queue with a `DelaySeconds` of 4 seconds.
- For the 3rd time the job will fail, it will be sent to the queue with a `DelaySeconds` of 8 seconds.
- If the job fails again (the 4th time), send it to a [dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) for further manual investigation by an engineer.

**Why this is a good practice to delay failed jobs?**

## Exercise 2 - Sending a message to an Amazon SQS queue from Amazon Virtual Private Cloud

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-sending-messages-from-vpc.html
