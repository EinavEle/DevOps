The time module provides different time-related functions.


To use this module we need to import it first: `import time ` 


When dealing with Python we have to know that the time module is based around what is known as **epoch** - the point where the time begins. For Unix system is the `January 1, 1970, 00:00:00`.


Let's look at this code:

```Python
import time
print(time.time())
  # Output: 1583755084.906643
print(time.ctime())
  # Output: Mon Mar  9 13:58:04 2010  
```

In the code above:
- `time.time()` gives the seconds passed since 12:00 am, January 1, 1970
- `time.ctime()` gives the current time and date


## sleep

```Python
time.sleep(x) 
```

Important function in the time module is sleep. sleep suspends the calling thread for x seconds. For now we won't talk about threads so let's think about it as a program suspension for x seconds.


Try this code:

```Python
print(1)
time.sleep(5)
print(2) 
```

Can you see what happened on screen?
<details>
<summary>Click here to see the answer</summary>

First "1" appeared in the screen and after 5 seconds number "2" appeared.

</details>

---


Feel free to take a look at the [Python documentation](https://docs.python.org/3/library/time.html) for more information on that module.
