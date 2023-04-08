## Ring Level
![image.png](https://img.ynchen.me/2023/04/cdee482779bb6f60f552e50d12cb282d.webp)  
A resource that is accessible to outer level is also accessible to inner level.

## Modes
1. **Supervisor Mode :** 
2. **Hypervisor Mode :** 
- [Linux](https://en.wikipedia.org/wiki/Linux_kernel "Linux kernel"), [macOS](https://en.wikipedia.org/wiki/MacOS "MacOS") and [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "Microsoft Windows") are three operating systems that use supervisor/user mode. To perform specialized functions, user mode code must perform a [system call](https://en.wikipedia.org/wiki/System_call "System call") into supervisor mode or even to the kernel space where trusted code of the operating system will perform the needed task and return the execution back to the userspace. Additional code can be added into kernel space through the use of [loadable kernel modules](https://en.wikipedia.org/wiki/Loadable_kernel_module), but only by a user with the requisite permissions, as this code is not subject to the access control and safety limitations of user mode.


- [[syscall]]