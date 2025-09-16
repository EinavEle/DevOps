Sometimes, docker images can contain security vulnerabilities, either by using a vulnerable base image or by installing insecure packages. Docker image security scanning is a process of identifying known security vulnerabilities in the packages listed in your Docker image. This gives you the opportunity to find vulnerabilities in container images and fix them before deploying images to production environments.

The [Snyk](https://docs.snyk.io/products/snyk-container/snyk-cli-for-container-security) Container command line interface helps you find and fix vulnerabilities in container images on your local machine.
1. You must first [Sign up for Snyk account](https://docs.snyk.io/getting-started/create-a-snyk-account).
1. Install [Snyk CLI](https://docs.snyk.io/snyk-cli/install-the-snyk-cli).
1. Get your API token from your [Account Settings](https://app.snyk.io/account) page.
Use `sync auth` to authenticate in Snyk API. Alternatively, set the `SNYK_TOKEN` environment variable with the API token as a value.
1. You can easily [scan docker images](https://docs.snyk.io/products/snyk-container) for vulnerabilities:
```bash
# will scan ubuntu docker image from DockerHub
snyk container test ubuntu 

# will alarm for `high` issues and above 
snyk container test ubuntu --severity-threshold=high
 
# will scan a local image my-image:latest. The --file=Dockerfile can add more context to the security scanning. 
snyk container test my-image:latest --file=Dockerfile
```

# Spot Check
Perform the above steps and make sure `snyk` scans images properly. You'll use it in the following exercises.