## Money Conversion

You need to create a Python program that will be used in a money exchange booth in the airport, that converts Shekels to Euros. The program should get the exchange rate at the beginning of each run (a random number between 3.5 to 5.5) and number of Shekels received from the customer.

Ask for the user to insert the amount of Shekels they would like to exchange.

The program will print out the number of Euros that should be returned to the customer.

The program will disregard the cents when calculating the final result (they are used as commission to the booth’s clerk)

<details>
<summary>Solution</summary>
<div> 

```python
from random import uniform

exchange_rate = uniform(3.5, 5.5)   # random number between 3.5 to 5.5
amount_of_shekels = float(input("Please enter the amount of Shekels you would like to exchange:\n"))
amount_of_euros = int(amount_of_shekels // exchange_rate)

print(f"The amount of euros after the converting is {amount_of_euros}. The exchange rate is {exchange_rate}")
```
</div>
</details>
