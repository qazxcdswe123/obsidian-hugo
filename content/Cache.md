---
aliases: []
tags: [Storage, Cache, Optimization] 
date created: Oct 9th, 2022
date modified: Jan 11th, 2023
---
- [What is a "cache-friendly" code? - Stack Overflow](https://stackoverflow.com/questions/16699247/what-is-a-cache-friendly-code)
## Overview
We have `t`, `s` and `b`
- A cache is a set of `2^s` cache sets
- A cache set is a set of `E` cache lines
	- `E` is called associativity
	- If `E=1`, it is called “direct-mapped"
- Each cache line stores a block
- We need to add tags to the cache, which supply the rest of the address bits to let us distinguish between different memory locations that map to the same cache block.

## Efficiency
- Cache hit: $h = N_{c} / (N_{c} + N_{m})$
	- Nc 表示 Cache 完成存取访问的总次数  
	- Nm 表示主存完成存取访问的总次数  
- 平均访问时间: $t_{a} = ht_{c} + (1-h)t_{m}$
	- tc 表示命中 Cache 时的访问时间  
	- tm 表示命中主存时的访问时间  
	- $t_{a} = \frac{t_{c}}{e}$
- Cache 访问效率：$e = \frac{t_{c}}{t_{a}}$

## Details
![](https://img.ynchen.me/2022/11/587cadee5cf122a2f27db692a8d69cc9.webp)

![](https://img.ynchen.me/2022/10/6f06f0422aced8d2b69b2999ae1002a3.webp)


- cache block: The basic unit for cache storage. May contain multiple bytes/words of data
- cache line: Same as cache block. Note that this is not the same thing as a “row” of cache.
- cache set: A “row” in the cache. The number of blocks per set is determined by the layout of the cache (e.g. direct mapped, set-associative, or fully associative).
- tag: A unique identifier for a group of data.
- valid bit: A bit of information that indicates whether the data in a block is valid (1) or not (0).
- index: the index of the position in cache block

- [Cache placement policies - Wikipedia](https://en.wikipedia.org/wiki/Cache_placement_policies)

## Look Aside Cache
_Look-Aside Caching_ is a pattern of caching where the input of a cacheable operation is used as the key for looking up any cached results from a prior invocation of the operation when given the same input.

## Direct-Mapped
Only 1 choice of where to place a block.  
Single cache line pre set (n x 1 column matrix)  
![](https://img.ynchen.me/2022/11/3b09bc2f92b493b01f43ce14e1d1836b.webp)

## Fully Associative
- 主存总容量：$2^{S}$ （块）x $2^{W}$ （字）
- Cache 总容量：$2^{r}$ x $2^{W}$
- CAM $2^{r}$ 行，每行 S 位 Tag（选主存），需遍历  
随便放，用 Tag 区分， Tag 是内存地址

## Set-Associative
- The cache is divided into groups of blocks, called sets.
- Each memory address maps to exactly one set in the cache, but data may be placed in any block within that set.
