We saw that we can use Python built-in function, and Python built-in modules.

We can also create our own modules and use them.


But Python has much (much) more to offer. Many great packages have been written by great minds, and we can use some of these amazing tools and solutions instead of developing everything from scratch.


These packages are not installed by default when we install Python.

We need to install them ourselves.

How can we install them? With **PIP**.


**PIP is a package management system used to install and manage software packages written for Python** (but not necessarily in Python).

Many packages can be found in the **Python Package Index** ([PyPI](https://pypi.org/)) .


PIP is already installed if you are using `Python >= 3.4` downloaded from `python.org`.

To make sure you have pip installed you can run in the cmd:
```
$ pip --version 
```

**Great!** So how do we use it?


The pip command is executed from a command line terminal:

```console
$ pip install  
```

These are the basic installing commands:
```console
$ pip install SomePackage           # latest version
$ pip install SomePackage==1.0.4    # specific version
$ pip install SomePackage>=1.0.4    # minimum version 
```

When we are working on a project, we might install packages along the way:
```console
$ pip install flask  
```
and later on…
```console
$ pip install dj-database-url   
```
and later on…
```console
$ pip install whitenoise  
```
and later on…
```console
$ pip install Markdown  
```

But when a new user will join our project how will he know which packages to install?

We want a way to install all the dependencies at once.
For that, pip has the `requirements.txt` file.

It is a text file that is located in the project's root directory.


This file should contain all the requirements of the project.

It will look something like that:
```txt
# json packages 
json5==0.9.1 
jsonschema==3.2.0

# Jupyter related 
jupyter-client==5.3.4 
jupyter-core==4.6.2 
jupyterlab==1.2.6 
jupyterlab-server==1.0.6

# data analysis 
numpy==1.18.0 
packaging==20.1 
pandas==0.25.3 
```
Note that the syntax is similar to the installation syntax.


We can install all of the dependencies with:
```console
$ pip install –r requirements.txt 
```

To list all the packages that are installed use:
```console
$ pip freeze  
```

You can store all the dependencies listed by pip freeze in a requirements.txt file with:
```console
$ pip freeze > requirements.txt 
```

OK. You are ready to go!
