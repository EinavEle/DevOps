Using this data:

```python
stocks = [
  {"name": "Apple", "price": 246},
  {"name": "Tesla", "price": 328},
  {"name": "Microsoft", "price": 140},
  {"name": "Amazon"},
  {"name": "Lionsgate", "price": 8},
  {"name": "Netflix", "price": 276},
  {"name": "Google"},
  {"name": "Activision", "price": 55},
] 
```

Create a CSV file called `stocks.csv` that has all the data in the list above.

Your CSV file should look like this in the end:
```console
Company,Price
Apple,246
Tesla,328
Microsoft,140
Amazon,0
Lionsgate,8
Netflix,276
Google,0
Activision,55 
```

**Note** that some of the dicts don't have a price - you have to handle this in your code by giving them a default value of `0`.


Take a look at [this solution](https://github.com/Elevationacademy/python-spotcheck-solutions/blob/master/File-IO/sc4.py) once you're done, or if you've been trying for at least 20 minutes.
