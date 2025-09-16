
MongoDB is a [document](https://www.mongodb.com/document-databases), [NoSQL](https://www.mongodb.com/nosql-explained/nosql-vs-sql) database, offers high availability deployment using multiple replica sets.
**High availability** (HA) indicates a system designed for durability and redundancy.
A **replica set** is a group of MongoDB servers, called nodes, containing an identical copy of the data.
If one of the servers fails, the other two will pick up the load while the crashed one restarts, without any data loss.

Follow the official docs to deploy containerized MongoDB cluster on your local machine. 
Please note that the mongo deployment should be configured **to persist the data that was stored in it**.

https://www.mongodb.com/compatibility/deploying-a-mongodb-cluster-with-docker

Got HA mongo deployment? great, let's move on...