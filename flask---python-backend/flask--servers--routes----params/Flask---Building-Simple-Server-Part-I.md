### FLASK
Flask is nothing more than a python package that allows us to create servers easily.

As such, go ahead and `pip install flask` for starters (you can create a new directory, or use an old one, up to you). Either way, create a server.py file, and let's import flask:

```
from flask import Flask
```

This should come as no surprise. We need to require every package we want to use.

By convention, we invoke Flask and store its value in a variable called app*:

```
app = Flask(__name__)
```

*Some people call this server instead, also sensible

Now if you take a look in ```app``` by executing:

```
print(dir(app))
```


you'll see that that's an object with a whole bunch of properties/methods.

One of the more interesting methods is the ```run``` method. We can invoke it like this:

```
port_number = 3000
if __name__ == '__main__':
	app.run(port=port_number)
```


Now - in your terminal, in the same directory where this file is - run the file: ```python server.py```
This will start a server that is listening on port 3000.

Listening for what? For requests. Remember this, and tattoo it across your back: servers are patient, responsive entities. They listen for requests, and only act when asked to. The requests can come from browsers, apps, code, Postman - wherever. The server doesn't care who is asking. It will respond.

Generally, this piece of code goes at the bottom of our ```server.py``` file - everything we add from now one should come before that. So, in fact this is the end of the file.

Now, if we go to ```localhost:3000```, we should see something like this:

![alt text](./flask01.png)

This might seem bad, but it is better than this error:

![alt text](flask02.png)

The error we're seeing is straightforward: when we try to go to ```localhost:3000```, we (technically the browser) are making a GET request. The browser is trying to get something from that address. However, our ```server.py``` file (which is the code running our server) looks like this:

```
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
	app.run(port=3000)
```


doesn't know how to respond.
We're not doing anything except for running a server - we haven't given it any instructions to respond to anyone!
