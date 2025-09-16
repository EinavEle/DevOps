
### Exercise 1 - Integrate the MongoDB cluster into the `productcatalogservice` service.

1. Under `k8s/productcatalogservice` you'll find the source code for the Product Catalog service, with modifications for work with the MongoDB cluster.
2. Build the image.
3. Connect to the Mongo shell of your primary replica, write some products data into it. Here is a valid example:
   ```json
   {
       "id": "OLJCESPC7Z",
       "name": "Sunglasses",
       "description": "Add a modern touch to your outfits with these sleek aviator sunglasses.",
       "picture": "/static/img/products/sunglasses.jpg",
       "priceUsd": {
           "currencyCode": "USD",
           "units": 19,
           "nanos": 990000000
           },
       "categories": ["accessories"]
   }
   ```
   You'll find valid examples in `products-example.json`. 

4. Change the `productcatalogservice/manifest.yaml` manifest according to you docker image name, and Mongo related environment variables. 
5. Apply. Make sure the service is working properly.


### Exercise 2 - Persist Grafana data using StatefulSet

**Before starting, delete any existed Grafana server from previous exercises**.

Provision a Grafana server using a StatefulSet with `2GB` volume to persist the server's data and configurations.
All Grafana data is stored under `/var/lib/grafana`. The server should run using 1 replica.

Make sure the StatefulSet was created successfully, and that Grafana data is persistent.   

### Exercise 3 - Increase volumes capacity

Assume your MongoDB cluster is monitored by Grafana, and you see that the disk capacity is about to be out of space.    

This exercise guides you how to properly increase the Kubernetes volume size.  

Resizing an existing volume is done by editing the **PersistentVolumeClaim** object.

Never manually interact with the storage backend, nor delete and recreate PV and PVC objects to increase the size of a volume. 

The StorageClass that your PVC is based on, must have the `allowVolumeExpansion` field set to `true`: 

```bash
kubectl describe storageclass <storage-class-name>
```

To add the `allowVolumeExpansion: true` field, or can edit the resource manually via the Kubernetes Dashboard, or perform:

```bash
# Edit the resource using VIM 
kubectl edit storageclass <storage-class-name>

# or Nano
KUBE_EDITOR="nano" kubectl edit storageclass <storage-class-name>
```

Now just increase the volume size in your PVC, again either by editing it manually via the Kubernetes Dashboard, or by:

```bash
kubectl edit pvc <pvc-name>
```

Kubernetes will interpret a change to the storage field as a request for more space, and will trigger automatic volume resizing.

Once the PVC has the condition `FileSystemResizePending` then pod that uses the PVC can be restarted to finish file system resizing on the node. 
Restart can be achieved by deleting and recreating the pod or by scaling down the StatefulSet and then scaling it up again.

Once file system resizing is done, the PVC will automatically be updated to reflect new size.

Any errors encountered while expanding file system should be available as events on pod
