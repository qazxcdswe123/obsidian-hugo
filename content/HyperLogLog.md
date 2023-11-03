---
aliases:
  - HLL
link: []
date created: Sep 5th, 2023
date modified: Sep 5th, 2023
---
A probabilistic data structure to count unique items.
provides a very good approximation of the cardinality of a set even using a very small amount of memory. In the Redis implementation it only uses 12kbytes per key to count with a standard error of 0.81%, and there is no limit to the number of items you can count, unless you approach 2^64 items

## Links
[HyperLogLog | Redis](https://redis.io/docs/data-types/probabilistic/hyperloglogs/)