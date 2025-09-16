Say we have this list of dicts:


```python
vacation_sites = [
    {"name": "Hotsplace", "avg_temp": 32},
    {"name": "Warmsvenue", "avg_temp": 24},
    {"name": "Fairsplace", "avg_temp": 25},
    {"name": "Coldsburrow", "avg_temp": 20},
    {"name": "Shiversland", "avg_temp": 12}
]
```


And we're only interested in the dicts whose `avg_temp` is higher than 24.

We could write code that looks like this:


```python
def filter_sites(sites):
    my_sites = []
    for site in sites:
        if site["avg_temp"] > 24:
            my_sites.append(site)
    return my_sites


filtered = filter_sites(vacation_sites)
print(filtered)
```

Now, there's nothing wrong with this code... but we could also write it like this:


```python
def is_site_warm(site):
    return site["avg_temp"] > 24


filtered = list(filter(is_site_warm, vacation_sites))
print(filtered)
```

Wow.



Let's break down what `filter` is:

- A built-in function in Python, i.e. we don't have to define it
- It takes two parameters:
  - a function that receives one parameter and returns a boolean
  - a list
- It returns a new list


In terms of how `filter` works, here is what it does:

- Take each item in the list you gave it
- Pass each item as a parameter to the function you gave it
- Keep only the items that return `True` from the function


Visually you can think of it like this:


```python
filter(function_that_filters, list_of_items)
```

In our example, our `function_that_filters` is `is_site_warm`, and our `list_of_items` is `vacation_sites`

What the `filter` function does is take each item inside of `vacation_sites`, invokes `is_site_warm` with that item, and if it returns `True`, then we keep that item. It is literally **filtering** our data for us.



Nice.

<hr/>

**Small Note**: if you need to access the result of a `filter` as a list, you'll sometimes have to wrap it in the `list`  function, like this:

```python
list(filter(a_function, a_list))[0]
```
The `list` function converts a filter result into a usable list.