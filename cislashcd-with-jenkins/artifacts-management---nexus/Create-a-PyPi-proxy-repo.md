
1. After signing in to your Nexus server as an administrator, click on the **Server configuration** icon.
2. Create a [PyPi proxy repo](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories).
3. On your machine, in some local Python venv, [configure](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories#PyPIRepositories-Download,searchandinstallpackagesusingpip) `pip` to download packages from your private artifact repository. To do so, create a file `pip.conf` with the following content:
```text
[global]
trusted-host = localhost:8081
index-url = http://localhost:8081/repository/<repo-name>/simple
index = http://localhost:8081/repository/<repo-name>
```

4. Put the `pip.conf` file either in your virtual env folder (`venv`). Alternatively (when installing packages outside a virtual env, e.g. in a Jenkins agent), define a custom location by setting the following env var: `PIP_CONFIG_FILE=<path-to-pip-conf>`. Note that there are many [other methods](https://pip.pypa.io/en/stable/topics/configuration/#location).
5. Install `flask`. Make sure you see the package when browsing the repo content. 

## Repository Health Check

[Repository Health Check (RHC)](https://help.sonatype.com/repomanager3/nexus-repository-administration/repository-management/repository-health-check) allows Nexus Repository users to identify open source security risks in proxy repositories at the earliest stages of their DevOps pipeline.

New vulnerabilities report is updated every 24 hours.

If you’re running Nexus Repository **Pro**, you can see a detailed report.

### Test it

1. Enable RHC by clicking the **Analyze** button on the relevant repository in **Repositories** page.
2. Try to install the [`insecure-package`](https://pypi.org/project/insecure-package/) pip package, this package contains built-in software vulnerability. Watch how Nexus recognizes the vulnerability.
