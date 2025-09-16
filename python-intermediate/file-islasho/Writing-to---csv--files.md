Writing to CSV files also uses the built-in csv tool from Python, where the only "trick" is that you have to write whole lists each time.


For example, if we have this data in our code:

```python
products = [
  {
    "name": "Apple",
    "product": "iPad",
    "price": 999
  },
  {
    "name": "Apple",
    "product": "iPod",
    "price": 1999
  },
  {
    "name": "Apple",
    "product": "iPed",
    "price": 2999
  },
  {
    "name": "Apple",
    "product": "iPud",
    "price": 3999
  },
  {
    "name": "Apple",
    "product": "iPid",
    "price": 4999
  }
] 
```

Then we would first have to extract the values from our dict, insert them into a list, and then save them. Like this:

```python
with open("products.csv", "w") as csv_file:
  csv_writer = csv.writer(csv_file)
  for product in products:
    # create a list with our data (the values from the dict above)
    data_in_list = [product["name"], product["product"], product["price"]]
    # writes a single row each time
    csv_writer.writerow(data_in_list) 
```

The `csv.writer` is a new "tool" we have that allows us to execute the writerow command - this command needs a list, which is exactly what we're giving it.


Notice that we're also using the `"w"` inside of open to indicate that we are writing a file. Because `products.csv` does not exist yet, Python will create this file for us.
