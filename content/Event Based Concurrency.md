---
aliases: []
date created: Jun 18th, 2023
date modified: Jun 18th, 2023
---

## What
CONCURRENT SERVERS WITHOUT [[Thread|THREADS]]

## How
- `select()`
- `poll()`
- `epoll()`

## Why
- Pros: No [[Lock]] needed.
- Cons: 
	- Blocking System Calls because only one thread is running. Unlike thread based [[concurrency]] which can have another thread running while doing [[IO]].

## Links
- [[NodeJS]]
- [[JavaScript Event Loop]]
- epoll