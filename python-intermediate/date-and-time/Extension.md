
## Birthday
### Instructions:

Use `datetime` module to write a program that:

1. Takes a birthday as input from the user in DD-MM-YYYY format (e.g. 25-03-1995).
2. Print the age of the user.
3. Print the number of days, hours, minutes, seconds and microsecond until the next birthday.





<details>
  <summary>
     Hints
  </summary>

  <li>Use <b>strptime()</b>  method from datetime module. </li>
  <li>Check how to get the year part from the date. </li>
  <li>Use replace() method from datetime module for calculating the next birthday. </li>
</details>




<details>
  <summary>
     Solution
  </summary>

```Python
    from datetime import datetime

    birthday = input("Please enter your birthday in DD-MM-YYYY format: ")
    date_format = "%d-%m-%Y"
    birthday_datetime = datetime.strptime(birthday, date_format)
    today = datetime.today()
    print("Your age is:", today.year - birthday_datetime.year)
    next_birthday = birthday_datetime.replace(year=today.year)
    
    if next_birthday < today:
      next_birthday = birthday_datetime.replace(year=today.year + 1)
      time_until_next_birthday = next_birthday - today  print("The time until the next birthday is:", time_until_next_birthday) 
```

</details>




