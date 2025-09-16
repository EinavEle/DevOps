We've reached our last station in the DevOps journey.
As a DevOps engineer, you will use monitoring tools to ensure the continuous health and performance of your services.
Platforms like Grafana, Kibana, Elasticsearch and Prometheus are commonly used to get real-time insights about the service, to trigger alerts when something is wrong, and to efficiently investigate these issues. 

## Elasticsearch and Kibana

**Elasticsearch** is the distributed search and analytics engine.
Elastic is a NoSQL database, can store structured or unstructured text, numerical data, or geospatial data. 
You can easily index data in a way that supports fast searches.

Elastic is a great choice to store and analyze logs, metrics, and security event data. 

**Kibana** is a web-based platform, which allows you to interactively explore, visualize, and get insights about your data. 

The Elasticsearch and Kibana projects (together with many more other projects) are developed and owned by the Elastic organization, and commonly referred as the [ELK stack](https://www.elastic.co/elastic-stack) (Elastic, Logstash, Kibana).
**Elasticsearch** in the database for storing the data, **Logstash** collects and streams the data into Elasticsearch from many different platforms, and **Kibana** provides a user-friendly interface for visualization and exploration. 


![.guides/img/monitoring_elk_stack](./monitoring_elk_stack.png)

