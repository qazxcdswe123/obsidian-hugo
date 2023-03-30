- Semaphores provide two operations: wait (P) and signal (V).

The wait operation decrements the value of the semaphore, and the signal operation increments the value of the semaphore. When the value of the semaphore is zero, any [[process]] that performs a wait operation will be blocked until another [[process]] performs a signal operation.

Both operations are atomic, meaning that the variable on which read, modify, and update happens at the same time/moment with no preemption. In other words, in-between read, modify, and update, no other operation is performed that may change the variable. A critical section is surrounded by both operations to implement [[process]] synchronization.

## Links
- [Producer–consumer problem - Wikipedia](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)