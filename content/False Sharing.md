## Common problems
A common problem in modern architectures with multiprocessor caches is called [false sharing](http://en.wikipedia.org/wiki/False_sharing). This occurs when each individual processor is attempting to use data in another memory region and attempts to store it in the same _cache line_. This causes the cache line -- which contains data another processor can use -- to be overwritten again and again. Effectively, different [[Thread|threads]] make each other wait by inducing cache misses in this situation. See also: [How and when to align to cache line size?](https://stackoverflow.com/questions/8469427/how-and-when-to-align-to-cache-line-size)

- [False sharing - Wikipedia](https://en.wikipedia.org/wiki/False_sharing)
- [[Cache]]