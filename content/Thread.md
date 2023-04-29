---
aliases: [线程]
date created: Jul 28th, 2022
date modified: Jul 28th, 2022
---

Although we normally think of a [[process]] as having a single control flow, in modern systems a [[process]] can actually consist of multiple execution units, called threads, each running in the context of the [[process]] and sharing the same code and global data.

## Thread Safe
thread-safe code ensures that when a thread is modifying or reading shared data, no other thread can access it in a way that changes the data

## Links
- [[Operating System]]
- [[Asynchronous]]
- [[Rust Ownership]]?