The value associated with a dict's key can be anything - including other dicts:


```
metrics = {
    "ram": {
        "size": 4,
        "status": "OK"
    },
    "disk": {
        "size": 512,
        "type": "SSD"
    }
}
```

As we see here, the `metrics` variable is a dict with two keys: `ram` and `disk`

The value of each of these keys is also a dict, with their own key-value pairs.



To access the `"status"` of the `"ram"`, for example, we would write this:


```
print(metrics["ram"]["status"]) # outputs: OK
```

You could re-write the above and break it down to steps, like this:


```
ram = metrics["ram"]
# now `ram` is a dict with two keys: size and status

print(ram["status"]) # accessing a dict's key normally
```

Remember, a dict is nothing more than a structure to keep our data organized.