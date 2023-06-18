---
aliases: [LRU, LFR, MRU]
date created: Mar 19th, 2023
date modified: Jun 4th, 2023
---
In [[Buffer Management]] and [[Page]]

## LRU

### Clock Algorithm
Use a ref bit (recently referenced) in the metadata table and a clock hand variable to track the current frame in consideration.  
If there is a ref bit, clear it. If not, evict it.

## MRU
measured by when the [[page]]’s pin count was last decremented.

## OPT
chooses the one that won't be used for the longest time in the future.