---
aliases: []
tags: []
date created: Oct 9th, 2022
date modified: Oct 9th, 2022
---
[[Storage]]
# Cache
## Overview
We have `t`, `s` and `b`
- A cache is a set of `2^s` cache sets
- A cache set is a set of `E` cache lines
	- `E` is called associativity
	- If `E=1`, it is called “direct-mapped"
- Each cache line stores a block

## Efficiency
- Cache hit: $h = N_{c} / (N_{c} + N_{m})$
	- Nc表示Cache完成存取访问的总次数  
	- Nm表示主存完成存取访问的总次数  
- 平均访问时间: $t_{a} = ht_{c} + (1-h)t_{m}$
	- tc表示命中Cache时的访问时间  
	- tm表示命中主存时的访问时间  
	- $t_{a} = \frac{t_{c}}{e}$
- Cache 访问效率：$e = \frac{1}{r+(1-r)h}$ ($r = \frac{t_{m}}{t_{c}}$ 表示主存慢于cache的倍率)
	- 1 / 慢的倍数 + 快的倍数 x 快的几率




## Details
![](https://img.ynchen.me/2022/10/6f06f0422aced8d2b69b2999ae1002a3.webp)


- cache block: The basic unit for cache storage. May contain multiple bytes/words of data
- cache line: Same as cache block. Note that this is not the same thing as a “row” of cache.
- cache set: A “row” in the cache. The number of blocks per set is determined by the layout of the cache (e.g. direct mapped, set-associative, or fully associative).
- tag: A unique identifier for a group of data.
- valid bit: A bit of information that indicates whether the data in a block is valid (1) or not (0).


## Direct-Mapped
Single cache line pre set (n x 1 column matrix)

### Place a block in cache


## Fully Associative

## Set-Associative
