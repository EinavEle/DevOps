
As you've probably noticed, instead of sending the recognized text to the client, we just send a **job ID** as a reference.

Why is that? the new architecture using SQS queue leads to a problem related to obtaining the results from the Worker service.
While in the previous synchronous architecture communication was direct and straightforward,
the Frontend service now delegates the processing task to the Worker service through the SQS queue, and when the job is done, it no longer has immediate access to the results.

Furthermore, the client has no direct way of knowing when the video processing is completed, since the Frontend service responses to the client's request immediately after the job was submitted to the SQS queue.

In order to allow users to receive results, we should somehow pass the results from Workers to the Frontend service, and then somehow ask the end-user to retrieve the results from the Frontend service.  

A very common architecture is **using a database** to store the results by Workers, allowing the Frontend service to read from the DB at any time:

- When some Worker completed a job, it writes the results to a database. 
- In the client side, using Javascript code and the received **job ID**, we continuously request (e.g. every 5 seconds) the Frontend service to check if there are some available results, until the job will be completed and results are available. 
- In every client request, the Frontend service checks for available results in the DB. If the job hasn't been completed yet, the Frontend service responds with a status code `0` to the client, indicating a "processing" status.
- If the job was completed (the Frontend service found results in the DB for the given Job ID), the Frontend service responds with a status code `200` indicating "completed", along with the resulted text.

Let's implement it!
