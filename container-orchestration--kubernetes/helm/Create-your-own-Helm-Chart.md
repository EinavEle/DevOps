
In this section we will create a Chart for the `paymentservice` (a component within the [Online Boutique service](https://github.com/GoogleCloudPlatform/microservices-demo)).

Why is it good idea? Imagine the Online Boutique service is a real product at your company. 
The service is probably deployed in at least two different environments: Development and Production. 
Instead of maintaining two different sets of Yaml manifests for with values per environment, we will leverage the created Chart to deploy the application in two instances: first as `paymentservice-dev` for the Development environment, and as `paymentservice-prod` for Production env, each with his own values.

Helm can help you get started quickly by using the `helm create` command:

```bash
helm create paymentservice
```

Now there is a chart in `./paymentservice`. You can edit it and create your own templates.
The directory name is the name of the chart.

Inside of this directory, Helm will expect the following structure:

```text
paymentservice/
  Chart.yaml          # A YAML file containing information about the chart
  values.yaml         # The default configuration values for this chart
  charts/             # A directory containing any charts upon which this chart depends.
  crds/               # Custom Resource Definitions
  templates/          # A directory of templates that, when combined with values,
                      # will generate valid Kubernetes manifest files.
  templates/NOTES.txt # OPTIONAL: A plain text file containing short usage notes
```

For more information about Chart files structure, go to [Helm docs](https://helm.sh/docs/topics/charts/). 

Change the default Chart values in `values.yaml` to match the original `paymentservice` service, as follows:

```yaml
# paymentservice/values.yaml

image:
  repository: gcr.io/google-samples/microservices-demo/paymentservice
  tag: "v0.8.0"

service:
  port: 50051 

resources:
  requests:
    cpu: 50m
    memory: 64Mi
  limits:
    cpu: 200m
    memory: 128Mi
```

As you edit your chart, you can validate that it is well-formed by running `helm lint`.

When it's time to package the chart up for deployment, you can run the `helm package` command:

```bash
helm package paymentservice
```

And that chart can now easily be installed by:

```bash
helm install paymentservice-dev ./paymentservice-0.1.0.tgz
```

> #### Try it yourself
> 
> - Watch the deployed `paymentservice-dev` Deployment in the cluster, try to debug the issues so the Pods can run successfully. 
>   **Hint**: take a look on the original `paymentservice` service, and change the `paymentservice/templates/deployment.yaml` manifest accordingly.
> - Create a new release for Prod: `paymentservice-prod`. 
> - Update the Chart version to `0.2.0`, pack and create a new release. 

