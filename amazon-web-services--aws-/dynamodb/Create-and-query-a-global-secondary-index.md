
1. In the navigation pane on the left side of the console, choose **Tables**.
2. Choose your table from the table list.
3. Choose the **Indexes** tab for your table.
4. Choose **Create** index.
5. For the **Partition key**, enter `AlbumTitle`.
6. For **Index** name, enter `AlbumTitle-index`.
7. Leave the other settings on their default values and choose **Create** index.

8. You query the global secondary index through PartiQL by using the Select statement and providing the index name
```shell
SELECT * FROM "<table-name>"."AlbumTitle-index" WHERE AlbumTitle='Somewhat Famous'
```
