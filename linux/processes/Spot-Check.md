1. How many days is the `systemd-resolved` service running?
1. Is `ufw` service active in your system? Is it running? If not, what is the exit code of the process that runs the service? 
1. What is the PID of the `systemd-timesyncd` service? Restart the service, what is the PID? What is this service responsible for? 
1. Check the status of service `ssh`. Send `SIGKILL` to the process ID of this service. What happened to the service? Check the status, what is the status, why?  
<details>
  <summary>
    Solution
  </summary>

1. Execute `systemctl status systemd-resolved`, the information is there. 
1. Execute `systemctl status ufw`, usually the service is active but not running. The exit code is 0 (code=exited, status=0/SUCCESS).
1. Execute `systemctl status systemd-timesyncd`, the PID is Main PID: 596. Restart the service by `sudo systemctl status systemd-timesyncd`. The PID may change. The service is responsible for synchronizing the system clock across the network with a remote server using the Network Time Protocol (NTP).
1. Execute `systemctl status ssh`, the service should be active and running. Kill the main process of the service by `kill -9 <ssh-pid>`, while `<ssh-pid>` is the process id of the service. If you send a SIGKILL signal to the process ID of the SSH service, the service will be abruptly terminated. Usually, this service has been configured to automatically restart after a failure or unexpected termination, so the service status should be active and running (with different PID).

</details>