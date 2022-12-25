---
aliases: [Hashmap]
tags: []
date created: Jun 26th, 2022
date modified: Dec 25th, 2022
---

## What
- Associate array or dictionary
- `std::unordered_map()` in [[C++ STL]]

## Implementation
- [java - Why Are HashMaps Implemented Using Powers of Two? - Stack Overflow](https://stackoverflow.com/questions/53526790/why-are-hashmaps-implemented-using-powers-of-two)
- [[Hashing Function]]

The size of the bucket will be power of 2, since it guarantee to be all 1 in binary. What we only need to do is a [[Binary|Bitwise]] AND operation and that's the module trick.  
E.g. 16 is a power of 2. If you subtract 1 from it, you get 15, whose binary representation is 1111. Now, if you do a bitwise AND of any number with 1111, you're going to get the last 4 bits of the number which, in other words, is equivalent to the modulo of the number by 16 (Division operation is usually an expensive operation. Hence, bitwise operation is usually preferred over division). These last 4 bits will evaluate to any number from 0 to 15 which are the indexes of your underlying array.

### Load Factor

### Collision Resolution
Use **Separate Chaining** or [[Open Addressing]] to deal with it.

## Links
[Wiki](https://en.wikipedia.org/wiki/Hash_table)  
[Algorithm 4E](https://algs4.cs.princeton.edu/34hash/)  
[新式哈希表 - Swiss Tables - 知乎](https://zhuanlan.zhihu.com/p/277732297)  

[[SwissTable]]