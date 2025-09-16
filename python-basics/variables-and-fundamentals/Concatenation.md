With some types of variables, we can bring two or more variables together in a process called **concatenation**. Here is an example:


```
name = "Jeniffer"
print("Hello there, " + name)
```

In this case, we are using the `+` operator to **concatenate** (bring together) the plain string `"Hello there, "` and the value of the variable `name`.

This process gives the output `"Hello there, Jeniffer"`



Of course, we can also concatenate multiple variables/strings together:


```
title = "Doctor"
print("Hello there, " + title + " " + name) # outputs: Hello there, Doctor Jeniffer
```

Note that we have to add the extra space: `" "` between `title` and `name`, because without them we would see: `DoctorJeniffer`


<hr/>


Like with other operators, we can create new variables from concatenation operations. Check this out:


```
first_name = "Isaac"
last_name = "Singer"

full_name = first_name + " " + last_name
print(full_name) # outputs: Isaac Singer
```

This is useful when we get information from separate places (for example, a signup form) and want to bring relevant pieces together.





## Concatenating with Numbers



In cases where you need to concatenate a string and a number, you will need to use the `str` operation.

This operation takes an expression and tries to convert it into a string. Here is an example


```
money_in_bank = 1200
bank_name = "Bank of Pythonica"

print(bank_name + " has " + str(money_in_bank) + " dollars") # outputs: Bank of Pythonica has 1200 dollars
```

Of course, you can put any valid expression between the `str`'s parentheses, for example:


```
bonus_money = 300
print(bank_name + " has " + str(money_in_bank + bonus_money) + " dollars") # outputs: Bank of Pythonica has 1500 dollars
```

Valid, if slightly odd code. Typically it's better to bring `money_in_bank` and `bonus_money` into a new variable, and use that with `str` instead.