We will use a DynamoDB table to store the job results.

- Design and create a DynamoDB table that will store results per Job ID.
- Under `youtube_subtitles_v3`:
  - Complete the `# TODO` in `worker/worker.py`, which responsible to write the results to a DynamoDB table for every completed job. Since the stored data should be read only once, very near to the point it was stored, the [TTL for items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) in the Dynamo table is 5 minutes (5 minutes old items should be deleted automatically).
  - Complete the `# TODO` in `fronetend/app.py`, in the `/status` endpoint. This endpoint responsible to retrieve the results from the table, while the job ID is given in the request as a query param.

Test your solution locally. 