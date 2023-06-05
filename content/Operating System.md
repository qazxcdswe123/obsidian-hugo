---
aliases: [OS]
date created: Jul 28th, 2022
date modified: Jun 4th, 2023
---

## Term
- context  
The operating system keeps track of all the state information that the [[process]] needs in order to run. This state, which is known as the context, includes information such as the current values of the PC, the [[register]] file, and the contents of main [[memory]].

- context switching  
In either case, a single CPU can appear to execute multiple processes concurrently by having the processor switch among them. The operating system performs this interleaving with a mechanism known as context switching.  
When the operating system decides to transfer control from the current [[process]] to some new [[process]], it performs a context switch by saving the context of the current [[process]], restoring the context of the new [[process]], and then passing control to the new [[process]].

- Kernel  
The kernel is the portion of the operating system code that is always resident in [[memory]]  
Note that the kernel is not a separate [[process]]. Instead, it is a collection of code and data structures that the system uses to manage all the processes.

## Goal of OS
- run multiple applications
- isolate them
- multiplex them
- share

## Links
- [Von Neumann architecture - Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)
- [[6.s081]]
- [[Memory]]
- [[Hardware]]
- [[Protection Ring]]
- [[Linux]]
- [[Signals]]
- [[Page]]
- [[Page Table]]
- [[File System]]
- [[Scheduler]]