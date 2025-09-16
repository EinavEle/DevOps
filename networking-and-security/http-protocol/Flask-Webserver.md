So far we've seen how to communicate with a server as **clients**.

The below exercise demonstrates how a **server** might look and operate.

We'll run a simple Flask Python server, and communicate with the server locally from the same machine. The client will be the good old `curl`.

The Python server is based on a Python package called [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#). Let's install this package.
1. Click the **Terminal** button in the bottom bar to open a new terminal session in PyCharm.
1. Make sure that your terminal is using the Python interpreter resides in your venv:
    ```bash
    (venv) myuser@hostname:~/path/to/project$ which python
    /home/myuser/path/to/project/venv/bin/python
                ^^^^^^^^^^^^^^^^^^^^--------------- path to venv dir in your project files
    ```
1. Install the flask package by: `pip install flask`.
    In our shared repo, review the code in `simple_flask_webserver/app.py`. Above every function, you can find the server endpoint (e.g. `/upload`) and the curl command to request this endpoint.
1. In your terminal, `cd simple_flask_webserver`, and run the server by: `python app.py`.
1. The default endpoint `/` can be accessed using your browser. Use `curl` to trigger the other endpoints as specified in `app.py`.

Take a closer look at the output you've got from the `/api/upload` endpoint, this is the so-called **JSON** format. 

JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications. JSON can be used independently from JavaScript, and many programming environments feature the ability to read and generate JSON.