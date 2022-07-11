- Port Forwarding
![](https://s2.loli.net/2022/02/26/aPhA3gmXjLsvydc.png)
![](https://s2.loli.net/2022/02/26/LoCRuIBzfP8ivHX.png)
- Local port forwarding
	`ssh -L sourcePort:forwardToHost:onPort connectToHost`
- Remote port forwarding
	`ssh -R sourcePort:forwardToHost:onPort connectToHost`

## Examples

### Example for 1

```
ssh -L 80:localhost:80 SUPERSERVER
```

You specify that a connection made to the local port 80 is to be forwarded to port 80 on SUPERSERVER. That means if someone connects to your computer with a web browser, he gets the response of the webserver running on SUPERSERVER. You, on your local machine, have no webserver running.

### Example for 2

```
ssh -R 80:localhost:80 tinyserver
```

You specify, that a connection made to the port 80 of tinyserver is to be forwarded to port 80 on your local machine. That means if someone connects to the small and slow server with a web browser, he gets the response of the webserver running on your local machine. The tinyserver, which has not enough diskspace for the big website, has no webserver running. But people connecting to tinyserver think so.