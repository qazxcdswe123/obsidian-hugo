---
aliases: []
tags: []
date created: Oct 9th, 2022
date modified: Oct 9th, 2022
---
![](https://img.ynchen.me/2022/10/b7dc1a6b16a372773b1e68a8c3593a2b.webp)

- cache block: The basic unit for cache storage. May contain multiple bytes/words of data
- cache line: Same as cache block. Note that this is not the same thing as a “row” of cache.
- cache set: A “row” in the cache. The number of blocks per set is determined by the layout of the cache (e.g. direct mapped, set-associative, or fully associative).
- tag: A unique identifier for a group of data.
- valid bit: A bit of information that indicates whether the data in a block is valid (1) or not (0).