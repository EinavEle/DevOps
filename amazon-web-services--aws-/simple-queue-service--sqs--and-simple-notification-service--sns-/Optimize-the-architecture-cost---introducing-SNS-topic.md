
Happy and satisfied you've deployed the DynamoDB solution! But then, after analysing the annual cost of this solution, you discover that the solution is very expensive.
Thousands of hundreds of requests are made to the DB, in vain. Most of the requests are merely checking whether a given job is done or not.

Let's implement caching mechanism that will mitigate the cost while maintaining the desired functionality and user experience.

**Here SNS (Simple Notification Service) comes in**.

Here's how you can integrate it to optimize the workflow:

- When the Worker service completes a job and writes results to DynamoDB, it also **publishes** a message to an **SNS topic**. This message includes the job ID of the completed job.

- Each Frontend instance **subscribes** to the SNS topic during its launch (assuming that the Frontend service operates across multiple instances). 
  This subscription enables Frontend instances to receive notifications when jobs are completed.

- When a Frontend instance receives a message from the SNS topic indicating the job has been completed, it should store the Job ID locally within the Frontend instance itself. 
  This local cache storage ensures that the information regarding completed jobs is readily available in the instance, without the need to query the DynamoDB table every time a client requests the job status. 

- Just as before, the client-side continues to query the Frontend service for job status using the job ID, every 5 seconds.
  However, now the Frontend instance can respond directly with the locally stored job ID cache, eliminating the need for frequent DynamoDB queries.
  - If the requested job ID exists in the instance local cache, it means that the Frontend instance was notified through the SNS topic about this job completion. Now the Frontend instance can read the results from the DB, knowing for sure that there will be some results for this job ID. 
  - If the requested job ID doesn't exist in the instance local cache, it is still being processed by some of the workers (or still queued, waiting for an available Worker to work on it).

With this approach, DynamoDB is accessed **only twice** per job. Once by a Worker instance, writing the results of a completed job, and once by a Frontend instance, when reading the job results upon client request. 

This optimization can help reduce costs, especially if you have a high volume of jobs being processed.

Let's implement it! But before.... a question
