Create a `Rectangle` class that receives a `width` and a `height` in its constructor. It should also have two methods:

- `calculate_area` which returns the product of the `width` and `height`
- `calculate_perimeter` which returns the perimeter of the rectangle:  `2∗length + 2∗width`


Next, create a class called Square which inherits from Rectangle. It should have its own init which receives only one parameter: length, and pass length twice to its parent (remember, a square is a rectangle but all sides are equal).


Also, Square should implement its own, simpler `calculate_perimeter` method.


If you've done it right, the following code should work:

```python
s = Square(2)
print(s.calculate_perimeter()) # outputs: 8
print(s.calculate_area()) # outputs: 4 
```

Try this out for a few minutes then see [this solution](https://github.com/Elevationacademy/python-spotcheck-solutions/blob/master/OOP-Inheritance/sc1.py).
