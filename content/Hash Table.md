---
aliases: []
tags: []
date created: Jun 26th, 2022
date modified: Nov 23rd, 2022
---

## What
- Associate array or dictionary
- `std::unordered_map()` in [[C++ STL]]

## Implementation
We set prime numbers of bucket to leverage modulo arithmetic and avoid collision.
[[Hashing Function]]

### Collision Resolution
Use **Separate Chaining** or [[Open Addressing]] to deal with it.

## Links
[Wiki](https://en.wikipedia.org/wiki/Hash_table)  
[Algorithm 4E](https://algs4.cs.princeton.edu/34hash/)
