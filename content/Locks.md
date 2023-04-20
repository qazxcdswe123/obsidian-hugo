---
aliases: []
date created: Mar 20th, 2023
date modified: Apr 11th, 2023
---

## Spinlock
In [software engineering](https://en.wikipedia.org/wiki/Software_engineering "Software engineering"), a **spinlock** is a [lock](https://en.wikipedia.org/wiki/Lock_(computer_science) "Lock (computer science)") that causes a [thread](https://en.wikipedia.org/wiki/Thread_(computer_science) "Thread (computer science)") trying to acquire it to simply wait in a loop ("spin") while repeatedly checking whether the lock is available. Since the thread remains active but is not performing a useful task, the use of such a lock is a kind of [busy waiting](https://en.wikipedia.org/wiki/Busy_waiting "Busy waiting").

## Deadlock
- [[Dijkstra’s Banker's Algorithm]]  
- What cause deadlock?
	- Deadlock occurs when two or more processes or threads are waiting for a resource that is held by another waiting process or thread.
	- [What Causes Deadlock](https://www.krivalar.com/OS-necessary-conditions-for-deadlock)
- Avoid deadlock.
1. Avoid circular wait: Circular wait occurs when two or more threads or processes are waiting for resources held by each other. To avoid circular wait, resources should be requested in a fixed order, and each thread or process should release all resources before requesting new ones.
2. Use timeouts: If a thread or process is waiting for a resource for too long, it may be a sign of deadlock. To avoid this, a timeout can be set for acquiring a resource. If the resource is not acquired within the timeout period, the thread or process can release the resources it holds and try again later.
3. Use resource allocation graphs: Resource allocation graphs can be used to detect and prevent deadlocks. A resource allocation graph is a directed graph that represents the allocation of resources to threads or processes. If a cycle is detected in the graph, it indicates a potential deadlock. To prevent deadlock, resources can be allocated in a way that avoids cycles in the graph.
4. Use a deadlock detection algorithm: A deadlock detection algorithm can be used to periodically check for deadlocks in a system. If a deadlock is detected, the algorithm can take appropriate action to resolve the deadlock, such as releasing resources or killing processes.
5. Use a lock hierarchy: A lock hierarchy can be used to avoid circular wait. In a lock hierarchy, locks are assigned a unique identifier, and threads or processes must acquire locks in a specific order. This ensures that a thread or process cannot acquire a lock that is held by a thread or process that is waiting for a lock that it holds.
- What to do when deadlock happens
	- Kill the one used the least resources.
	 - Fight for resources (wait for resources).

## Mutex Lock
- A binary [[Semaphore]]  
It acts as a gatekeeper to a section of code, allowing only one thread to enter at a time and blocking access to all others.

## Optimistic concurrency control
- 乐观锁：乐观锁在操作数据时非常乐观，认为别人不会同时修改数据。因此乐观锁不会上锁，只是在执行更新的时候判断一下在此期间别人是否修改了数据：如果别人修改了数据则放弃操作，否则执行操作。
- 悲观锁：悲观锁在操作数据时比较悲观，认为别人会同时修改数据。因此操作数据时直接把数据锁住，直到操作完成后才会释放锁；上锁期间其他人不能修改数据。