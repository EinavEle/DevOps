Write a Python program that receives a line of text (string) and returns the 5 most common words.



For example, for the following test case:
```
line = "wee wee goo koo goo doo doo so go go yo yo yo yo fo zo"
print(get_5common(line))
```

The output will be:

[('yo', 4), ('doo', 2), ('go', 2), ('wee', 2), ('goo', 2)]



The order might be different.


<details>
<summary>Hint</summary>
<div> 
Read about defaultdict, it might come handy, especially in this exercise.
</div>
</details>

<details>
<summary>Solution</summary>
<div> 

```python
from collections import defaultdict


def get_5common(line):
    words_counter = defaultdict(int) # using the default of the type(int) which is 0

    for word in line.split():
        words_counter[word] += 1
    pair_array = [(k,v) for k,v in words_counter.items()]
    most_common_words = sorted(pair_array, reverse=True, key=lambda pair: pair[1])
    return most_common_words[:5]

line = "wee wee goo koo goo doo doo so go go yo yo yo yo fo zo"
print(get_5common(line))
```
</div>
</details>

<details>
<summary>Solution 2</summary>
<div> 

```python
from collections import Counter

def five_high_freq(text):
    line = text.split()
    return Counter(line).most_common(5)
  

line = "wee wee goo koo goo doo doo so go go yo yo yo yo fo zo"
print(five_high_freq(line))
```
</div>
</details>
