CSV is another popular file type - you might recognize it due to its familiarity with Excel/Google Sheets.

CSV stands for Comma Separated Values, and it looks like a table with rows and columns:

```console
owner, expense, category
Ryan, 17, groceries
Diane, 200, water bill
Diane, 180, electricity bill
Ryan, 48, decor
Jess, 200, internet 
```

Typically the first row of a CSV file will be the headers, and every row after that is the next set of data.


To read CSV files, Python has a built-in tool, called csv which we need to import into our code.

To follow along with this example, **copy the above data into a `expenses.csv` file:**

```python
import csv
with open('expenses.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader:
    print(row) 
```

If you run the code above, you'll see this being output:

```console
['owner', ' expense', ' category']
['Ryan', ' 17', ' groceries']
['Diane', ' 200', ' water bill']
['Diane', ' 180', ' electricity bill']
['Ryan', ' 48', ' decor']
['Jess', ' 200', ' internet'] 
```

So what we understand is that the csv_reader reads the file and gives us access to each row in the data as a list when we loop over it.


The slight "issue" with this is that we're also iterating over the first row - the headers of our "table", which typically is not interesting to us.

Luckily, Python has a command called next that can take care of this for us:

```python
with open('expenses.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  next(csv_reader) 
  # for row... 
```

All next does is skip the first row, which will allow us to only loop over the rows of data in which we're interested.



Now that we know how to access the data, using it is simple - exactly the same way you work with any list. For instance, if we wanted to sum all the expenses, we'd have to access each row at index 1, and sum them:

---

```python
total_expenses = 0  

with open('expenses.csv') as csv_file:      
  # read the data and skip the first row     
  csv_reader = csv.reader(csv_file)     
  next(csv_reader)      
  
  # iterate over the data     
  for row in csv_reader:         
    # add each expense to our counter         
    total_expenses += int(row[1])  


print(total_expenses) 
# outputs: 645 
```

Notice that we have to use int to convert our data into a number, because the CSV format saved it as a string.
