
1. Create a **PyPI group repo**, which contains both the proxy and hosted repo you've created in the previous sections. 

Note that the order of the repositories listed in **Ordered Group Repositories** is important. When the repository manager searches for a component in a group, it will return the first match. 
It's recommended placing hosted repositories higher in the list than proxy repositories within the list. 

2. Change the repo URL in `pip.conf` according to the new group repo URL.
3. Make sure you are able to install new packages after changing the repo URL.
