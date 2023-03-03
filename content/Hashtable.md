---
aliases: [Hashmap]
tags: []
date created: Jun 26th, 2022
date modified: Jan 17th, 2023
---

## What
- Associate array or dictionary
- `std::unordered_map()` in [[C++ STL]]
- A hash table works by taking the modulus of the hash over the number of buckets.

## Implementation
- [java - Why Are HashMaps Implemented Using Powers of Two? - Stack Overflow](https://stackoverflow.com/questions/53526790/why-are-hashmaps-implemented-using-powers-of-two)
- [[Hashing]]

The size of the bucket will be power of 2, since it guarantee to be all 1 in binary. What we only need to do is a [[Binary|Bitwise]] AND operation and that's the module trick.  
E.g. 16 is a power of 2. If you subtract 1 from it, you get 15, whose binary representation is 1111. Now, if you do a bitwise AND of any number with 1111, you're going to get the last 4 bits of the number which, in other words, is equivalent to the modulo of the number by 16 (Division operation is usually an expensive operation. Hence, bitwise operation is usually preferred over division). These last 4 bits will evaluate to any number from 0 to 15 which are the indexes of your underlying array.

### Load Factor
The number of keys in bucket.

### Collision Resolution
Use **Separate Chaining** or [[Open Addressing]] to deal with it.

## Why Use a Prime Number as a Mod in a Hashing Function
- [language agnostic - Why should hash functions use a prime number modulus? - Stack Overflow](https://stackoverflow.com/questions/1145217/why-should-hash-functions-use-a-prime-number-modulus)
- [data structures - Why is it best to use a prime number as a mod in a hashing function? - Computer Science Stack Exchange](https://cs.stackexchange.com/questions/11029/why-is-it-best-to-use-a-prime-number-as-a-mod-in-a-hashing-function/64191)
We can not control the output of the hash function, so if it is a biased hash function that are likely to return multiple of `n`, and after we mod `n` it all goes to the same bucket which is not good.

## Links
- [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)  
- [Algorithm 4E](https://algs4.cs.princeton.edu/34hash/)  
- [新式哈希表 - Swiss Tables - 知乎](https://zhuanlan.zhihu.com/p/277732297)  

- [[SwissTable]]