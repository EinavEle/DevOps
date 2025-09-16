### Exercise 1 - Zero downtime during scale

Your goal in this exercise is to achieve zero downtime during scale up/down events of a simple webserver.

The code can be found in `k8s/zero_downtime_flask` for Python (or `k8s/zero_downtime_node` for Nodejs).

1. Deploy the app as a simple Deployment (with the corresponding Service). 
2. Generate some incoming traffic (5 requests per second) using a `load-generator` pod: 
   ```bash
   kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.2; do (wget -q -O- http://SERVICE_NAME &); done"
   ```
   Chane `SERVICE_NAME` accordingly.    

3. Increase the Deployment replicas while watching the `load-generator` pod logs. Did you lose requests for a short moment? Why?
4. Decrease the Deployment replicas, lost requests again? Why? 
5. Define a `liveness` and `readiness` probes in your Deployment. Change the server code and add the corresponding endpoints for the probes (e.g. `/healthz` for liveness, `/ready` for readiness). 
6. Test again and make sure you don't lose even aa single requests during **scale up and scale down** events.

**Bonus**: Make sure you are able to perform a rolling update with zero downtime. 

### Exercise 2 - Pod troubleshoot

In the file `k8s/pod-troubleshoot.yaml`, a PostgreSQL database Deployment is provided with intentionally injected issues for troubleshooting purposes.

Fix the issues while complying with the below requirements: 

- You should be able to communicate with the DB by (the command creates a temporary Pod that lists the existed databases in Postgres):

  ```bash
  kubectl run -i --tty --rm postgres-client --image=postgres:11.22-bullseye --restart=Never -- /bin/sh -c "PGPASSWORD=<your-pg-pass> psql -h mysql-service -U postgres -c '\list'"
  ```
  
  While `<your-pg-pass>` is your postgres DB password.

- The DB must be running on a node labeled `disktype=ssd`.
- The `postgres:11.22-bullseye` container must be scheduled on a node with at least 50 milli-cpu.
- The `postgres:11.22-bullseye` container must have liveness and readiness probed configured and working properly. 

### Exercise 3 - Init containers

A Pod can have multiple containers running apps within it, but it can also have one or more [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/), which are run before the app containers are started.

Create a Pod with an init container that clones the [2048 game](https://github.com/gabrielecirulli/2048) source code repo game into a **shared volume** with the Pod's container - an [nginx](https://hub.docker.com/_/nginx) image - that will serve the game.   




