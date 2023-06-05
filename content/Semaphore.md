---
aliases: []
date created: Mar 20th, 2023
date modified: Jun 4th, 2023
---
1. **P operation (also known as wait, sleep, or down operation)**: This operation *decreases* the value of the semaphore. If the semaphore's value becomes negative, the process executing the P operation is blocked, i.e., added to the semaphore's queue.
2. **V operation (also known as signal, wake, or up operation)**: This operation increases the value of the semaphore. If the resulting value is less than or equal to zero, then a process blocked in the semaphore's queue gets unblocked.

## Links
- [Producer–consumer problem - Wikipedia](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)
