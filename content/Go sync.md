---
aliases: []
date created: Sep 28th, 2022
date modified: Apr 17th, 2023
---


## `sync.WaitGroup`
- [Go by Example: WaitGroups](https://gobyexample.com/waitgroups)  
To wait for multiple [[Goroutine]] to finish, we can use a _wait group_.  
A WaitGroup must not be copied after first use.

**_Share [[memory]] by communicating, don't communicate by sharing memory_**

## `sync.Cond`
`Cond` implements a conditional variable that can be used in scenarios where multiple Readers are waiting for a shared resource ready (if there is only one read and one write, a lock or [[Go Channel]] takes care of it).

## Links
- [[Go Channel]]
- [[Asynchronous]]
- [[Go Error Handling]]
- [[Go defer]]
- [sync package - sync - Go Packages](https://pkg.go.dev/sync)