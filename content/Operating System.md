---
aliases: [OS]
date created: Jul 28th, 2022
date modified: Apr 10th, 2023
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

## Scheduler
- First Come First Serve (FCFS)
	- automatically executes queued requests and processes in order of their arrival
- Shortest Job First (SJF)
- Shortest Time-to-Completion First
- Multi-Level Feedback [[Queue]]
	- If a process uses too much CPU time, it will be moved to a lower-priority queue.
	- If a process is I/O-bound or an interactive process, it will be moved to a higher-priority queue.
	- If a process is waiting too long in a low-priority queue and [starving](https://en.wikipedia.org/wiki/Starvation_(computer_science) "Starvation (computer science)"), it will be [aged](https://en.wikipedia.org/wiki/Aging_(scheduling) "Aging (scheduling)") to a higher-priority queue.
- Proportional-share Scheduling
- Completely Fair Scheduler (CFS)
	- CFS basically models an “ideal, precise multi-tasking CPU” on real [[hardware]].

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