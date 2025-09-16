
We also would like to protect the `main` branch from being merged by non-tested branch.

1. From GitHub main repo page, go to **Settings**, then **Branches**.
2. **Add branch protection rule** for the `main` branch as follows:
   1. Check **Require a pull request before merging**.
   2. Check **Require status checks to pass before merging** and search the `continuous-integration/jenkins/pr-merge` check done by Jenkins.
   3. Save the protection rule.

Your `main` branch is now protected and no code can be merged to it unless the PR is reviewed by other team member and passed all automatic tests done by Jenkins.
