Another possible solution to address the Worker - Frontend communication problem is by using a simple HTTP request from the Worker service to the Frontend service to sends the results.
When the Worker service completed some job, it can make an HTTP request to a specific endpoint exposed by the Frontend service, providing the job ID and the corresponding results in the request payload. 
The Frontend service, upon receiving the HTTP request, can then associate the results with the respective job and make them available to the end-user retrieval.

**Why will this solution fail when the Frontend service is deployed in HA architecture?**  
