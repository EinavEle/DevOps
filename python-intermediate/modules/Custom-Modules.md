When we write a project, we want to break down our code into modules.

We can then create and import our own modules.

Each file we create in the script directory, will be a module we will be able to import.

Python knows by default to search for modules in the root file directory *(the directory of the file we will run)*.

How you ask? We will get to it later.

Let's take a look at the following structure:

    - main.py 
    - url_utils.py  
    - Person.py 

The file we will run is `main.py` and since all the other files are in the same directory we will be able to simply import them in `main.py` like this:
```python
import url_utils 
import Person 
```

But what if we have files inside a folder?

    - main.py 
    - utils   
      - url_utils.py  
    - Person.py 


In this case we will say that the `url_utils` **module** is inside the `utils` **package**.


### What is a package?
**In Python 3.3 and above, any folder.**
**In previous versions you had to include a `__init__.py` file.**

In order to use `url_utils` now, we will have to import it from the package:
```python
from utils import url_utils


url_utils.parse_url("https://translate.google.com/") 
```

Assuming `parse_url` is a function inside the `url_utils` module.

Another option would be:
```python
from utils.url_utils import parse_url


parse_url("https://translate.google.com/") 
```
Note that we use a `.` to separate between the 2 levels.

In python we mark a **package hierarchy level** (directory level) with a `.`
(In the cmd we might have written `utils/url_utils` but in Python imports `utils.url_utils`).

We also use a `.` to go up
- 1 dot `.` means - the same directory
- 2 dots `..` mean - 1 level up
- 3 dots `...` mean 2 levels up
- ... you get the point.


So if we have the following structure:

    - main.py 
    - utils   
      - url_utils.py 
    - data   
      - Person.py 

and we want to use the `parse_url` function in `url_utils` module from the Person module.

The import would look like that:
```python
# Person File
from ..utils.url_utils import parse_url 
```

So we are in `Person.py`. We use `..` to go up to the root directory, from that we want the `utils` package and from that we want the `url_utils` module, so we use a `.` to get it. Finally, after we got the module we wanted we can get the `parse_url` function.

## 

**It is important to note that the root folder is not considered a package.**

So, if this is your file structure:

    - main.py 
    - utils   
      - url_utils.py 
    - data   
      - Person.py 
    - errors.py 


you can't write in main.py:
```
from .errors import *  
```

In that case you will get an error:

    ModuleNotFoundError: No module named '__main__.erros';  '__main__' is not a package 


What you should do is simply specify the module name:
```
from errors import *  
```
