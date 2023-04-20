---
aliases: [Linux File]
date created: Mar 28th, 2023
date modified: Apr 7th, 2023
---

## Linux System's Filesystem Table
- [An introduction to the Linux /etc/fstab file | Enable Sysadmin](https://www.redhat.com/sysadmin/etc-fstab)  
A configuration table designed to ease the burden of mounting and unmounting file systems to a machine.

![image.png](https://img.ynchen.me/2023/04/a9a232590552ea27b02af85837b28c34.webp)

# Special Files
- Block file(b) 
- Character device file(c) 
- Named pipe file or just a pipe file(p) 
- Symbolic link file(l) 
- Socket file(s)

## Block Devices
- Block layer provides an interface between the [[file system]] and the physical storage device, allowing the file system to read and write data to the device
- Block devices are usually implemented with a [[File System]] meant for storing files. Now whenever an userspace application initiates a File I/O operation (read, write), the [[Linux Kernel|kernel]] in turn initiates a sequence of Block I/O operation through File System Manager. The `struct bio` keeps track of all Block I/O transactions (initiated by user app) that is to be processed. That's what is mentioned here as **flight/active** regions.
- [[Memory]] buffers are required by the [[Linux Kernel|kernel]] to hold data to/from Block device.
- The block I/O layer also provides functions that allow the kernel to put data buffers in high [[memory]] and implement a "zero-copy" schema, where disk data is directly put in the User Mode address space without being copied to [[Linux Kernel|kernel]] memory first
- [BIO.pdf](https://www.cs.cornell.edu/courses/cs4410/2021fa/assets/material/lecture24_blk_layer.pdf)

# Links
- [[SPDK]]