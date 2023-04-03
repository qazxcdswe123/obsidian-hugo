---
aliases: []
date created: Mar 21st, 2023
date modified: Mar 22nd, 2023
---
## Overview
Because we cannot fit all of the data in [[memory]] at once, we’ll need to build several different hash tables and concatenate them together.

## How to
- [[Divide and Conquer]] [[algorithm]] to partition and hash
We have $B$ buffers, hash each record to $B-1$ partitions. A partition is a set of pages such that for a particular hash function, the values on the pages all hash to the same hash value. We need save 1 buffer for the input buffer.
When output buffer filled, flush it to disk. The two pages that came from the same buffer will be placed adjacently. The most important property of each partition is that if a certain value appears in that partition, all occurrences of that value in our data appear in that partition.

![image.png](https://img.ynchen.me/2023/03/81ba65fa29c798b0d9f3c4286fb73320.webp)


## Links
- [[External Sort]]
- [[DBMS]]
