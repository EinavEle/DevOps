If we want to *either* do something based on a condition, or do something otherwise, we need to use the `else` keyword, which looks like this:


```
if some_condition:
	print("Thing that happens")
else:
	print("Thing that happens otherwise")
```

An important note is that when you use an `if`-`else` statement, **only one** of the blocks will ever execute. It is an absolute either or situation:


```
if True:
	print("You will see this")
else:
	print("You will not see this")

# We could also say the following:

if False:
	print("Now this doesn't output")
else:
	print("But this will be output")
```

To summarize: we only have one condition when using `if`-`else`, and we define that condition after the `if` statement. If the condition resolves to `True`, then the `if` block will execute. Otherwise, the `else` block will execute.



Last note about `else` - it is **not** required to have an `else` with an `if`, but if you do have one it **has to come after** the `if` - that's just a syntax rule.