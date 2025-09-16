
## Exercise 1 - Store YAML artifacts in Nexus

In this exercise we assume a Jenkins pipeline that generates a YAML artifact (for Kubernetes Deployment manifest) and store the artifact in Nexus `raw` hosted repo. 

1. Under `yaml_artifact_example` you'll find:
   2. `my-deployment.yaml` - this is a **template** YAML manifest (note that `{{ img_tag }}` is a placeholder for a variable that should be replaced with an actual image tag).
   3. `generate_yaml.py` - is a Python code that replaces the `{{ img_tag }}` with an actual image tag provided as an argument to the script (e.g. `python generate_yaml.py 0.0.1`).

   Test it by `python generate_yaml.py 0.0.1` and inspect the generated YAML artifact.
2. Create a bash script that generates the YAML artifact and push it to a **hosted raw** repo called `k8s-manifests`. 
3. (Optional) Create a Jenkins pipeline that generates the artifacts, and integrate your script as a Stage.

## Exercise 2 - Define s3 as an artifacts storage

Follow:  

https://help.sonatype.com/repomanager3/nexus-repository-administration/repository-management/configuring-blob-stores#ConfiguringBlobStores-AWSSimpleStorageService(S3)


## Exercise 3 - Nexus Docker repo  

1. In your Nexus server, create `Docker(proxy)`, `Docker(hosted)` and `Docker(group)` which contains the two repos (the proxy and hosted).
2. From your local machine, pull an image from the created group repo.
4. From your local machine, push an image into the hosted repo.

## Exercise 4 - Policy to clean-up artifacts 

If you are not cleaning out old and unused components, your repositories will grow quickly. Over time, this will present risks to your deployment:

- Storage costs will increase
- Performance is impacted
- Artifact discovery will take longer
- Consuming all available storage will results in server failure

Create two clean-up policies as follows:

- `dev-cleanup` policy that cleans artifacts after 30 days.
- `prod-cleanup` policy that cleans artifact after 1 year (production artifacts should be stored for long time). 

Create associate the `dev-cleanup` policy with one of your repositories.

## Exercise 4 - Serve Nexus over HTTPS (using self-signed certificate)

Please follow:   

https://help.sonatype.com/repomanager3/nexus-repository-administration/configuring-ssl#ConfiguringSSL-ServingSSLDirectly

At the end, you should be able to communicate with the server by `https://localhost:8443`.
