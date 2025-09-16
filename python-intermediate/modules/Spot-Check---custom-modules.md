
**Let's practice some imports!**


Assuming you have a project with the following structure:

    - main.py
    - config.py
    - utils
      - string_utils.py
      - math
        - fractions.py
    - data
      - users.py 


1. In the `config` file define:
```import
password = "1sd2fe3" 
```

Now go to the main file and print it (of course you will need to import it first).


2. In the `users.py` define:
```import
admin = "Momo" 
```

Now go to the main file and print it.


3. In the `string_utils` module write a function that returns the **first character of a string**.

In the fractions module call this function with the string "import" and save the result in a variable called first. Finally in the main, import and print the `first` variable.


Now run the main module.

You should get:


    1sd2fe3 
    Momo 
    i 


Check out the solution [here](https://github.com/Elevationacademy/python-spotcheck-solutions/tree/master/Modules/imports-spot-check).
