> 有两类程序员几乎不出[[Multi Threading|多线程]]bug：一类是啥也不懂，只要涉及到多[[Thread|线程]]就直接上锁；另一类熟读内存模型、体系结构、缓存一致性协议、内存屏障、竞态条件、指令重排……然后决定只要涉及到[[Multi Threading|多线程]]就直接上锁。

> “Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once” – Rob Pike

## Concurrency
- To overlap disk [[IO|I/O]] requests
- To reduce latency by prefetching results to expected queries
- To take advantage of multiple processors.

## Parallelism
Multi [[process]].

## [[Asynchronous]]
Concurrency is having two tasks run in parallel on separate threads. However, **[[asynchronous]] methods run in parallel but on the same [[thread]]**.

## Links
- [[Coroutine]]
- [[Rust Concurrency]]
- [[Go Concurrency Pattern]]
- [[Go sync]]
- [[Go Channel]]
- [[Event Based Concurrency]]
- [[CAS]]
- [[CSP]]
- [Dining Philosophers](https://doc.rust-lang.org/1.4.0/book/dining-philosophers.html)