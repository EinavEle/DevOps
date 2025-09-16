
Nexus ships with a great [Official docs](https://help.sonatype.com/repomanager3/nexus-repository-administration/repository-management) and compatible with [many package managers](https://help.sonatype.com/repomanager3/nexus-repository-administration/formats): Java/Maven, npm, NuGet, PyPI, Docker, Helm, Yum, and APT.

### Repository Types

#### Proxy repo

Proxy repository is a repository that is linked to a remote repository. Any request for a component is verified against the local content of the proxy repository. If no local component is found, the request is forwarded to the remote repository.

#### Hosted repo

Hosted repository is a repository that stores components in the repository manager as the authoritative location for these components.

#### Group repo

Repository group allow you to combine multiple repositories and other repository groups in a single repository.
This in turn means that your users can rely on a single URL for their configuration needs, while the administrators can add more repositories and therefore components to the repository group.
