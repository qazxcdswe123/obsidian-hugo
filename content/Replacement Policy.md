---
aliases: [LRU, LFR, MRU]
tags: []
date created: Mar 19th, 2023
date modified: Mar 19th, 2023
---
In [[Buffer Management]]

# LRU

## Clock Algorithm
Use a ref bit (recently referenced) in the metadata table and a clock hand variable to track the current frame in consideration.
If there is a ref bit, clear it. If not, evict it.

# MRU
measured by when the page’s pin count was last decremented.