Let's review the following Git workflow:

<img src=".guides/img/envbased.png" width="35%">

1. Developers branching our from an up-to-date `main` branch into their feature branch. 
2. They commit changes into their feature branch.
3. At some point, they want to test their changes in Development environment. They merge the feature branch into `dev` branch, and push to remote.
4. After the changes have been tested in development environment and a few more fixes has been committed, the developer creates a Pull Request from their feature branch into `main`.
5. The `main` branch can be deployed to production environment directly after the merge. 

From the above Git workflow, we can conclude that a Pull Request is a crucial point for testing and review code changes before they are merged into the `main` branch, and potentially deployed to production systems. 
Thus, it's common practice to let Jenkins perform an extensive testing on an opened Pull Requests.

So far we've seen how pipeline can be built and run around a single Git branch (e.g. `main` or `dev`). 
Now we would like to create a new pipeline which will be triggered on **every PR** that is created in GitHub.
For that we will utilize Jenkins [multi-branch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/).
