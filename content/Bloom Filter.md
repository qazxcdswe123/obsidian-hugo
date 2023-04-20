---
aliases: []
date created: Dec 21st, 2022
date modified: Apr 8th, 2023
---

## What
A space-efficient [[Probability|probabilistic]] data structure to test whether an element is a member of a set.

## Implementation
Use $n$ bits array and $m$ hashing functions. Apply all $m$ functions to the input and $\mod n$, then we can set all $m$ results bits to 1.

## Design
- Use random keys in order to minimize the chance that a false positive for one user is a false positive for all.
- If it returns negative, then we can guarantee that it's not in the bloom filter.
- If it returns positive, then it may be in bloom filter.

## Links
- [chrome/browser/safe\_browsing/bloom\_filter.cc - chromium/chromium - Git at Google](https://chromium.googlesource.com/chromium/chromium/+/refs/heads/main/chrome/browser/safe_browsing/bloom_filter.cc)
- [Bloom filter calculator](https://hur.st/bloomfilter)
- [[Algorithm]]
- [[Probability]]
- [[Hashing]]
- Counting Filter / Cuckoo Filter

___

There is also another filter called *cuckoo filter*, which should be practically better than bloom filter since it supports **deletion**.
- [https://www.cs.cmu.edu/\~dga/papers/cuckoo-conext2014.pdf](https://www.cs.cmu.edu/~dga/papers/cuckoo-conext2014.pdf)
- [Cuckoo filter - Wikipedia](https://en.wikipedia.org/wiki/Cuckoo_filter)
- [Cuckoo hashing - Wikipedia](https://en.wikipedia.org/wiki/Cuckoo_hashing)