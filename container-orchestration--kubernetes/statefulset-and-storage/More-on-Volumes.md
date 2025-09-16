
Kubernetes supports [many types](https://kubernetes.io/docs/concepts/storage/volumes/#volume-types) of persistent volumes.

As your Minikube cluster deployed on your local machine, there is no any real "volume". 
Thus, the `hostPath` volumes type is used, which mounts a file or directory from the host node's file system into the Pod.

### Volume data protection

PersistentVolumeClaims (PVCs) and PersistentVolumes (PVs) are not a joke. 
These are the objects in the cluster representing real infrastructure containing your ⚠️⚠️ **customer's data** ⚠️⚠️. 

You don't want to delete a (PVCs) or (PVs) by mistake, and lose your data as a result. 

Kubernetes is shipped with a **Storage Object in Use Protection feature** to deal with that risk. 
PersistentVolumeClaims (PVCs) **in active use by a Pod** and PersistentVolume (PVs) that are bound to PVCs are not removed immediately from the system.

- PVC removal is postponed until the PVC is no longer actively used by any Pods.
- PV removal is postponed until the PV is no longer bound to a PVC.

And what about the underlying infrastructure that the PV in bound to (such as an AWS EBS or GCE PD volume)? 

Kubernetes allows reclamation of the PersistentVolume resource by another PersistentVolumeClaim.
The reclaim policy for a PersistentVolume tells the cluster what to do with the volume after it has been released of its claim. 

Volumes reclaim policy can either be `Retained` or `Deleted`.

- `Retain` - When the PersistentVolume is deleted, the associated storage asset in external infrastructure (AWS EBS or Azure disks) still exists. 
- `Delete` - When the PersistentVolume is deleted, the associated storage asset in the external infrastructure is removed as well.
