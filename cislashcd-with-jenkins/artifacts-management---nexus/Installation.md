
We will deploy the Nexus server using a [pre-built Docker image](https://hub.docker.com/r/sonatype/nexus3/).

Throughout this tutorial we will be experimenting with the Nexus server while running locally:

```shell
sudo mkdir /nexus-data && sudo chown 200:200 /nexus-data && sudo chmod 700 /nexus-data
docker run -d -p 8081:8081 --name nexus -v /nexus-data:/nexus-data -e INSTALL4J_ADD_VM_PARAMS="-Xms1000m -Xmx1000m -XX:MaxDirectMemorySize=1000m" sonatype/nexus3
```

## Sport check 

Why was the ownership on the `/nexus-data` dir changed to be owned by user ID and group Id `200`? 


<details>
  <summary>
     Solution
  </summary>
    
    These are the UID and GID of the user running the `sonatype/nexus3` container. 

</details>