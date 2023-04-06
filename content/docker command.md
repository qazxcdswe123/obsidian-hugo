---
aliases: []
date created: Oct 29th, 2022
date modified: Mar 14th, 2023
---

## Docker Exec
`docker exec -it <container name> /bin/bash`

## Docker Run
```
docker run -d --rm \
	--name watchtower
	-v /var/run/docker.sock:/var/run/docker.sock \
	containrrr/watchtower \
	alist
```

- `-d` flag to run the container in detached mode. 
- `--name` specify a name to the container
- `--rm` to automatically delete it when it exits  
- `-p 8080:80`: Map TCP port `80` in the container to port `8080` on the Docker host.

### Multi Stage Build
- [Multi-stage builds | Docker Documentation](https://docs.docker.com/build/building/multi-stage/)
