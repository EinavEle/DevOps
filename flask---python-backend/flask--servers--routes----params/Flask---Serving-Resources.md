So far our routes have been serving nothing more than simple strings and objects. This is important, because we want our servers to serve data - but we promised that servers could also serve files.

To show how this works, go ahead and create a folder called public, and inside of it add an image file.

The public folder is a directory that our server will serve to whoever asks. The name public is just a convention - other developers will call this folder client, build, or dist - they're all fine choices.

And now, to serve the file, and all other file that we will put in the public directory, add the following lines to your server.py file:

```
app = Flask(__name__, static_url_path='', static_folder='public')
```



Here we're defining 2 parameters:

- `static_url_path` - The url for requesting static files. Here it is defined as root, so we can ask for static files from the root url.
- `static_folder` - the folder that contains the static files.

In order to request the image file, we just need to specify it's path:
So if we added a tree.jpeg to the public directory, the path to get it will be 
```
http://127.0.0.1:3000/tree.jpeg
```

Here we defined a parameterized route (a route with a parameter), where the parameter is the file path. Then we are using the flask send_static_file method to send the file back to the client.

Let's add one small validation before we continue to more awesome features.
Flask has a mechanism to validate the type of the parameter we are defining.
The available types are:
**string**: Accepts any text without a slash (the default).
**int**: Accepts integers.
**float**: Accepts numerical values containing decimal points.
**path**: Similar to a string, but accepts slashes.

In our case we will want to use the path type, so our code will now look like this:

```
@app.route('/<path:file_path>')
def serve_static_file(file_path):
  return app.send_static_file(file_path)
```


Note that we have a slightly different syntax. When we defined the parameter `file_path` we also defined it's type - path, like this: `path:file_path` so path is the type and `file_path` is the name of the parameter.

And now, save your file, restart your server, and go to `localhost:3000/` - and voila, your first served application.



