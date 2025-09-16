We saw how to do all kinds of imports:

For example:
```Python
from ..folder1.file1 import func1 
```

But how does the import system works?
Where do Python start from?


In order to answer that question we need to know how does the import system work, and especially where does it look for modules!

When Python needs to look for a module it follows this order:

1. Built-in modules
2. Directories listed in the sys.path variable


**Let's start with built-in modules.**

What are the built-in modules?
**These are modules that comes bundled with the python interpreter.**

A full list can be found like this:
```Python
import sys


print(sys.builtin_module_names) 
```

Let's continue to examine the `sys.path`

What directories are present there?
To see what directories are in `sys.path` you can simply print it:
```Python
import sys


print(sys.path) 
```

1. The top-level/root directory - the directory of the script we’re running (or the current directory if no file is specified).
2. A list of directories from `PYTHONPATH` env. variable.
3. Default `sys.path` location (installation dependent)
    -   On mac: `/usr/local/lib/python3.7/site-packages`.
    -  On windows: `/lib/site-packages` in your Python folder


What does all this mean?

First, it is important to understand that all the paths in our modules will be calculated from the root directory. (number 1 in the list).

In the `site-packages` folder we can find all the installed modules (we will talk about it soon).

We can even add a path manually:
```Python
import sys


sys.path.append("kuku/cookie/kushkush")  
```
