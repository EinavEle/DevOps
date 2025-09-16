With the init file we can make functions in subdirectories available in package level.

Let's look at an example.

Here is the structure of a project:

    - main.py 
    - config.py 
    - utils   
      - string_utils.py   
      - math     
        - fractions.py 
    - data   
      - users.py 

If we want to use a function from `fractions` module in the `main` module we would have to import it:
```python
# main.py
from utils.math.fractions import get_fraction 
```

This is a very long import.


Another option is to expose the `get_fraction` function in the `utils` package level.

In order to do that we need to:


1. Add an `__init__.py` file in the `utils` package :
 

    - main.py 
    - config.py 
    - utils   
      - __init__.py   
      - string_utils.py   
      - math     
        - fractions.py 
    - data   
      - users.py 


2. Import `get_fraction` function in `__init__.py` :

```python
# __init__.py
from utils.math.fractions import get_fraction  
```

3. Then, in `main.py` import `get_fraction` from the `utils` package :

```python
# main.py
from utils import get_fraction 
```

Now we can import `get_fraction` easily :)
