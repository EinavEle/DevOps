Head over to [this link](https://github.com/Elevationacademy/python-spotcheck-solutions/blob/master/File-IO/attendance.txt) and copy the list of names into a file called `attendance.txt`


Write some code that creates a dict of "attendance", i.e. how many times each name appears on the list.


To do this you'll need to:

- Create an empty dict called `student_attendance`
- Read the file
- Loop through all the names
- For each name, if it exists in `student_attendance`, increase its value by 1
- Otherwise, add it as a key to the dict with an initial value of 1


If you've done it correctly, when you `print(student_attendance)` you should see this

```python
{
  'Timothy': 5, 'Quincy': 3, 'Claude': 2, 'Barry': 7,
  'Douglas': 4, 'Mason': 5, 'Ira': 2, 'Flynn': 4,
  'Curtis': 3, 'August': 5, 'James': 1, 'Jude': 5,
  'Sawyer': 3, 'Lyle': 3, 'Raleigh': 5, 'Harley': 3,
  'Austin': 8, 'Spencer': 4, 'Elliot': 4, 'Neil': 4,
  'Noah': 3, 'Aidan': 2, 'Owen': 5, 'Murray': 4,
  'Roy': 3, 'Gary': 3
} 
```

**Note:** make sure both the .txt file and your code are in the same directory, **and** that you're executing your code from the same directory.


Try this for at least 15 minutes. If you're still stuck, or just want to compare - here is a [solution](https://github.com/Elevationacademy/python-spotcheck-solutions/blob/master/File-IO/sc1.py).
