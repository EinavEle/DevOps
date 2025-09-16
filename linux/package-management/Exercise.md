# Exercise - Playing with apt-get
1. Why do we need `sudo` to `apt-get update` and `install`? 
1. Perform `apt-cache show apache2` to see the local list of the `apache2` package on your system. 
1. Choose one of the versions from the above output (preferably not the latest version), and install  `apache2`, in this specific version. 
1. Perform `sudo apt-get` update. Was the list updated? Do you have some new versions of apache2 available to be installed? 
1. Upgrade `apache2` to the latest version.
1. Remove `apache2`.

<details>
  <summary>
     Solution
  </summary>

1. The reason we need to use `sudo` is because these commands make changes to files in `/etc` and `/var`, which belong to the root user. Thus, require root privileges to make changes to the system.
1. The output depends on each machine. Example for two available versions:

    - `2.4.31-4ubuntu3`
    - `2.4.41-4ubuntu3`

1. `sudo apt-get install apache2=2.4.31-4ubuntu3`
1. `sudo apt-get update` and after executing `apt-cache show apache2` again we can see a new version (the latest version) - `2.4.41-4ubuntu3.14`. 
1. `sudo apt-get upgrade apache2`
1. `sudo apt-get remove apache2`

</details>