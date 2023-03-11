---
aliases: [多进程]
tags: [CSAPP, ] 
date created: Feb 24th, 2022
date modified: Mar 6th, 2023
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

## Spinlock
In [software engineering](https://en.wikipedia.org/wiki/Software_engineering "Software engineering"), a **spinlock** is a [lock](https://en.wikipedia.org/wiki/Lock_(computer_science) "Lock (computer science)") that causes a [thread](https://en.wikipedia.org/wiki/Thread_(computer_science) "Thread (computer science)") trying to acquire it to simply wait in a loop ("spin") while repeatedly checking whether the lock is available. Since the thread remains active but is not performing a useful task, the use of such a lock is a kind of [busy waiting](https://en.wikipedia.org/wiki/Busy_waiting "Busy waiting").

## Links
- [difference-between-multiprocessing-and-multithreading](https://www.guru99.com/difference-between-multiprocessing-and-multithreading.html)
- [[Memory]]
- [[CSAPP]]
- [Spinlock - Wikipedia](https://en.wikipedia.org/wiki/Spinlock)