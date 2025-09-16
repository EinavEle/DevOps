
When versioning is enabled in S3, every time an object is overwritten or deleted, a new version of that object is created. Over time, this can lead to a large number of versions for a given object, many of which may no longer be needed for business or compliance reasons.

By creating lifecycle rules, you can define actions to automatically transition non-current versions of objects to a lower-cost storage class or delete them altogether. This can help you reduce storage costs and improve the efficiency of your S3 usage, while also ensuring that you are in compliance with data retention policies and regulations.

For example, you might create a lifecycle rule to transition all non-current versions of objects to `Standard-IA` storage after 30 days, and then delete them after 365 days. This would allow you to retain current versions of objects in S3 for fast access, while still meeting your data retention requirements and reducing storage costs for non-current versions.


1. Choose the **Management** tab, and choose **Create lifecycle rule**\.

1. In **Lifecycle rule name**, enter a name for your rule\.

1. Choose the scope of the lifecycle rule (in this demo we will apply this lifecycle rule to all objects in the bucket).

1. Under **Lifecycle rule actions**, choose the actions that you want your lifecycle rule to perform:
    + Transition *noncurrent* versions of objects between storage classes
    + Permanently delete *noncurrent* versions of objects

1. Under **Transition non\-current versions of objects between storage classes**:

    1. In **Storage class transitions**, choose **Standard\-IA**.

    1. In **Days after object becomes non\-current**, enter 30.

1. Under **Permanently delete previous versions of objects**, in **Number of days after objects become previous versions**, enter 90 days.

1. Choose **Create rule**\.

   If the rule does not contain any errors, Amazon S3 enables it, and you can see it on the **Management** tab under **Lifecycle rules**\.
