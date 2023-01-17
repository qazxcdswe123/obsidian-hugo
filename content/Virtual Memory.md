---
aliases: []
tags: []
date created: Dec 24th, 2022
date modified: Jan 11th, 2023
---

## Virtual Memory
Each [[process]] has the same uniform view of memory, which is known as its virtual address space.  
In [[Linux]], the topmost region of the address space is reserved for code and data in the [[operating system]] that is common to all processes. The lower region of the address space holds the code and data defined by the user's [[process]].

![](https://i.stack.imgur.com/HOY4C.png)  
- [memory management - Stack and Heap locations in RAM - Stack Overflow](https://stackoverflow.com/questions/32418750/stack-and-heap-locations-in-ram)
- [[Memory]]
- [TLB-Translation lookaside buffer - Wikipedia](https://en.wikipedia.org/wiki/Translation_lookaside_buffer)
- [[Page Table]]