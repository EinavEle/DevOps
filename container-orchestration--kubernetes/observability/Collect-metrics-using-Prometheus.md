
[Prometheus](https://prometheus.io/docs/introduction/overview/) is a monitoring platform that collects metrics from [different platforms](https://prometheus.io/docs/instrumenting/exporters/) (such as databases, cloud providers, and k8s clusters).

Prometheus collects and stores its metrics as **time series** data, i.e. metrics information is stored with the timestamp at which it was recorded, alongside optional key-value pairs called **labels**.
Prometheus monitors its targets by using a **pull-based model**, where Prometheus periodically fetches metrics from the HTTP endpoints exposed by the targets.

![.guides/img/k8s_prom-architecture](./k8s_prom-architecture.png)


1. Deploy Prometheus using the [community Helm chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus). The Chart is already configured with the exporters needed to collect metrics from Pods and Nodes in your cluster. Use `k8s/prometheus-values.yaml` as the values override file. 
1. Integrate Prometheus into Grafana as a datasource.
1. In Grafana, import one of the following dashboards to get some insights about your cluster:
    - https://grafana.com/grafana/dashboards/6417-kubernetes-cluster-prometheus/
    - https://grafana.com/grafana/dashboards/315-kubernetes-cluster-monitoring-via-prometheus/
    - https://grafana.com/grafana/dashboards/12740-kubernetes-monitoring/
