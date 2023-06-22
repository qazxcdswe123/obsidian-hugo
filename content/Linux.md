---
aliases: []
date created: Jul 15th, 2022
date modified: Apr 2nd, 2023
---
- [[Manjaro]] 
- [[PVE]]

___

- [[Linux Command Modern Alternative]]
- [[Linux User]]
- [[Linux Network Command]]
- [[Linux Kernel]]
- [[Linux Permission]]
- [[Linux Storage]]
- [[Protection Ring]]
- [[rsync]]
- [[inode]]
- [[eBPF]]
- [[ABI]]
- [[Operating System|OS]]

___

- [[01-Linux and Command Line]]

## Mirrors

### Ubuntu
```
sudo sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list
```

### Debian
```
sudo sed -i 's/ftp.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
apt purge package
```
