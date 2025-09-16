The script that is being executed is called the **top-level (or main scope) script**.

Since there is no `main()` function in Python, how would we be able to determine if a certain module is the main script?

In order to do so, we can use the built-in `__name__` variable:

```Python
# some_file.py
​if __name__ == "__main__":
  print("This is the main script") 
```

The print will be executed only if we ran this file.

If, for example, another file imports this file the print will not be executed.
