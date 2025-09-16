The above architecture is referred to as **synchronous architecture** because communication between these services occurs in a synchronous manner -
end users wait for a response from the Frontend service, which in turn waits for a response from the Worker service.  

This architecture may work well for smaller-scale applications.
However, it has some disadvantages in terms of scalability and failure tolerance.

- **Scalability**: In the current architecture, the Frontend microservice directly sends a request to the Worker microservice to process the YouTube URL and generate subtitles. As the application's load increases, this direct communication can lead to performance bottlenecks and slow down response times to the end users. 
  The bottleneck here creates a situation where Frontend's performance is limited by the slow response from Worker. 

- **Fault Tolerance**: The current architecture lacks built-in failure tolerance mechanisms. If the Worker microservice experiences an unexpected failure or goes offline, the Frontend service has no way to handle or recover the outstanding end-users requests.

Let's introduce a **queue** system to address these issues.
