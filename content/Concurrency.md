> 有两类程序员几乎不出多线程bug：一类是啥也不懂，只要涉及到多线程就直接上锁；另一类熟读内存模型、体系结构、缓存一致性协议、内存屏障、竞态条件、指令重排……然后决定只要涉及到多线程就直接上锁。

## Concurrency
a means to increase performance, _e.g._, to overlap disk I/O requests, to reduce latency by prefetching results to expected queries, or to take advantage of multiple processors.

- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => [[Multi Threading]]
- I/O Bound, Slow I/O, Many connections => Asyncio

## Links
- [golang atomic maps](https://go.dev/doc/faq#atomic_maps)
- [GitHub - orcaman/concurrent-map: a thread-safe concurrent map for go](https://github.com/orcaman/concurrent-map)
- [象牙山刘能 on Twitter: "有两类程序员几乎不出多线程bug：一类是啥也不懂，只要涉及到多线程就直接上锁；另一类熟读内存模型、体系结构、缓存一致性协议、内存屏障、竞态条件、指令重排……然后决定只要涉及到多线程就直接上锁。" / Twitter](https://twitter.com/disksing/status/1582017780294946817)
- [[Coroutine]]