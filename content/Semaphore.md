---
aliases: []
date created: Mar 20th, 2023
date modified: Jun 4th, 2023
---
one can use semaphores as both locks and condition variables

1. **P operation (also known as wait, sleep, or down operation)**: This operation *decreases* the value of the semaphore. If the semaphore's value becomes negative, the process executing the P operation is blocked, i.e., added to the semaphore's queue.
2. **V operation (also known as signal, wake, or up operation)**: This operation increases the value of the semaphore. If the resulting value is less than or equal to zero, then a process blocked in the semaphore's queue gets unblocked.

## Example
A semaphore is an object with an integer value that we can manipulate with two routines; in the POSIX standard, these routines are `sem_wait()` and `sem_post()`. Because the initial value of the semaphore determines its behavior, before calling any other routine to interact with the semaphore, we must first initialize it to some value.

```c
#include <semaphore.h>
sem_t s;
sem_init(&s, 0, 1);

// Binary Semaphore, aka a lock
sem_wait(&s);
// critical section here 
sem_post(&s);
```


The second argument to `sem_init()` will be set to 0 in all of the examples we’ll see; this indicates that the semaphore is shared between threads in the same process. They can be used to synchronize access across different processes

## Links
- [Producer–consumer problem - Wikipedia](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)
- [[Multi Threading]]