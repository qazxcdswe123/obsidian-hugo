---
aliases: []
tags: []
date created: Jul 15th, 2022
date modified: Mar 29th, 2023
---
- [[Manjaro]] 
- [[Command Line]] 
- [[Linux Command Modern Alternative]]
- [[Linux User]]
- [[Firewall]]
- [[01-Linux and Command Line]]
- [[symbolic link]]
- [[rsync]]
- [[inode]]
- [[File System Permission]]
- [[Linux Permission]]
- [[ebpf]]
- [[ABI]]
- [[Linux File]]
- [[Operating System|OS]]
- [[Kernel]]
- [[PVE]]

## Configurations
- [[Linux Networking]]
- [[Linux Storage]]

## Mirrors

### Ubuntu
```
sudo sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list
```

## Debian
```
sudo sed -i 's/ftp.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
apt purge package
```