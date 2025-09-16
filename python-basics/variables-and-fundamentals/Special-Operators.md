There are other operators Python gives us which can be of use:



- `%` - modulo; helps us find the remainder in a division operation
- `+=` - "plus equals"; used for updating variables
- `-=` - "minus equals"; used for updating variables




## modulo



The `%` operator gives us the remainder of a division, for example:


```
print(5 % 2) # outputs: 1, because 2 goes into 5 twice, with 1 leftover
print(7 % 4) # outputs: 3, because 4 goes into 7 once, with 3 leftover 
```

This operator can be useful for determining whether a number is even or not, since all even numbers have a remainder of 0:


```
print(18291218174 % 2) 
# outputs: 0, therefore the number is even
```



## _equal



We can use any of the mathematical operators in conjunction with the equals sign to modify a variable's value quickly.

Take a look at this example:


```
litres = 50
litres += 25

print(litres) # outputs: 75
```

The above code is **exactly** equivalent to doing `liter = liter + 25`, but saves you the hassle of writing `liter` twice.

The `+=` operator says "take the value on the right, and add it into whatever is already in the left"



The same applies for `-=`, `*=`, and `/=`


<hr/>


Incidentally, we can also use the `+=` for concatenation:


```
name = "Jillian"
name += ", PhD"

print(name) # outputs: Jillian, PhD
```

Again, the above is exactly the same as doing this:


```
name = name + ", PhD"
```

But a little simpler.



Some other mathematical operators we should know are:

- `//` - Division (floor): divides the first operand by the second and rounds it down
- `**` - exponent (power): calculates first in the power of the second


When we divide 3 by 2 we get 1.5, which is a fractional number
```python
print(3/2) # 1.5
```
But sometimes we want the round number, meaning 1.

For that we can use the // operator:
```python
print(3//2) # 1
```

Finally the `**` operator will give us the exponent:
```python
print(2**3) # 8
```