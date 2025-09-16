# Sum of Squares

Find the sum of the squares (x in the power of 2) of the 4 largest even numbers in a list.

Given a list:

```python
numbers = [2, 3, 55, 4, 6, 8, 43, 10]
```
Your code should return `216`

<details>
<summary>Solution</summary>
<div> 

```python
def get_sum_of_squares(numbers):
    four_largest_even = sorted([x for x in numbers if x%2 == 0])[-4:]
    squares = [x**2 for x in four_largest_even]
    return sum(squares)    


assert(get_sum_of_squares([2,3,55,4,6,8,43,10]) == 216)
assert(get_sum_of_squares([-2,-3,-55,-4,-6,-8,-10]) == 120) 
print(get_sum_of_squares([2,33,43,46,57,83,64,78,24,98,52,77,22]))

```
</div>
</details>
