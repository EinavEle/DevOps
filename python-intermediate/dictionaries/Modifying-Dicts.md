## Adding key-value Pairs

Once a dict is created, we can still add keys to it:


```
exam_scores = {}

exam_scores["Nick"] = 82
exam_scores["Andrew"] = 85
exam_scores["Jessi"] = 91
exam_scores["Missy"] = 96
```

Even though we started with an empty dict, we've populated it with lots of data post-definition.

Adding key-value pairs is straightforward: access the dict at the new key, and assign it a new value.



If we run `print(exam_scores)` we will see this in the output:


```
{'Nick': 82, 'Jessi': 91, 'Missy': 96, 'Andrew': 85}
```

There is no difference between dicts created statically or dynamically, so everything else you know about dicts applies here as well!





## Updating Values



Similar to adding new keys-value pairs, we can also modify existing values by accessing their key:


```
exam_scores["Andrew"] = 87
```

It looks exactly like adding a new key-value pair, **but** in this case `"Andrew"` is already a key, so Python will simply update its value.

<hr/>



Because we're dealing with normal strings/numbers/data in dicts, we can even modify values like this:


```
exam_scores["Missy"] += 3
```

This will look at the current value associated with the key "Missy", and add 3 to it, so now if we print(exam_scores) we'll see:


```
{'Nick': 82, 'Jessi': 91, 'Missy': 99, 'Andrew': 87}
```

Now Missy is still there, but with her updated score. Good job Missy, you deserve that score.



There is another way of updating multiple values at once:
```
values_to_add = {"1": 'complete number', "0.5": 'half', "0.25": 'quarter'}
numbers = {'pi': 3.14159265359, 'phi': 1.6180339887, "1": 'complete'}


numbers.update(values_to_add)
print(numbers)
```

`update()` adds all the pairs from the given dictionary (values_to_add) to the target dictionary.

Note that it overrides existing values, so the value of numbers["1"] is now "complete number".