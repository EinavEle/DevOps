To remedy this, add the following code to your file (remember, before running the app):

```
@app.route('/')
def index():
  return "Someone has made a request and accessed the server. Exciting!"
```


Now, whenever the browser (or anyone) tries to visit ```localhost:3000/```, they have somewhere to go.

The above code is literally saying When someone makes a GET request to me*, invoke the following function - we'll talk about what / means in a minute.

* "me" in this case is app, the server

Save your ```server.py``` file, restart your server (remember, ```Ctrl + C``` then ```python server.py``` again in the terminal), and refresh the page. And now... voila!
We see the message in the browser.


This was the final part of building a basic server, to send a response.
The more formal way of sending a response is by using the Response object that we import from flask:

```
from flask import Flask, Response

@app.route('/')
def index():
  return Response("Someone has made a request and accessed the server. Exciting!")
```

Here we're using the Response object to respond to the client!

And that's it - that's the most basic server you can create.
If you want to see this work as a 'real' server, try using [**ngrok**](https://ngrok.com/download) and let someone else access your server as well.
In the simple example we just saw, a user can only go to [http://localhost:3000/](http://localhost:3000/) - that's like if people could only ever go to [google.com](google.com) - but often our site will be much more complex and have many routes.

For instance, [google.com](google.com) will take you to Google's landing page with the familiar search bar, but [google.com/maps](google.com/maps) will take you to their maps app, and you can guess where [google.com/calendar](google.com/calendar) will take you.

These ```/somewhere``` are known as routes, and we can add some to our app as well:

```
@app.route('/')
def index():
	return Response("Someone has made a request and accessed the server. Exciting!")


@app.route('/maps')
def maps():
	return Response("Here's some stuff related to maps")


@app.route('/shoobi')
def shoobi():
	return Response("This here is the shoobi *route*")
```





The "base" ``/`` is known as the root route - it has no specific name.

But if you change your code to look like the one above, save your file, then restart your server, you should be able to go to ```localhost:3000/```maps or ```localhost:3000/shoobi``` - and get each separate response.

