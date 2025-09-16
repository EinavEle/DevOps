This, therefore, is one of the most basic servers you can create to serve a web application:

```
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='public')

@app.route('/<path:file_path>')
def serve_static_file(file_path):
  return app.send_static_file(file_path)

if __name__ == '__main__':
	app.run(port=3000)
```


Notice that to serve a simple bundle of files, we don't even need any routes!
Generally, we use routes to serve data.


Maybe [**Serveo**](https://serveo.net/) or [**ngrok**](https://ngrok.com/) to show off an old project to someone..?
So now we can host our apps through a server, but the only way we know to access the server (either routes or files) is through the browser.

But of course, the browser is just making a GET request to whichever route we give it.
Let's use python code to send HTTP requests to the server. As there are many APIs out there, it is very common for a server to send an HTTP request to another server. Of course a client (web, mobile or desktop application) can also send a request to the server.

How will we do it?    With a python library of course!
There are a few options, we will use the python requests library.

To put this to practice, we're going to create our own mini-Google-books-API:

We will run a python file that will send a request to our server requesting information about a book.
We will use a user input to get the id of the book, and then we will send a HTTP request asking for information about that book.
Now, let's add another python file client.py
First thing we want to ask the user to insert a book id, and just to validate let's print it:

```
print('Enter a book id:')
id = input()
print(id)
```


Now let's use the requests library to send a request to our server
make sure to install ( pip install requests ) and import the requests package( import requests ).

```
import requests

books_url = 'http://localhost:3000/books/{}'.format(id)
res = requests.get(url=books_url)
print(res.json())
```


First we compose the endpoint, and store it in books_url, then we make a get request.
Finally, we will extract the data we got back from the response object by using res.json()

This code makes a GET request to `/books/the-id-the-user-input` - yes, we are creating our route dynamically - and yes, we are making a GET request to our own server!

This is very exciting! We can send requests to our server or to other servers.
