## [[Minecraft]]
```
docker run -d -v /root/mc_data:/data \
    -e TYPE=MODRINTH \
    -e MEMORY=3G \
    -e MODRINTH_PROJECT=moon-luseban \
    -e EULA=TRUE \
    -p 25565:25565 -e EULA=TRUE --name mc itzg/minecraft-server
```