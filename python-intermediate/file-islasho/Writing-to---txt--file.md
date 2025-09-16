When you write to a text file, you will either write to an existing file, or create a new one altogether and write data there.


For both operations we need to introduce a new keyword: `with`

The exact nature of with is out of scope for this lesson, but its use is straightforward:

```python
with open('example.txt', 'a') as the_file:
  the_file.write("Pineapple\n") 
```

A few things going on here:

- We're opening the file as usual, using `open`
- We pass a second parameter to the open command: `'a'` - this is short for **append**
- Thus we will be adding to this file, and not creating it
- We "alias" our file using the as keyword; this is similar to defining a variable
- The `write` command which - as you expect - writes to the file
- The `\n` at the end of the text to append (Pineapple)
- We're adding this so that any text we add thereafter goes on to the next line and not on the same line as the last item


Any write operation we want to execute **must** be inside the with block (i.e. indented), because once this block finishes executing, the files **closes** automatically and we cannot write to it without executing open again.

---

If, instead of adding to a file, we wish to create a new one and write to it, we simply replace the `'a'` with a `'w'` - short for write:

```python
with open("new_file.txt", "w") as the_file:
  the_file.write("good text\n")
  the_file.write("great text\n")
  the_file.write("The Best Text\n") 
```

The above code creates a new file called new_file.txt, and then writes three lines of text into it, line after line
