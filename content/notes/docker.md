---
title: docker
---

[ArchLinux Wiki](https://wiki.archlinux.org/title/docker#Installation)
[[systemd]]
# Trouble Shooting
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
and relogin

# Mirror
`https://b9b9x0p9.mirror.aliyuncs.com`

# Projects
```
docker run -it \ --device /dev/kvm \ -p 50922:10022 \ -e XDG_RUNTIME_DIR=/tmp \ -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \ -v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/$WAYLAND_DISPLAY \ -e GENERATE_UNIQUE=true \ -e MASTER_PLIST_URL='https://raw.githubusercontent.com/sickcodes/osx-serial-generator/master/config-custom.plist' \ sickcodes/docker-osx:monterey
```