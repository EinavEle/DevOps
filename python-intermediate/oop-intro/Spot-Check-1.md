Write your own class, Restaurant, that has three attributes: `name`, `ratings` (a number), and `is_vegetarian` (a boolean).

Next, create a few instances to make everything works:
```python
r1 = Restaurant("Zoozaazo", 4, False)
r2 = Restaurant("Top La Pompei", 3, False)
r3 = Restaurant("El Viego", 5, True) 
```

If you `print(r3.ratings)` it should output `5`

Feel free to use the previous parts of the lesson to remember the syntax, and see the solution as an example when you're done.


<details>
  <summary>
     Solution
  </summary>

```python
    class Restaurant:
      def __init__(self, name, ratings, is_vegetarian):
        self.name = name
        self.ratings = ratings
        self.is_vegetarian = is_vegetarian

    r1 = Restaurant("Zoozaazo", 4, False)
    r2 = Restaurant("Top La Pompei", 3, False)
    r3 = Restaurant("El Viego", 5, True)
```
</details>
