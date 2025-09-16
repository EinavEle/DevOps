
## Talk with Dynamo using `aws` cli

From your local machine, write some more items using the `aws dynamodb put-item` command.
Use the `aws dynamodb get-item` to get some item.

## Database migration 

Database migration is the process of transferring data and schema from one database to another, typically when transitioning to a new system or version. 

Zero downtime database migration refers to the seamless migration of a database without any interruption or impact on the availability of the system. 
It involves careful planning, replication, and synchronization techniques to ensure continuous service while transitioning to the new database environment.

1. Start [`mongo`](https://hub.docker.com/_/mongo) docker container.
2. Start the script under `db_migration/init.py`. The script should write new data to your running mongo every second. Keep this script running while you work on your next step.
3. Based in the script in `db_migration/init.py`, create another script called `mirror_db.py` such that every data that is written to mongo will be written to dynamoDB table (create this table with `dataId` as a partition key).
4. (Optional) Use `try...except` to catch and handle the case where the write operation for either mongo or dynamo is failed. 
5. Stop the running script from step 2, keep the timestamp of the last document that was written to mongo. 
6. Start the `mirror_db.py` script. From now on, every piece of data is being written to both mongo and dynamo. You only need to create to the data written before you started the mirror script. 
7. Write a script that copies all the documents with timestamp smaller than or equal to the timestamp you kept from step 5. This script should be run only once.   

After a while... stop the `mirror_db.py` script and check that the data stored in both DBs is identical (you may write some python script for that).


##  Point-in-time recovery for DynamoDB

Restore your table to how it was looking like a few minutes ago.   

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html#restoretabletopointintime_console



