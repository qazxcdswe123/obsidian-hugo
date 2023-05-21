---
aliases: [线程]
date created: Jul 28th, 2022
date modified: May 15th, 2023
---

Although we normally think of a [[process]] as having a single control flow, in modern systems a [[process]] can actually consist of multiple execution units, called threads, each running in the context of the [[process]] and sharing the same code and global data.

## Problems
- Race conditions, where threads are accessing data or resources in an inconsistent order
- Deadlocks, where two threads are waiting for each other, preventing both threads from continuing
- Bugs that happen only in certain situations and are hard to reproduce and fix reliably  

## Thread Safe
thread-safe code ensures that when a thread is modifying or reading shared data, no other thread can access it in a way that changes the data

## Lightweight Thread
- [[Goroutine]]
	- [Why is goroutine being called a “lightweight” thread? | by Jessie Kuo | Medium](https://medium.com/@jessie_kuo/why-is-goroutine-being-called-a-lightweight-thread-46d70d198ad6)
- [[Java]] virtual thread.

## Thread Pool


## Links
- [[Operating System]]
- [[Asynchronous]]
- [[Locks]]