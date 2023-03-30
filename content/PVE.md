---
aliases: [proxmox]
tags: []
date created: Mar 28th, 2023
date modified: Mar 29th, 2023
---
- 换源：
	- [proxmox | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/proxmox/)
- 修改 [[IP]] 地址
	- [Proxmox Virtual Environment（PVE）完美的更改IP地址 - 知乎](https://zhuanlan.zhihu.com/p/354038479)
 - Use [[tailscale]] to connect
 - Template:
	 - Right click to clone
	 - Base image
  - CT: [[Operating system]] container
  - [[Docker]]
  - Use `xterm.js`:
	  - Add serial port on hardware
	  - Change display to serial terminal
   - Resize disk: `qm resize 9001 scsi0 +18G`
   - [Firewall - Proxmox VE](https://pve.proxmox.com/wiki/Firewall)

## Force Quit Vm
```
rm /var/lock/qemu-server/lock-1001.conf
qm unlock 1001
# then stop the vm
```

## Power Consomption
```
# 下载编译
sudo apt install git
sudo apt install libpci-dev cmake gcc g++
git clone https://github.com/FlyGoat/RyzenAdj
cd RyzenAdj
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make

# 查询功耗
sudo ./ryzenadj -i
```

## Cloud Init
- [Open Source Cloud Computing Infrastructure - OpenStack](https://www.openstack.org/)
- [Understanding OpenStack](https://www.redhat.com/en/topics/openstack)
- [GitHub - canonical/cloud-init: Official upstream for the cloud-init: cloud instance initialization](https://github.com/canonical/cloud-init)
- [Index of /images/cloud/bullseye](https://cloud.debian.org/images/cloud/bullseye/)  
Cloud images are operating system templates and every instance starts out as an identical clone of every other instance. It is the user data that gives every cloud instance its personality and cloud-init is the tool that applies user data to your instances automatically.

- virt-customize

```
# On host
# sudo apt update -y && sudo apt install libguestfs-tools -y
virt-customize -a debian-11-genericcloud-amd64-20230124-1270.qcow2 --install qemu-guest-agent
```

```sh
qm create 9001 --name "debian-template" --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0
qm importdisk 9001 debian-11-genericcloud-amd64-20230124-1270.qcow2 local-lvm
qm set 9001 --scsihw virtio-scsi-pci --scsi0 local-lvm:vm-9001-disk-0
qm set 9001 --ide2 local-lvm:cloudinit
qm set 9001 --boot c --bootdisk scsi0
qm set 9001 --serial0 socket --vga serial0
qm template 9001
```

## LXC

## ZFS

## NFS

## Cache
- [Dragonfly](https://d7y.io/)
- `apt-cacher-ng`: [Docker](https://hub.docker.com/r/sameersbn/apt-cacher-ng)
- [[IaC]]