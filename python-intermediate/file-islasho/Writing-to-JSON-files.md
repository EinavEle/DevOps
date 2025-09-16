Writing to JSON is similar to writing to other files. However, because JSON is a format that has to be read in its entirety to be "understood", if we want to **add** to an existing JSON file, we first have to read it - which we already know how to do:

```python
the_file = open("turtles.json")
turtle_data = json.load(the_file) 
```

Now that we have the data, we write to the file:

```python
with open("turtles.json", "w") as the_file:
  turtle_data.append({"test": 0})
  json.dump(turtle_data, the_file) 
```

Notice that here we're opening the file, and passing the w argument - this is short for **write**, and it will **overwrite** the entire file!

Thankfully, we already have all the data in `turtles_data`, and all we're doing is adding a simple dict: `{"test": 0}`


The `json.dump` command is what ultimately writes to the file, and it needs two things: what to write (turtles_data), and where to write it (the_file). Once you run the commands above, you can take a look at the `turtles.json` file and see the new dict at the end for yourself.


**Note:** you'll be using this file later, so **remove that new dict** after you checked that it works (just delete it manually from the file.)

---

Writing an entirely new JSON file is a little simpler, because we don't have to read anything first:

```python
some_data = {"animal": "Lion", "job_description": "King"}
with open("new_file.json", "w") as f:
  json.dump(some_data, f) 
```

The dump command works the same here the f - the file - is where we're writing the data, and some_data is what we're writing to the file.
