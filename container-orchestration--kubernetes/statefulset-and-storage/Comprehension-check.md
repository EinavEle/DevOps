
Given a cluster with a running MySQL StatefulSet: 

```yaml 
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: "mysql"
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql-container
        image: mysql:latest
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "your-root-password"
        - name: MYSQL_DATABASE
          value: "your-database-name"
        - name: MYSQL_USER
          value: "your-mysql-user"
        - name: MYSQL_PASSWORD
          value: "your-mysql-password"
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql

  volumeClaimTemplates:
  - metadata:
      name: mysql-persistent-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 5Gi
```

Answer the below 3 questions.


{Check It!|assessment}(multiple-choice-3070140558)
{Check It!|assessment}(multiple-choice-387711468)
{Check It!|assessment}(multiple-choice-1704249248)
{Check It!|assessment}(multiple-choice-3230939952)
{Check It!|assessment}(multiple-choice-2687848308)
{Check It!|assessment}(multiple-choice-3619870778)
{Check It!|assessment}(multiple-choice-253462421)
{Check It!|assessment}(multiple-choice-3829701108)
