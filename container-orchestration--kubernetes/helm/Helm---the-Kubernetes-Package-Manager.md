## Motivation

**Helm** is a "package manager" for Kubernetes, here are some of the main features of the tool:

- **Helm Charts**: Instead of dealing with numerous YAML manifests, which can be a complex task, Helm introduces the concept of a "Package" (known as **Chart**) – a cohesive group of related YAML manifests that collectively define a single application within the cluster.
  For example, an application might consist of a Deployment, Service, HorizontalPodAutoscaler, ConfigMap, and Secret. 
  These manifests are interdependent and essential for the seamless functioning of the application. 
  Helm encapsulates this collection, making it easier to manage, version, and deploy as a unit.

- **Sharing Charts**: Helm allows you to share your charts, or use other's charts. Want to deploy MongoDB server on your cluster? Someone already done it before, you can use her Helm Chart to with your own configuration values to deploy the MongoDB.  

- **Dynamic manifests**: Helm allows you to create reusable templates with placeholders for configuration values. For example:
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: {{ .Values.serviceName }}   # the service value will be dynamically placed when applying the manifest
  spec:
    selector:
      app: {{ .Values.Name }}   # the selector value will be dynamically placed when applying the manifest
  ...
  ```
  
  This becomes very useful when dealing with multiple clusters that share similar configurations (Dev, Prod, Test clusters). 
  Instead of duplicating YAML files for each cluster, Helm enables the creation of parameterized templates.

## Install Helm

https://helm.sh/docs/intro/install/

## Helm Charts 

Helm uses a packaging format called charts. A chart is a collection of files that describe a related set of Kubernetes resources. 
A single chart might be used to deploy some single application in the cluster.
