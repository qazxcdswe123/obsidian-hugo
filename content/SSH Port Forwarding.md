---
aliases: []
date created: Feb 26th, 2022
date modified: Mar 29th, 2023
---
- [[Linux]]
- Local port forwarding  
	- `ssh -L sourcePort:forwardToHost:onPort connectToHost`
	- The requests to your local machine is forwarded to a remote machine 
- Remote port forwarding  
	- `ssh -R sourcePort:forwardToHost:onPort connectToHost`
	- The requests to the remote machine is forwarded to your local machine

## Examples

### Example for Local Port Forwarding
```
ssh -L 80:localhost:80 SUPERSERVER
```

You specify that a connection made to the local port 80 is to be forwarded to port 80 on SUPERSERVER. That means if someone connects to your computer with a web browser, he gets the response of the webserver running on SUPERSERVER. You, on your local machine, have no webserver running.

### Example for Remote Port Forwarding
```
ssh -R 80:localhost:80 tinyserver
```

You specify, that a connection made to the port 80 of tinyserver is to be forwarded to port 80 on your local machine. That means if someone connects to the small and slow server with a web browser, he gets the response of the webserver running on your local machine. The tinyserver, which has not enough diskspace for the big website, has no webserver running. But people connecting to tinyserver think so.

![](https://s2.loli.net/2022/02/26/aPhA3gmXjLsvydc.png)  
![](https://s2.loli.net/2022/02/26/LoCRuIBzfP8ivHX.png)
