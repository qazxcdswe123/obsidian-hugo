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