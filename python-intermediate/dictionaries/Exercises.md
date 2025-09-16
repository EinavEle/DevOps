## Exercise 1



Given the following code:
```
state = "France"

heads_of_states = {
    "Italy": {
        "president": "Sergio Mattarella",
        "prime minister": "Giuseppe Conte"
    },
    "India": {
        "president": "Ram Nath Kovind",
        "prime minister": "Narendra Modi"
    },
    "France": {
        "president": "Emmanuel Macron",
        "prime minister": "Edouard Philippe"
    }
}

print("The president of France is Emmanuel Macron and the prime minister is Edouard Philippe")
```

Modify the code so that the print statement at the end is not hard-coded, but rather uses the `state` variable along with the `heads_of_states` dict.

For example, if you change the value of state to be `"Italy"`, the `print` should output 
```shell
The president of Italy is Sergio Mattarella and the prime minister is Giuseppe Conte.
```


**Note**: there is **no** if-statement required for this; simply use the dict to access the relevant values!


<details>
<summary>Solution</summary>
<div> 

```python
# version 1
domain = "underworld"

gods = {
    "thunder": {
        "greek": "Zeus",
        "norse": "Thor"
    },
    "ocean": {
        "greek": "Poiseidon",
        "norse": "Aegir"
    },
    "underworld": {
        "greek": "Hades",
        "norse": "Hel"
    }
}

print("The greek god of", domain, "is", gods[domain]["greek"], "and the norse god is", gods[domain]["norse"])


# version 2
state = "Italy"

heads_of_states = {
    "Italy": {
        "president": "Sergio Mattarella",
        "prime minister": "Giuseppe Conte"
    },
    "India": {
        "president": "Ram Nath Kovind",
        "prime minister": "Narendra Modi"
    },
    "France": {
        "president": "Emmanuel Macron",
        "prime minister": "Edouard Philippe"
    }
}

print("The president of", state, "is", heads_of_states[state]["president"], "and the prime minister is", heads_of_states[state]["prime minister"])

```
</div>
</details>



## Exercise 2



Given the following code:
```
user_id = 3058
bonus_months = 3

user_months = {
    1552: 18,
    7021: 2,
    532: 12,
    3058: 9,
    1102: 4
}

print("Giving user " + str(user_id) + " an extra " + str(bonus_months) + " month bonus")
```

Add a line of code that updates the `user_months` dict. You should update the value of the key that matches `user_id`, by adding the `bonus_months` to the existing value.



**For example**, if you use the current values of `user_id` and `bonus_months`, then after your update, the value of the key `3058` will now be 12.

<details>
<summary>Solution</summary>
<div> 

```python
user_id = 3058
bonus_months = 3

user_months = {
    1552: 18,
    7021: 2,
    532: 12,
    3058: 9,
    1102: 4
}

print("Giving user " + str(user_id) + " an extra " + str(bonus_months) + " month bonus")

user_months[user_id] += bonus_months

print(user_months[user_id])
```
</div>
</details>




## Exercise 3



Create a dict called `country_populations`, it should be empty at first.

Add the following key-value pairs to `country_populations`:

- Ghana - 28
- Brazil - 209
- Mongolia - 3


Next, define a variable called `country` - it should be a string whose value is any of the above countries.

Finally, write a conditional statement that prints whether the country is big or small. Big countries have a population of at least 50.



For example, if the value of `country` is "Ghana", your conditional statement should output "Ghana is a small country".

Make sure you're only accessing the population through `country_populations`, and not writing it out yourself.


<details>
<summary>Solution</summary>
<div> 

```python
BIG_COUNTRY = 50

country_populations = dict()

country_populations["Ghana"] = 28
country_populations["Brazil"] = 209
country_populations["Mongolia"] = 3

country = "Brazil"

print(country, "is a big country") if country_populations[country] >= BIG_COUNTRY else print(country, "is a small country")

```
</div>
</details>



## Exercise 4



Given this code:
```
tomato = "Tomato Soup"
onion = "Onion Soup"
carrot = "Carrot Soup"

user_preferences = {
    "Sarah": tomato,
    "Sheila": carrot,
    "Fernando": tomato,
    "Jovan": onion,
    "Simona": carrot
}

soup_recipes = {
    tomato: "Get a bunch of tomatoes, cut them up, and throw them in boiling water",
    onion: "Be prepared to cry",
    carrot: "Find a rabbit, ask him how to make a carrot soup"
}

user = "Jovan"

print("Be prepared to cry")
```

Modify the code so that the `print` statement at the end is not hard-coded, but rather uses the `user`, `soup_recipes`, and `user_preferences` variables.

For example, if you change `user` to be `"Simona"` instead of `"Jovan"`, it should print `Find a rabbit, ...`



**Note**: there is **no** if-statement required for this; you should be able to do this in a single line that references both the dicts.

<details>
<summary>Solution</summary>
<div> 

```python
tomato = "Tomato Soup"
onion = "Onion Soup"
carrot = "Carrot Soup"

user_preferences = {
    "Sarah": tomato,
    "Sheila": carrot,
    "Fernando": tomato,
    "Jovan": onion,
    "Simona": carrot
}

soup_recipes = {
    tomato: "Get a bunch of tomatoes, cut them up, and throw them in boiling water",
    onion: "Be prepared to cry",
    carrot: "Find a rabbit, ask him how to make a carrot soup"
}

user = "Simona"

print(soup_recipes[user_preferences[user]])
```
</div>
</details>
