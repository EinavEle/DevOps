
1. Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/)
2. In the navigation pane on the left side of the console, choose **Dashboard**.
3. On the right side of the console, choose **Create Table**.
4. Enter the table details as follows:
    1. For the table name, enter a unique table name.
    2. For the partition key, enter `Artist`.
    3. Enter `SongTitle` as the sort key.
    4. Choose **Customize settings**.
    5. On **Read/write capacity settings** choose **Provisioned** mode with autoscale capacity with a minimum capacity of **1** and maximum of **10**.
5. Choose **Create** to create the table.

### Write and read data from AWS web console

1. On DynamoDB web console page, choose **PartiQL editor** on the left side menu.
2. The following example creates several new items in the `<table-name>` table. The [PartiQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html) is
   a SQL-compatible query language for DynamoDB.

```text
INSERT INTO "<table-name>" VALUE {'Artist':'No One You Know','SongTitle':'Call Me Today', 'AlbumTitle':'Somewhat Famous', 'Awards':'1'}
```

```text
INSERT INTO "<table-name>" VALUE {'Artist':'No One You Know','SongTitle':'Howdy', 'AlbumTitle':'Somewhat Famous', 'Awards':'2'}
```

```text
INSERT INTO "<table-name>" VALUE {'Artist':'Acme Band','SongTitle':'Happy Day', 'AlbumTitle':'Songs About Life', 'Awards':'10'}
```

```text                            
INSERT INTO "<table-name>" VALUE {'Artist':'Acme Band','SongTitle':'PartiQL Rocks', 'AlbumTitle':'Another Album Title', 'Awards':'8'}
```

Query the data by

```text
SELECT * FROM "<table-name>" WHERE Artist='Acme Band' AND SongTitle='Happy Day'
```
