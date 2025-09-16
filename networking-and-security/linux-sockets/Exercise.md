# Exercise 1 - client and server communication over TCP socket
Using the `./server` application create multiple connections between different clients to the same server. Explore the connections in `netstat`'s output.

Once the server is running, explore `/proc/<pid>/fd` while `<pid>` is the server process id, to see the created socket file for each client.

Try to run 2 servers on the same machine. What is the returned error and why?