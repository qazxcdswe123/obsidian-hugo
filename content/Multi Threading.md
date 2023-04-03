---
aliases: [多进程]
date created: Feb 24th, 2022
date modified: Mar 20th, 2023
---

## Overview
- Relationship between stack and heap
> In a multi-threaded application, each thread will have its own stack. But, all the different threads will share the heap. Because the different threads share the heap in a multi-threaded application, this also means that there has to be some coordination between the threads so that they don’t try to access and manipulate the same piece(s) of memory in the heap at the same time.

- **Concurrency** is when two or more tasks can start, run, and complete in overlapping time **periods**. It doesn't necessarily mean they'll ever both be running **at the same instant**. For example, _multitasking_ on a single-core machine.
- **Parallelism** is when tasks _literally_ run at the same time, e.g., on a multicore processor.

线程：[[Thread]]  
进程：[[Process]]

## Concurrency
a means to increase performance, _e.g._, to overlap disk I/O requests, to reduce latency by prefetching results to expected queries, or to take advantage of multiple processors.

- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
- I/O Bound, Slow I/O, Many connections => Asyncio

## Links
- [difference-between-multiprocessing-and-multithreading](https://www.guru99.com/difference-between-multiprocessing-and-multithreading.html)
- [[Memory]]
- [[CSAPP]]
- [Spinlock - Wikipedia](https://en.wikipedia.org/wiki/Spinlock)
- [[Locks]]
- [[Semaphore]]
- [[Event Loop]]
