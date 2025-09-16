The Kibana Query Language (KQL) is a simple text-based query language for filtering data in the Discover page.

Follow [the KQL short tutorial](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) from Elastic's official docs.



### Spot check - Practice KQL

Open the **Kibana Sample Data Logs** data view under **Discover** page, and search for the following information:

1. Query all logs with response code 200 or 404 from the last 4 days.
2.  Query all successful requests from last day, referred from `twitter.com`
3.  Search all documents where the `request` field contains the string `elasticsearch-6.3.2.deb` within the last 7 days.
4.  According to a bad system design, your platform has to block users from download large files (files larger than `9216` bytes (9KB)) during every day for 30 minutes. The product manager asks your insights regarding the hour in the day that you should apply this limitation. What hour will you advise?
5.  Click on the **+** button (Add Filter) to displays data when `hour_of_day` value is in between the working hours only (`9-17`).
6. What is the maximum requested resource (highest `bytes` request) within the last 7 days, during working hours? Was it responded with `200` status code?



<details>
  <summary>
     Solution
  </summary>

 Here is a solution for the first 3 queries:

 1. `response_code:(200 or 404) and @timestamp >= now-4d`
 2. `response_code:200 and referer: "twitter.com" and @timestamp >= now-1d`
 3. `request: "elasticsearch-6.3.2.deb" and @timestamp >= now-7d`

</details>