---
aliases: [多进程]
tags: [CSAPP, ] 
date created: Feb 24th, 2022
date modified: Aug 19th, 2022
---
- Relationship between stack and heap
> In a multi-threaded application, each thread will have its own stack. But, all the different threads will share the heap. Because the different threads share the heap in a multi-threaded application, this also means that there has to be some coordination between the threads so that they don’t try to access and manipulate the same piece(s) of memory in the heap at the same time.

线程：[[Thread]]  
进程：[[Process]]

[difference-between-multiprocessing-and-multithreading](https://www.guru99.com/difference-between-multiprocessing-and-multithreading.html)

- [[Memory]]
- [[CSAPP]]