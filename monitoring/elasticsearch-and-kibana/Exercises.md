
### Exercise 1 -  Working with Elasticsearch API

Throughout the tutorial we mainly worked with Kibana, which in turn queried the data from Elastic. 
Let's work with Elasticsearch API. 

1. Open Kibana’s main menu ("☰" near Elastic logo) and go to **Dev Tools** > **Console**. The Dev Tools allows you to interact with Elasticsearch using its API directly. This provides a more granular level of control over your data and enables advanced functionalities beyond what Kibana's graphical interface offers.
2. Submit the following indexing request to add a single document to the books index. 

```text
POST books/_doc
{"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470}
```

3. You can add multiple documents using the `_bulk` endpoint:

```text
POST /_bulk
{ "index" : { "_index" : "books" } }
{"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585}
{ "index" : { "_index" : "books" } }
{"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328}
{ "index" : { "_index" : "books" } }
{"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227}
{ "index" : { "_index" : "books" } }
{"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268}
{ "index" : { "_index" : "books" } }
{"name": "The Handmaids Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311}
```

4. Search the `books` index for all documents:

```text
GET books/_search
```

5. You can use the `match` query to search for documents that contain a specific value in a specific field. 

```text
GET books/_search
{
  "query": {
    "match": {
      "name": "brave"
    }
  }
}
```

Perform the following queries against the `kibana_sample_data_logs` data stream:

- Use the [match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html) to search for the word `twitter` contained in the field `message` in the documents.

<details>
  <summary>Solution</summary>

```text
GET kibana_sample_data_logs/_search
{
  "query": {
    "match": {
      "message": "twitter"
    }
  }
}
```

</details>

- Use the [match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html) to search for the word `twitter` **or** `facebook` contained in the field `message`.
- Use the [match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html) to search for the word `twitter` **and** `facebook` contained in the field `message`.
- Use the [boolean `must`](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html) query to search for the documents that contain the word `beats` in `message`, and `bytes` >= `1024`.
- Repeat the above query, but now replace `must` with `filter`. Notice the `_score` value.
- Use [boolean `must`](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html) query to search for the documents that contain the word `beats` in `message`, and `bytes` >= `1024`. In addition, add to the bool query the `should` entry to include documents with `referer` that contains `twitter.com`

For more information:

- https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html
- https://www.elastic.co/guide/en/elasticsearch/reference/current/search-with-elasticsearch.html

### Exercise 2 - Elastic data lifecycle

You can use **index lifecycle management (ILM)** to automate the management of indices.
For example, you can use ILM to automatically move older backing indices to less expensive hardware and delete unneeded indices. 
ILM can help you reduce costs and overhead as your data grows.

Follow https://www.elastic.co/guide/en/elasticsearch/reference/current/set-up-lifecycle-policy.html and create a policy as follows:

- Data is being transferred to Warm phase after 60 days.
- Data is deleted after 365 days. 
- Replication is reduced to 1 (in case the documents are replicated more than once in the index).

Apply the created policy with your logs sample data stream: 

1. Go to **Stack Management** > **Index Management**.
2. Under **Index Templates** tab choose your data stream.
3. In the opened tab, clock on **Manage**, then **Edit**.
4. In the **Index setting** step, add the below entry under the `index` key:

```text
lifecycle.name": "YOUR POLICY NAME"
```

Test your changes. 

### Exercise 3 - Snapshot and restore

A **snapshot** is a backup of a running Elasticsearch cluster.

Review the docs:    
https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html

Then go to **Stack Management** > **Snapshot and Restore**. 

Define an S3 repository and a snapshot policy to backup your logs data stream every day at midnight. 
