---
aliases: [Locking, Lock]
date created: Mar 20th, 2023
date modified: Apr 11th, 2023
---

## Spinlock
In [software engineering](https://en.wikipedia.org/wiki/Software_engineering "Software engineering"), a **spinlock** is a [lock](https://en.wikipedia.org/wiki/Lock_(computer_science) "Lock (computer science)") that causes a [thread](https://en.wikipedia.org/wiki/Thread_(computer_science) "Thread (computer science)") trying to acquire it to simply wait in a loop ("spin") while repeatedly checking whether the lock is available. Since the thread remains active but is not performing a useful task, the use of such a lock is a kind of [busy waiting](https://en.wikipedia.org/wiki/Busy_waiting "Busy waiting").

## Deadlock
![image.png](https://img.ynchen.me/2023/06/f437278e5177c64cc0ddb36739729863.webp)

- [[Dijkstra’s Banker's Algorithm]]  
- What cause deadlock?
	- Mutual exclusion: Threads claim exclusive control of resources that they require (e.g., a thread grabs a lock).
	- Hold-and-wait: Threads hold resources allocated to them (e.g., locks that they have already acquired) while waiting for additional resources (e.g., locks that they wish to acquire).
	- No preemption: Resources (e.g., locks) cannot be forcibly removed from threads that are holding them.
	- Circular wait: There exists a circular chain of threads such that each thread holds one or more resources (e.g., locks) that are being requested by the next thread in the chain.
- How to avoid deadlocks
	- Circular Wait
	- Hold and Wait
- What to do when deadlock happens
	- Kill the one used the least resources.
	 - Fight for resources (wait for resources).

## Mutex Lock
- A binary [[Semaphore]]  
It acts as a gatekeeper to a section of code, allowing only one thread to enter at a time and blocking access to all others.

## Optimistic concurrency control
- 乐观锁：乐观锁在操作数据时非常乐观，认为别人不会同时修改数据。因此乐观锁不会上锁，只是在执行更新的时候判断一下在此期间别人是否修改了数据：如果别人修改了数据则放弃操作，否则执行操作。
- 悲观锁：悲观锁在操作数据时比较悲观，认为别人会同时修改数据。因此操作数据时直接把数据锁住，直到操作完成后才会释放锁；上锁期间其他人不能修改数据。

## Two Phase Locking (2PL)
### Growing Phase (Locking)
The transaction may obtain locks, but cannot release any locks.
transaction can obtain a shared (read) lock or exclusive (write) lock on a data item before it is read or written to.

### Shrinking Phase (Unlocking)
Once the transaction releases its first lock, the second phase starts, in which it can only release locks, but cannot obtain any new locks.
The transaction keeps all the locks until it completes all 'write' operations to maintain isolation and consistency.

The purpose of two-phase locking is to ensure that all the conflicting operations are executed in an order that is equivalent to some serial order to avoid [[concurrency]] related issues like dirty reads, unrepeatable reads, and phantom reads.