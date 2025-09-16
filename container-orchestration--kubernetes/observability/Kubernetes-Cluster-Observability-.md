## Motivation and challenges 

Kubernetes cluster is great, but what about monitoring the cluster applications?

By **monitoring** we mean collecting logs and metrics from our containers and nodes. 

**Logs** are chronological records of events that occur within the app, typically in a semi-structured textual form.

**Metrics**, on the other hand, are quantitative measurements (numbers) that represent the state or performance of a system (e.g. CPU usage, network incoming traffic).
Since metrics are values that might change very rapidly, they often collected at regular intervals (e.g. every 15 seconds). 

Collecting logs and metrics from applications is important for several reasons, including:

- **Troubleshooting and Debugging**: investigate issues and bugs.
- **Performance Analysis**: gain insights into the system's behavior, identify performance bottlenecks.
- **Auditing**: Keep a historical record of audit events in your system.
- **Capacity Planning**: By analyzing metrics, you can gain insights into resource usage patterns, helping with scaling planning.
- **Business Intelligence (BI)**: Logs and metrics can contain valuable business insights, such as user behavior, preferences, and trends.

Monitoring clusters presents unique challenges stemming from the distributed nature of its components and the dynamic, ephemeral environment it operates in. 

- Pods are spread by k8s across dozen of Nodes.
- Pods are launched and terminated throughout the cluster's lifecycle, which lead to loss of critical logs from pods that was terminated.

In this tutorial we will set up a robust monitoring system for our cluster.
