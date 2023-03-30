## Docker Compose
May not needed
```sh
ARCH=$(uname -m) && [[ "${ARCH}" == "armv7l" ]] && ARCH="armv7"
sudo mkdir -p /usr/local/lib/docker/cli-plugins
sudo curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-${ARCH}" -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
ln -s /usr/local/lib/docker/cli-plugins/docker-compose /usr/bin/docker-compose
```

## Command
### Stop

## Projects
- [DeathRoadToBaldness/301.Server/Docker at main · qazxcdswe123/DeathRoadToBaldness · GitHub](https://github.com/qazxcdswe123/DeathRoadToBaldness/tree/main/301.Server/Docker)