# Exercises 1 - Dated Copy
Create a script that takes a valid file path as the first argument and creates a dated copy of the file. 
For example:
```bash
myuser@hostname:~$ ./datedcp.sh myfile.txt
myuser@hostname:~$ ls
2022-04-30_myfile.txt
```

# Exercise 2 - Theater Night Out Booking System
In our shared repo, copy the file under `theatre_nighout/init.sh` into an empty directory and execute it. This script creates 5 directories, each for a famous theater show. In each directory there are 50 files, representing 50 available seats for the show. Create a bash script `available_seat.sh` that takes one argument which is the name of a show and prints the available seats for the show (by simply using `ls` command). Create another bash script `booking.sh` that takes two arguments - the name of a show and a seat number. The selected seat should be marked as booked by deleting the file that represents the seat number. You should print an informative message to the user upon successful or failed booking. You can always re-run `init.sh` to test your script again. 
For example:
```bash
$ ./init.sh && cd shows
$ ./available_seat.sh Hamilton
Available seats for Hamilton:
1 2 3 4 5 6 7 8 9 10 ... 48 49 50
$ ./booking.sh Hamilton 5
Seat 5 for Hamilton has been booked!
$ ./available_seat.sh Hamilton
Available seats for Hamilton:
1 2 3 4 6 7 8 9 10 ... 48 49 50
$ ./booking.sh Hamilton 5
Error: Seat 5 for Hamilton is already booked!
```

<details>
  <summary>
     Solution
  </summary>

```bash
#!/bin/bash

# available_seat.sh
echo "Available seats for $1:"
ls "$1"
```
```bash
#!/bin/bash


show_name=$1
seat_number=$2

rm "$show_name/$seat_number" && echo "Seat $seat_number for $show_name has been booked!" || echo "Error: Seat $seat_number for $show_name is already booked!"
```

</details>

# Exercise 3 - Env Variable Setter
Create a script that takes two positional arguments: the first argument should be an uppercase **name** and the second argument should be a file **path**. The script should define an environment variable named after the provided **name**, and set the content of the variable to the contents of the file located at the provided file **path**.
E.g.
```bash
source ./script.sh  ./example.txt VAR
source ./script.sh  /home/user/documents/test.txt FOO
source ./script.sh  /etc/config.txt SETTINGS
```

<details>
  <summary>
     Solution
  </summary>

```bash
#!/bin/bash

filepath=$1
varname=$2

content=$(cat "$filepath")
export "$varname"="$content"
```

</details>

# Exercise 4 - User Commands
Write a script that takes a command as user input and executes it, capturing the output in a variable, and then prints the output to the terminal. Usage example:
```bash
myuser@hostname:~$ ./myscript.sh ls
demo.yml
hi.sh
server
server.c
myuser@hostname:~$ ./myscript.sh “echo hello”
hello
```

<details>
  <summary>
     Solution
  </summary>

```bash
#!/bin/bash

COMMAND=$1
OUTPUT=$($COMMAND)
echo "$OUTPUT"
```

</details>