When we talk about collections, another important distinguish is between ordered collection, which are called sequences and unordered collections.


The built-in sequences are:

- list
- string
- tuple
- range


The unordered collections are:

- dictionary
- set


It is important to know that because python sequences share many operators and functions.

So we might of seen a specific operation for a specific type.

For example, we can slice lists:
```python
numbers = [1,2,3,4,5]
first_two = numbers[:2] 
```

But, it is good to know that slicing is a sequence operation. In that case we can apply it for all sequences, meaning strings and tuples too.

Great! more tools to work with :)

---

So let's go over other sequence operations, and now we will know they apply to all sequences:


### Slicing

```python
word = "This is so cool"
part_of_it = word[-4:] 
```


### Concatenation

```python
nums = (1,2,3)
more_nums = nums + (4,5,6)

# OR

string = "this is" 
string += " not the end" 
```


### Duplication

```python
nums = (1,2,3)
duplicated = nums*2 
```

We already met some sequence functions when we talked about lists.

So, let's just mention them.

- count
- index

