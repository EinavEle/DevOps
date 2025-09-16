What happens if we want to write a string that contains quotes, something like:

<span style="background: lightgray; padding:7px">He said: "Hello"</span>

obviously we can't write it straight forward:
```
 "He said: "Hello""
 ```
In that way we are closing the first string before `Hello` and creating a second empty string after it, not to mention we will get an error.

Worry not, because there is a solution, called **escaping**.

For some characters that have special meaning like `"`, if we want to use it in its non-special meaning we just add a `\` before:
```
print("He said: \"Hello\"")
```
There are a few other cases, for example if we want to add a line break (start a new line) in the middle of a string:
```
print("first line \nsecond line")
```

OK. I think you got the idea.

Feel free to investigate other types of escaping.