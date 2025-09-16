To define a basic condition in Python we use the reserved keyword if, like so:


```python
if some_condition:
	print("do something")
```

In order for us to see `do something` in the output, the result of `some_condition` **must** be `True` - that is exactly how conditional statements work.



Let's flesh this out with a "real" bank example:


```python
money_in_bank = 300
transfer_amount = 50

if transfer_amount <= money_in_bank:
	print("Execute transfer")
```

Remember how expressions work. If we break the code down, in reality it looks like this:


```python
if 50 < 300:
	# ...

# since 50 < 300 is True then really we're saying:
if True:
	print("Execute transfer")
```

And therefore we will see `Execute Transfer` in the output!



If our condition was opposite, like this:


```python
if transfer_amount >= money_in_bank:
	print("??")
```

Then we would **not** see anything in the output because the **conditional statement** ( `transfer_amount >= money_in_bank` ) resolves to `False`