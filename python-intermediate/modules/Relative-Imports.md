Let's say we have the following structure:

    - utils
      - string_utils.py
      - math
        - fractions.py
        - polynomials.py
    - data
      - users.py 


If `polynomials` module had to import `fractions` module it could use an absolute import:
```python
import utils.math.fractions 
```
specifying all the packages from the root of the project.

Another way is:
```python
from utils.math import fractions  
```

You can see that if we had a complex folder structure, those absolute paths could be very long and tiering.

In this case, it is good we also have relative imports:
```python
from . import fractions 
```

The **dot** means *"this directory"*, in our case the math package.

In relative paths we calculate the path from out current location, and not from the root directory.


Although absolute paths are strongly recommended, there might be some cases where deep in the packages hierarchy it is simpler to use a relative path.

You can read more about it in the PEP documentation.
