---
aliases: [system call]
date created: Apr 4th, 2023
date modified: Jun 17th, 2023
---
Can be used in perf/latency measurement.  

| # | Layer       | Components                                                            |
|---|-------------|-----------------------------------------------------------------------|
| 1 | Userspace   | user application                                                      |
| 2 | Userspace   | GNU C library (glibc)                                                 |
| 3 | Kernelspace | System Call Interface                                                 |
| 4 | Kernelspace | Subsystems: virtual filesystem, [[memory]] management, [[process]] management |
| 5 | Kernelspace | Architecture Dependent Code, device drivers                           |
| 6 | [[Hardware]]    | Physical devices                                                      |

## How
To execute a system call, a program must execute a special [[Trap]] instruction. This instruction simultaneously jumps into the [[Linux Kernel|kernel]] and raises the privilege level to kernel mode; once in the kernel, the system can now perform whatever privileged operations are needed (if allowed), and thus do the required work for the calling [[process]].  
When finished, the [[Operating System|OS]] calls a special return-from-trap instruction, which, as you might expect, returns into the calling user program while simultaneously reducing the privilege level back to user mode.

To specify the exact system call, a system-call number is usually assigned to each system call. The user code is thus responsible for placing the desired system-call number in a register or at a specified location on the [[stack]]; the OS, when handling the system call inside the trap handler, examines this number, ensures it is valid, and, if it is, executes the corresponding code. This level of indirection serves as a form of **protection**; user code cannot specify an exact address to jump to, but rather must request a particular service via number

Being able to execute the instruction to tell the hardware where the trap tables are is a very powerful capability. Thus, as you might have guessed, it is also a **privileged** operation.