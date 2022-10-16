---
aliases: []
tags: []
date created: Oct 9th, 2022
date modified: Oct 9th, 2022
---
# Cache
## Overview
We have `t`, `s` and `b`
- A cache is a set of `2^s` cache sets
- A cache set is a set of `E` cache lines
	- `E` is called associativity
	- If `E=1`, it is called “direct-mapped"
- Each cache line stores a block

## Details
![](https://img.ynchen.me/2022/10/6f06f0422aced8d2b69b2999ae1002a3.webp)


- cache block: The basic unit for cache storage. May contain multiple bytes/words of data
- cache line: Same as cache block. Note that this is not the same thing as a “row” of cache.
- cache set: A “row” in the cache. The number of blocks per set is determined by the layout of the cache (e.g. direct mapped, set-associative, or fully associative).
- tag: A unique identifier for a group of data.
- valid bit: A bit of information that indicates whether the data in a block is valid (1) or not (0).


