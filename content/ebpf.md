---
aliases: []
date created: Jan 5th, 2023
date modified: Apr 8th, 2023
---

## Idea
- Compiling eBPF programs into bytecode
- Verifying programs execute safely in a VM before being being loaded at the hook point
- Attaching programs to hook points within the kernel that are triggered by specified events
- Compiling at runtime for maximum efficiency
- Calling helper functions to manipulate data when a program is triggered
- Using maps (key-value pairs) to share data between the user space and kernel space and for keeping state.

## Maps
- allow eBPF program to store and retrieve data in a wide set of data structures
- 

- Hash tables, Arrays
- LRU (Least Recently Used)
- Ring Buffer
- Stack Trace
- LPM (Longest Prefix match)

## Hooks
If a predefined hook does not exist for a particular need, it is possible to create a kernel probe (`kprobe`) or user probe (`uprobe`) to attach eBPF programs almost anywhere in kernel or user applications.

## Links
- [What is eBPF? An Introduction and Deep Dive into the eBPF Technology](https://ebpf.io/what-is-ebpf/)
- [GitHub - iovisor/bcc: BCC - Tools for BPF-based Linux IO analysis, networking, monitoring, and more](https://github.com/iovisor/bcc)