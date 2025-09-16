We saw how to concatenate strings:
```
"Hello " + "World"
```
of course we can concatenate also strings that are stored in variables:
```
hello_to = "universe"
"Hello" + hello_to
```

But when we want to use many variable in a string, it starts to become exhausting:
```
adjective = "sweet"
another_adjective = "wonderful"
noun = "world"


greeting = "Hello to my " + adjective + " and " + another_adjective + " " +  noun
```

In order to provide a better readable method, Python offers the `format()` function, which allows us to add placeholders for the content we would like to insert:
```
adjective = "sweet"
another_adjective = "wonderful"
noun = "world"


greeting = "Hello to my {} and {} {}".format(adjective, another_adjective, noun)
```

However, this method can still be complicated when handling long strings.

To overcome that, since Python 3.6 and on, it is possible to use f-string, using `f` prefix:
```
greeting = f"Hello to my {adjective} and {another_adjective} {noun}"
```
What we are actually doing here is evaluating the expression in the `{ }` and insert it in the exact place of the string.

So we can write in the `{ }` any valid python expression:
```python
greeting = f"Hello to my {adjective.upper()} and {'-'.join(list(another_adjective))} {noun}"
```
* Don't worry about what these functions and expressions, we will get to them later.

(If you are very curious, take a minute to read about it :) )