> 有两类程序员几乎不出[[Multi Threading|多线程]]bug：一类是啥也不懂，只要涉及到多[[Thread|线程]]就直接上锁；另一类熟读内存模型、体系结构、缓存一致性协议、内存屏障、竞态条件、指令重排……然后决定只要涉及到[[Multi Threading|多线程]]就直接上锁。

## Concurrency
a means to increase performance, _e.g._, to overlap disk I/O requests, to reduce latency by prefetching results to expected queries, or to take advantage of multiple processors.

- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => [[Multi Threading]]
- I/O Bound, Slow I/O, Many connections => Asyncio

## Parallelism
Multi-core 

## Asynchronous
Concurrency is having two tasks run in parallel on separate threads. However, **[[asynchronous]] methods run in parallel but on the same 1 [[thread]]**.


## Links
- [[Coroutine]]
- [[Rust Concurrency]]
- [[Go Async]]
- [[Go Channel]]
- [[Event Based Concurrency]]
- [[CAS]]
- [Dining Philosophers](https://doc.rust-lang.org/1.4.0/book/dining-philosophers.html)