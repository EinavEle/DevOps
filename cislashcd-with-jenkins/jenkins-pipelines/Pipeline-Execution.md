
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

Let's discuss the execution stages when your pipeline is running:

1. **Job scheduling**: When you trigger a pipeline job, Jenkins schedules the job on one of its available **agents** (also known as nodes). Agents are the machines that actually execute the build steps. In our case, the pipline runs on the Jenkins server machine itself, known an the **built-in node**. This is very bad practice and we will change it soon. Each agent can have one or more **executors**, which are worker threads responsible for running jobs concurrently.
2. **Workspace creation**: Jenkins creates a **workspace directory** on the agent's file system. This directory serves as the working area for the pipeline job.
3. **Checkout source code**: Jenkins checks out the source code into the workspace. 
4. **Pipeline execution**: Jenkins executes your pipeline script step-by-step. 

## Spot check

Is the order of `stage`s matter?


<details>
  <summary>
     Solution 
  </summary>
    
Yes, the order of stages in a Jenkins pipeline matters. The stages are executed sequentially in the order they are defined in the pipeline script. Each stage typically represents a distinct phase of your build, test, and deployment process, and they are executed one after the other.

</details>
