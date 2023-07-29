---
aliases: [proxmox, homelab]
date created: Mar 28th, 2023
date modified: Mar 31st, 2023
---
- 换源：
	- [Proxmox 源使用帮助 — USTC Mirror Help 文档](https://mirrors.ustc.edu.cn/help/proxmox.html)
- 修改 [[IP]] 地址
	- [Proxmox Virtual Environment（PVE）完美的更改IP地址 - 知乎](https://zhuanlan.zhihu.com/p/354038479)
 - Use [[Tailscale]] to connect
 - Template:
	 - Right click to clone
	 - Base image
  - CT: [[Operating system]] container
  - [[Docker]]
  - Use `xterm.js`:
	  - Add serial port on hardware
	  - Change display to serial terminal
   - Resize disk: `qm resize 1001 scsi0 +18G`
   - [Firewall - Proxmox VE](https://pve.proxmox.com/wiki/Firewall)

## Force Quit Vm
```
rm /var/lock/qemu-server/lock-1001.conf
qm unlock 1001
# then stop the vm
```

## `perl: warning: Falling back to a fallback locale ("en_US.UTF-8").`
```
cat << EOF >> ~/.bashrc
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
EOF
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
- [Index of /images/cloud/bullseye](https://cloud.debian.org/images/cloud/bullseye/latest)  
Cloud images are operating system templates and every instance starts out as an identical clone of every other instance. It is the user data that gives every cloud instance its personality and cloud-init is the tool that applies user data to your instances automatically.

- `virt-customize`

```sh
# On host
# sudo apt update -y && sudo apt install libguestfs-tools -y
virt-customize -a debian-11-genericcloud-amd64.qcow2 --install qemu-guest-agent

# virt-customize -a debian-11-genericcloud-amd64.qcow2 --install qemu-guest-agent --append-line '/etc/apt/apt.conf.d/proxy:Acquire::http::Proxy "http://192.168.2.22:3142";'
```

```sh
qm create 1001 --name "debian-template" --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0
qm importdisk 1001 debian-11-genericcloud-amd64.qcow2 local-btrfs
qm set 1001 --scsihw virtio-scsi-single --scsi0 local-btrfs:vm-1001-disk-0
qm set 1001 --ide2 local-btrfs:cloudinit
qm set 1001 --boot c --bootdisk scsi0
qm set 1001 --serial0 socket --vga serial0
qm template 1001
```

## LXC
- resize CT's volume

```sh
# pct resize <vmid> <disk> <size> [OPTIONS]
pct resize 1002 rootfs 108G
```

## QEMU
- Resize vm disk

```sh
# qm resize <vmid> <disk> <size>
qm resize 1001 virtio0 +25G
```

## NFS

## Cache
- [Dragonfly](https://d7y.io/)
- `apt-cacher-ng`: [Docker](https://hub.docker.com/r/sameersbn/apt-cacher-ng)
- [[IaC]]
