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

## terminal
