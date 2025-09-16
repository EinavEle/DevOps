
### Terminology

Source reference: https://www.jenkins.io/doc/book/managing/nodes/

#### Jenkins controller

The Jenkins controller is the Jenkins service itself and where Jenkins is installed. It is also a web server that also acts as a "brain" for deciding how, when, and where to run tasks. 

#### Nodes

Nodes are the "machines" on which build agents run. Jenkins monitors each attached node for disk space, free temp space, free swap, clock time/sync, and response time.
A node is taken offline if any of these values go outside the configured threshold. Jenkins supports two types of nodes:

- **Agents** - an agent is a small (170KB single `jar`) Java client process that connects to a Jenkins controller
- **Built-in node** (exists within the controller)

#### Executors

An executor is a slot for the execution of tasks. Effectively, it is a thread in the agent. The number of executors on a node defines the number of concurrent tasks that can run. 

### Create an EC2 based agent 

Let's create an EC2 and connect it to your Jenkins controller as an agents.

1. Create an Ubuntu `*.micro` EC2 instance in the same VPC as your Jenkins server. Your instance has to have Java 11 and Docker installed. Make sure you have enough disk to execute your pipelines. It's recommended to create an AMI from this instance to later usage.
3. Go to **Manage Jenkins** > **Manage Nodes and Clouds** > **New Node**.
2. Give your node a name. E.g. `EC2 agent 1`.
3. Choose the option **Permanent Agent** and click **Ok**.
4. In **Number of executors** it's recommended to choose a value according to the number of CPUs of your agents machine. 
5. Under **Remote root directory** specify a directory on the agent where Jenkins will store files, it can be any directory that the `ubuntu` user has access to. E.g. `~/jenkins` or any other path.
4. Assign a label to the agent, e.g. `general`. The label will be later used to assign jobs specifically on an agent having this label.
5. In the **Launch method** section, select **Launch agents via SSH**.
6. Fill in the SSH details for your EC2 instance:
   - Host: Enter the private IP address of your EC2 instance.
   - Credentials: Choose or create the SSH credentials that allow Jenkins to connect to your EC2 instance.
   - Host Key Verification Strategy: Choose **Non verifying Verification Strategy**
   
   Click **Save** to save the configuration.
7. On the **Nodes** page, find your newly created agent and click on it, click on **Launch agent** from the left-hand menu.
8. Configure the `build.Jenkinsfile` pipeline to b executed on agents labeled according to the label you choose. For example:

```text
agent {
    docker {
        label 'general'
        image '<image-url>'       
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
}
```

Trigger the pipeline and make sure it's running on the agents machine. 


## Spot check 

In the Jenkins UI, how can you determine whether a job was scheduled on a specific agent?


<details>
  <summary>
     Solution
  </summary>
In the job's details page, look for the "Build Executor Status" section. This section provides information about the executor that was used to run the job.

You will see details such as:

- Executor Number: This indicates the executor (agent) number used for the build.
- Executor Name: This typically displays the name or label of the agent where the job was executed.
- Current Status: You can see whether the executor is currently idle, busy, or paused.

Additionally, you can click on the "Console Output" link to view the console log for the job.
In the console log, you can find information about the agent where the job was executed. Look for lines similar to:

```text
Running on agent-name or executor-number
```

This line indicates the name of the agent or executor where the job was scheduled and executed.

</details>