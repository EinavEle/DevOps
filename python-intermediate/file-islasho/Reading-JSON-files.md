JSON is a popular format for storing and sending data. It looks similar to a dict, though it has its own set of unique rules:


- Keys **have** to be surrounded by double quotes - no variables here
- String values **have** to be surrounded by double quotes; not single
- No trailing commas (i.e., the JSON "dict" can't end with a comma)
- No comments


Because JSON is so widely used, Python has a built-in command to read JSON data. To code along with this example, create a `turtles.json` file and copy [this data](https://github.com/Elevationacademy/python-spotcheck-solutions/blob/master/File-IO/turtles.json) into it.


Once you have the file with the data ready, this code will read the JSON:
```python
import json
the_file = open("turtles.json")
turtles_data = json.load(the_file) 
```

Notice the import json line - this tells Python that we want to use its built-in JSON functionality. This line *has* to be at the top of the file any time we want to work with JSON data.


Also notice that we are loading the file - that means, not only we are **reading** it, we're also telling Python to turn it into a dict that we can handle. As such, if we run this command:

```python
print(turtles_data[0]['gender']) 
```

We should see the gender of the first turtle - in this case, "female"


So now we have this `turtles_data` list that works like any other list in Python - nice.
