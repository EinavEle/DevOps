The **datetime** module works with dates and times. Surprising, we know!

To use this module we need to import it first: `import datetime`  


## datetime.date

`datetime.date` is a simple format for dates object.

```Python
import datetime
print(datetime.date.today())
# Output: 2020-02-11 
```

`datetime.date.today` gives us today's date including the year, month and day. It can be useful when we need to record what day it is.

For example, when we want to save information in log messages or when we work with databases.


## datetime.datetime

`datetime.datetime` contains all the information about the date and time objects.

```Python
import datetime


print(datetime.datetime.today())
  # Output: 2020-01-12 10:40:38.367704
print(datetime.datetime.now())
  # Output: 2020-01-12 10:40:38.367743 
```

Both methods, `datetime.datetime.today()` and `datetime.datetime.now()` give us today's date including current date and time parameters. `datetime.now()` provides more precision.


## strftime()

The `strftime()` method allows us to create a string that represents the date and time in a more readable way. We can control the output format. This is very nice and helpful.

Here are some examples:

```Python
import datetime
print(datetime.datetime.today().strftime("%Y%m%d"))
  # Output: 20200312
print(datetime.datetime.today().strftime("%m/%d/%Y"))
  # Output: 03/12/2020
print(datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))
  # Output: 2020-03-12-10.59.53  
```

Feel free to take a look at the [Python documentation](https://docs.python.org/3/library/datetime.html) for more information on that module.
