Add a `get_menu` method to your `Restaurant` class that prints either `We have meat` or `We have vegetables` depending on the value of `is_vegetarian` - remember to use self

Here is a solution to check your code.


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

    def get_menu(self):
        if self.is_vegetarian:
            print("We have vegetables")
        else:
            print("We have meat")

r1 = Restaurant("Zoozaazo", 4, False)
r2 = Restaurant("Top La Pompei", 3, False)
r3 = Restaurant("El Viego", 5, True)

r1.get_menu() # outputs: We have meat
r3.get_menu() # outputs: We have vegetables
```
</details>
