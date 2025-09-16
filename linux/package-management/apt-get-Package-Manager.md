Many Linux distributions use a package management system to install, remove, and manage software packages. Here are some commonly used commands for package management on Ubuntu:

`apt-get` is a command line tool that helps to handle packages in Ubuntu systems. Its main task is to retrieve the information and packages from the authenticated sources for installation, upgrade, and removal of packages along with their dependencies (the packages that your desired package depends on).

Generally, when first using `apt-get`, you will need to get **an index** of the available packages of public repositories, this is done using the command `sudo apt-get update`:
```bash
myuser@hostname:~$ sudo apt-get update
...
```
Note that the command doesn't install any package, so what just happened under-the-hood?

First, `apt-get` reads the `/etc/apt/sources.list` file (and any additional files under `/etc/apt/sources.list.d/`), which contains a list of [configured data sources and properties](https://bash.cyberciti.biz/guide//etc/apt/sources.list_file) to fetch packages from the internet. Then for each repository in the list, apt fetches a list of all available packages, versions, metadata etc... Package lists are stored under `/var/lib/apt/lists/`.

To install a package, just type:
```bash
sudo apt-get install <package-name>
```
When you run the above command, the package manager (in this case, `apt-get`) will search for the package in its local package lists (the ones stored under `/var/lib/apt/lists/`). These package lists are the catalog of available packages that can be installed on your system, in case the packages don't exist in the catalog, you won’t be able to install it. Thus, it is important to perform `sudo apt-get` update before every installation in order to update the local lists with all available packages in their latest version.

`apt-get` checks the **digital signature** of the files to ensure that it is valid and has not been tampered with. The signature is used to verify the authenticity and integrity of the repository and its contents. The concepts of digital signatures, data integrity and authenticity will be discussed later on in this course.