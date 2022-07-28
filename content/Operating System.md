---
aliases: [OS]
tags: [] 
date created: Jul 28th, 2022
date modified: Jul 28th, 2022
---

- context
The operating system keeps track of all the state information that the [[process]] needs in order to run. This state, which is known as the context, includes information such as the current values of the PC, the [[register]] file, and the contents of main [[memory]].

- context switching
In either case, a single CPU can appear to execute multiple processes concurrently by having the processor switch among them. The operating system performs this interleaving with a mechanism known as context switching.
When the operating system decides to transfer control from the current [[process]] to some new [[process]], it performs a context switch by saving the context of the current [[process]], restoring the context of the new [[process]], and then passing control to the new [[process]].

- kernel
The kernel is the portion of the operating system code that is always resident in [[memory]]
Note that the kernel is not a separate process. Instead, it is a collection of code and data structures that the system uses to manage all the processes.

- [Von Neumann architecture - Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)