## Exercise 1

Given the following variables:


```
is_VIP = False
cash = 500
```

Write some code that outputs either

1. "Come on in"
  a. this should output only if is_VIP is True or if cash is at least 500
2. "Get out"
  a. this should output otherwise

<details>
<summary>Solution</summary>
<div> 

```python
is_VIP = True
cash = 400

print("Come on in") if is_VIP or cash >= 500 else print("Get out")
```
</div>
</details>


## Exercise 2

Given the following variables:


```
name = "John"

singer = "Lennon"
president = "Kennedy"
actor = "Travolta"

profession = # you decide which string: 'singer', 'president', or 'actor'
```

Write some code that adds the value of either `singer`, `president`, or `actor` to `name`, depending on the value of `profession`

There is more than one way to solve this (`elif`, multiple `if`s, with or without an `else`) - try a few ways to make sure you understand them all.

<details>
<summary>Solution</summary>
<div> 

```python
name = "John"

singer = "Lennon"
president = "Kennedy"
actor = "Travolta"

profession = "singer"   # you decide which string: 'singer', 'president', or 'actor'

if profession == "singer":
    name += " " + singer
elif profession == "president":
    name += " " + president
elif profession == "actor":
    name += " " + actor

print(name)
```
</div>
</details>


## Exercise 3
Tesla (the electric car company) is building a prototype for an AI salesperson. To do this, it needs you to code part of the flow of the initial conversation with the customer. The rules of the flow are as follow:



- If the customer has previously bought a Tesla, and the customer is a US citizen, the AI should check how long ago the customer bought their Tesla:
  - If the Tesla was bought fewer than four years ago, the AI should ask (console log) whether the customer would like an upgrade.
  - Otherwise, it should ask whether the customer is satisfied with the car.
- If the customer is not as US citizen but has bought a Tesla, the AI should ask whether the customer would like to move to the US.
- If the customer has not bought a Tesla, the AI should ask whether ze is interested in buying one.


You are given these inputs from each customer (these are dummy values)


```
bought_tesla = True
year_of_tesla_purchase = 2015
is_US_citizen = True
current_year = 2018
```

Once you write your code, make sure to change the values to to test that all the cases are working.

For the above inputs, your AI prototype should output "Would you like an upgrade?"

<details>
<summary>Solution</summary>
<div> 

```python
bought_tesla = True
year_of_tesla_purchase = 2015
is_US_citizen = True
current_year = 2018

if bought_tesla:
    if is_US_citizen:
        if current_year - year_of_tesla_purchase < 4:
            input("Would you like an upgrade? ")
        else:
            input("Are you satisfied with the car? ")
    else:
        input("Would you like to move to the US? ")
else:
    input("Are you interested in buying a car? ")


```
</div>
</details>
