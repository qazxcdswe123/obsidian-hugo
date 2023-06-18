---
aliases: [进程]
date created: Jul 28th, 2022
date modified: Jul 28th, 2022
---

A process is the [[operating system]]'s abstraction for a running program
- Running: In the running state, a process is running on a processor. This means it is executing instructions.
- Ready: In the ready state, a process is ready to run but for some reason the OS has chosen not to run it at this given moment.
- Blocked: In the blocked state, a process has performed some kind of operation that makes it not ready to run until some other event takes place. A common example is when a process initiates an I/O request to a disk. It becomes blocked, allowing some other process to use the processor.

[[State Machine]] of a process
![image.png](https://img.ynchen.me/2023/06/732627331f20f7e2a3c2a06d9d576730.webp)

## Zombie Process
