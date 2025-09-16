In Docker, **image tags** are labels attached to container images that help identify specific versions, variations, or configurations of an image. They allow users to differentiate and reference different image versions or variations based on the tags assigned to them.

By default, when pulling an image without specifying a tag, Docker assumes the `latest` tag. This tag represents the most recent version of the image available in the repository.
```bash
$ docker pull python
Using default tag: latest
latest: Pulling from library/python
4eedd9c5abf7: Pull complete 
9cdadd40055f: Pull complete 
2a12d0031f3f: Pull complete 
24685c45a066: Pull complete 
6ba57ec00f34: Pull complete 
71bcc9787aa7: Pull complete 
Digest: sha256:30f9c5b85d6a9866dd6307d24f4688174f7237bc3293b9293d590b1e59c68fc7
Status: Downloaded newer image for python:latest
docker.io/library/python:latest
```
The above command pulls the latest version of the `python` docker image.

We can also notice the image SHA digest, and the full URI address:
- **Image SHA digest** is a unique identifier calculated from the contents of a Docker image. It represents the specific version and content of the image, providing a reliable reference for ensuring image integrity, version control, and reproducibility.
- The image full **URI address** is `docker.io/library/python:latest`.

It's important to note that relying solely on the `latest` tag may lead to unexpected behavior or compatibility issues, as it may change over time as new versions are released. Alternatively, you want to explicitly specify a version tag:
```bash
$ docker pull python:3.9.16
3.9.16: Pulling from library/python
918547b94326: Already exists 
5d79063a01c5: Already exists 
4eedd9c5abf7: Already exists 
9cdadd40055f: Already exists 
2a12d0031f3f: Already exists 
cea461a97d87: Pull complete 
a48c72dfa8c4: Pull complete 
c343b921680a: Pull complete 
Digest: sha256:6ea9dafc96d7914c5c1d199f1f0195c4e05cf017b10666ca84cb7ce8e2699d51
Status: Downloaded newer image for python:3.9.16
docker.io/library/python:3.9.16
```

# Semantic Version for Image Tags
While the image creator can decide the way she tags her images, many organizations (including the above `python` image you've pulled) follow a specific tagging method called [**semantic version**](https://semver.org/), or **SemVer**.

Take a look at the `python` image version: `3.9.16`. Each component has a specific meaning, given a version number `MAJOR.MINOR.PATCH`:
Increment the `MAJOR` version when you make **incompatible** API changes.
Increment the `MINOR` version when you **add functionality** in a backward compatible manner.
Increment the `PATCH` version when you make backward compatible **bug fixes**.