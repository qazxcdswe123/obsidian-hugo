---
aliases: []
tags: [] 
date created: Jun 2nd, 2022
date modified: Nov 24th, 2022
---
- [[systemd]]
- [[Docker Volume]]  
- [[Docker Command]]
- [[Docker Compose]]
- [[DockerFile]]
- [[Kubernetes]]

- Install Docker

```
curl -fsSL https://get.docker.com | sh
```

## Trouble Shooting
- `docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.`

```
systemctl start docker
```

- `docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied.`

```
sudo gpasswd -a $USER docker
sudo usermod -a -G docker $USER
newgrp docker
```

logout to take effect.

## Mirror
```
# /etc/docker/daemon.json
{
	"registry-mirrors": ["https://b9b9x0p9.mirror.aliyuncs.com"]
}
```

## Links
[ArchLinux Wiki](https://wiki.archlinux.org/title/docker#Installation)  
