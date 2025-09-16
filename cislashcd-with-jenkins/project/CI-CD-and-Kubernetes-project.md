**Note:** The compute infrastructure used in this project is not related to the previous AWS project. To reduce costs, pplease cleanup the EC2 instance, ASG and ELB used in the AWS project. 

## Background

In this project you will design and implement CI/CD pipelines for the Object Detection Service to automate the deployment process in Kubernetes cluster. 

## Infrastructure

You'll deploy your service on a local Minikube cluster.

In order to receive traffic from Telegram servers into your `polybot` service running in k8s cluster, you can create a [Service of type `NodePort`](https://minikube.sigs.k8s.io/docs/handbook/accessing/) for the `polybot` Deployment. Then, you can use `ngrok` to route the traffic to the Minikube node:

```bash
ngrok http http://$(minikube ip):NODE_PORT
```

While changing `NODE_PORT` to your Service's node port number. 


## CI server

Use the Jenkins server we've setup in class, or create a new one if needed (either in k8s, EC2, or any other way). 
You can also use any other CI platform (e.g. GitHub Actions, Azure DevOps).  

**No need** to run agents on different nodes! All pipelines can be running on the Jenkins server itself.

## Build pipelines

Design and implement build pipelines for the `polybot` and `yolo5` services:

- You can simply create 2 `Jenkinsfile`s as detailed below. Alternatively, if you want to reduce code duplication, use Jenkins [shared library](https://www.jenkins.io/doc/book/pipeline/shared-libraries/).

```text
.
├── yolo5-build.Jenkinsfile
├── polybot-build.Jenkinsfile
```

- The pipelines should be triggered automatically upon push event.
- Make sure to build only services that their source code have been changed. If you changed the `polybot` code and pushed it, only the build pipeline of the `polybot` should be triggered. 
- Each new built Docker image should have a different image tag.

## Deployment to Kubernetes using ArgoCD

[ArgoCD](https://argo-cd.readthedocs.io/en/stable/) is a declarative continuous delivery tool for Kubernetes. 

Argo automatically detects changes done in YAML manifests in your GitHub repo, and sync the cluster accordingly.
For example, if you change an image tag in a YAML manifest, and **commit and push** it, Argo can automatically deploy the new version into your cluster (instead of executing the `kubectl apply` command).
This pattern is called **GitOps**, which means, using Git repositories as the **source of truth** for defining the desired application state.

- In your project repo, create YAML manifests. For example:

  ```text
  .
  ├── k8s
  │    ├── yolo5.yaml      # Deployment
  │    └── polybot.yaml    # Deployment and Service
  ```

   - This is only a suggestion. Feel free to change to any other files layout that works for you.
   - You can use **Helm** if you want to reduce code duplications.

- Install Argo in your cluster by: 

  ```bash
  kubectl create namespace argocd
  kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
  ```
  
  You can access the server by port-forwarding the `argocd-server` service in `argocd` namespace.

- Create the below "release" pipeline that is triggered after a successful running of the build pipeline:

  ```text
  .
  ├── release.Jenkinsfile
  ```
  
  - The release pipeline receives the new image tag from the build pipeline (similarly as done in class).
  - The pipeline will **commit and push** the new version of your YAML manifests to the `releases` branch of your Git repository. Once the new version of the YAML manifests is pushed, ArgoCD automatically detects the changes and initiates the deployment process.

- In your Argo server, create a new application (**+ New App**) for the `polybot` and `yolo5`. The apps should use the `releases` branch as a source for YAML manifests.


## Trying it all together

Try to make some change to your code, commit and push it. Watch how Jenkins builds an image and Argo deploys the new version into your cluster. 


# Good Luck
