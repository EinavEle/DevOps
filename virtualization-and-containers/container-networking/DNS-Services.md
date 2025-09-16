Containers that are connected to the default bridge network inherit the DNS settings of the host, as defined in the `/etc/resolv.conf` configuration file in the host machine (they receive a copy of this file). Containers that attach to a custom network use Docker’s embedded DNS server. The embedded DNS server forwards external DNS lookups to the DNS servers configured on the host machine.

Custom hosts, defined in `/etc/hosts` on the host machine, aren’t inherited by containers. To pass additional hosts into the container, refer to [add entries to container hosts file](https://docs.docker.com/engine/reference/commandline/run/#add-host) in the `docker run` reference documentation.

# The `EXPOSE` Dockerfile Instructions
The `EXPOSE` [instruction](https://docs.docker.com/engine/reference/builder/#expose) informs Docker that the container listens on the specified network ports at runtime.

The `EXPOSE` instruction **does not** actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To actually publish the port when running the container, use the `-p` flag on docker run to publish and map one or more ports.