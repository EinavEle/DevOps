
**Remove any existed grafana Deployment, StatefulSet or Service before you start.**

Like DockerHub, there is a open-source community Hub for Charts of famous applications.
It's called [Artifact Hub](https://artifacthub.io/packages/search?kind=0), check it out. 

Let's review and install the [official Helm Chart for Grafana](https://artifacthub.io/packages/helm/grafana/grafana).

To deploy the Grafana Chart, you first have to add the **Repository** in which this Chart exists. 
A Helm Repository is the place where Charts can be collected and shared.

```bash
helm repo add grafana-charts https://grafana.github.io/helm-charts
helm repo update
```

The `grafana-charts` Helm Repository contains many different Charts maintained by the Grafana organization. 
[Among the different Charts](https://artifacthub.io/packages/search?repo=grafana&sort=relevance&page=1) of this repo, there is a Chart used to deploy the Grafana server in Kubernetes. 

Deploy the `grafana` Chart by: 

```bash
helm install grafana grafana-charts/grafana 
```

The command syntax is as follows: `helm install <release-name> <helm-repo-name>/<chart-name>`.

Whenever you install a Chart, a new **Release** is created.   
In the above command, the Grafana server has been released under the name `grafana`, using the `grafana` Chart from the `grafana-charts` repo.

During installation, the Helm client will print useful information about which resources were created, what the state of the Release is, and also whether there are additional configuration steps you can or should take.

> #### Try it yourself
> 
> Review the release's output. Then use `port-forward` to visit the Grafana server.

### Customize the Grafana release

When installed the Grafana Chart, the server has been release with default configurations that the Chart author decided for you. 

A typical Chart contains hundreds of different configurations, e.g. container's environment variables, custom secrets, etc..

Obviously, you want to customize the Grafana release according to your configurations.
Good Helm Chart should allow you to configure the Release according to your configurations. 

To see what options are configurable on a Chart, go to the [Chart's documentation page](https://artifacthub.io/packages/helm/grafana/grafana), or use the `helm show values grafana-charts/grafana` command. 

Let's override some of the default configurations by specifying them in a YAML file, and then pass that file during the Release upgrade:

```yaml
# k8s/grafana-values.yaml

persistence:
  enabled: true
  size: 2Gi

env:
  GF_DASHBOARDS_VERSIONS_TO_KEEP: 10

```

The above values configure the Grafana server data to be persistent, and define some Grafana related environment variable. 

To apply the new Chart values, `upgrade` the Release: 

```bash
helm upgrade -f grafana-values.yaml grafana grafana-charts/grafana
```

An `upgrade` takes an existing Release and upgrades it according to the information you provide. 
Because Kubernetes Charts can be large and complex, Helm tries to perform the least invasive upgrade. 
It will only update things that have changed since the last release.

> #### Try it yourself
> 
> Review the [Official Grafana Helm values](https://artifacthub.io/packages/helm/grafana/grafana), and add more Chart values overrides in `grafana-values.yaml` to achieve following configurations: 
> 
> 1. The deployed Grafana [image tag version](https://hub.docker.com/r/grafana/grafana/tags) is higher than `8.0.0`. 
> 2. The [`redis-datasource`](https://grafana.com/grafana/plugins/redis-datasource/?tab=overview) plugin is installed.
> 3. A redis datasource is configured to collect metrics from the `redis-cart` service.


If something does not go as planned during a release, it is easy to roll back to a previous release using `helm rollback [RELEASE] [REVISION]`:

```shell
helm rollback grafana 1
```

To uninstall the Chart release:

```shell
helm uninstall grafana
```
