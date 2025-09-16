
### An overview of packaging for Python

Let's say you develop and maintain a Python package called `fantastic_auth` which responsible for authentication aspects in your application.
This package is aimed for internal use in different microservices. It is being used by other teams in your organization, which can install it by `pip install fantastic_auth` as part of their build process. 

Since this package should be used from within your organization only, there is no point store it in PyPI, which is the public Python Packages Index, but we would like to store and manage it in our private Nexus repo.  

1. Create two `pypi (hosted)` repos, call them `pypi-releases` and `pypi-snapshot`.  

   - **Releases** repo is intended to be the repository where your organization publishes **internal releases**.   
   - **Snapshots** repo is intended to be the repository where your organization publishes internal **development versions**, also known as snapshots.

Under `fantastic_auth`, you are given a sample source code for the library.
As you can see, in order to turn a directory with python files into a Python package, 
we need to add some necessary files and organize directory structure in a specific format.

The most important file is `setup.py` which exists at the root of your project directory.
This file configures some aspects of your project. Take a look at it.

Complete the below steps to build the package:

2. Install `build` library by `pip install build`, which is a simple build "frontend".
   [build](https://pypa-build.readthedocs.io/en/latest/) reads the `fantastic_auth/pyproject.toml` file and invokes the build "backend" as configured there ([setuptools](https://setuptools.pypa.io/en/latest/index.html) in our case).

3. Open a terminal in the library root directory, build the package by: `python -m build`.    
   This will build the package in an isolated environment, generating two formats under the `dist/` dir: a source-distribution (`.tar.gz`), and wheel (`.whl`).

   - **Source-distribution** (or `sdist` for short) is a format that contains the source code in pure Python files, along with setup and build scripts.
     When installed, these packages are **built and compiled** on the target system.
   
   - **Wheel** (of `whl` for short) is a binary distribution format that contains **pre-compiled**, platform-specific versions of a Python package.
     whl packages are typically faster to install because they don't require compilation on the target system. 
   
   `pip` always prefers wheels.

4. Finally, it's time to upload your package to Nexus. We will use [twine](https://twine.readthedocs.io/en/latest/) to upload the package. Install Twine by: `pip install twine`.
5. In order to upload your package to the PyPI repo in Nexus, configure the `fantastic_auth/.pypirc` file [as describe in Nexus docs](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories#PyPIRepositories-Uploadtoahostedrepositoryusingtwine).
6. Run Twine to upload all archives under `dist/` by:
   ```bash
   python3 -m twine upload --config-file .pypirc --repository pypi-releases -u <nexus-username> -p <nexus-password> dist/*
   ```
7. Observe the uploaded packages in Nexus server.
