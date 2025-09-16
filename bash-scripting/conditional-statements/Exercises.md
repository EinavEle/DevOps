# Exercise 1 - Geo-location Info
Write a bash script `geo_by_ip.sh` that, given an ip address, prints geo-location details, as follows:
1. The script first checks if `jq` cli is installed. If not installed, it prints a message to the user with a link to download the tool: https://stedolan.github.io/jq/download/
1. The script checks that **exactly one argument** was sent to it, which represents the ip address to check. Otherwise, an informative message is printed to stdout.
1. The script checks that the given IP argument is not equal to `127.0.0.1`.
1. The script performs an HTTP GET request to `http://ip-api.com/json/<ip>`, where `<ip>` is the IP argument. The results should be stored in a variable.
1. Using the jq tool and the variable containing the HTTP response, check that the request has succeeded by checking that the `status` key has a value of `success`. The command `jq -r '.<key>'` can extract a key from the json (e.g. `echo $RESPONSE | jq -r '.status'`)
1. If the request succeed, print the following information to the user:
    - country
    - city
    - regionName

# Exercise 2 - Extended Availability test
Extending the above script to be more modular. Assume `availability_test.sh` is: 
```bash
curl google.com &> /dev/null

if [ $? -eq 0 ]
then
  echo "Request succeeded"
else
  echo "Request failed, trying again..."
fi
```
Change the script such that it can be working for any URL input from the user, in the following form:
```bash
myuser@hostname:~$ ./availability_test.sh google.com
…
myuser@hostname:~$ ./availability_test.sh cnn.com
…
myuser@hostname:~$ ./availability_test.sh abcdefg
…
myuser@hostname:~$ ./availability_test.sh
A valid URL is required
```