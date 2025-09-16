
**Note**: Throughout this module you will build, test and deploy an app called Roberta (can be found in our shared repo under `roberta`).
This is a simple flask webserver that serves a [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) AI model based on [roberta-base](https://huggingface.co/roberta-base).
The model was trained on a data from Reddit to analyze the sentiment of an English sentence. 

A **GitHub webhook** is a mechanism that allows GitHub to notify a Jenkins server when changes occur in the repo. 
When a webhook is configured, GitHub will send a HTTP POST request to a specified URL whenever a specified event, such as a push to the repository, occurs.

1. If you don't have it yet, create a new GitHub repository and copy the files under the `roberta` directory to the root directory of your repo, push it.
2. To set up a webhook from GitHub to the Jenkins server, on your GitHub repository page, go to **Settings**. From there, click **Webhooks**, then **Add webhook**.
3. In the **Payload URL** field, type `http://<jenkins-ip>:8080/github-webhook/`. In the **Content type** select: `application/json` and leave the **Secret** field empty.
4. Choose the following events to be sent in the webhook:
    1. Pushes
    2. Pull requests


## Spot check 

Describe one use case for which we want Jenkins to be notified about "push", and one use case for "pull request" events in GitHub


<details>
  <summary>
     Solution
  </summary>
    - Push event: when a developer pushes new code, we may want to automatically build a new version with her changes and deploy it to developments environments.

    - Pull Request - when a developer creates a PR, we may want to test the app with her version before we allow to merge it to production branch. 

</details>