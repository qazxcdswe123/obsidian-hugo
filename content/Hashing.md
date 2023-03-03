---
aliases: []
tags: []
date created: Nov 23rd, 2022
date modified: Feb 26th, 2023
---

# Overview and Difference
- A **[[checksum]]** (such as CRC32) is to prevent _accidental_ changes. If one byte changes, the [[checksum]] changes. The [[checksum]] is not safe to protect against malicious changes: it is pretty easy to create a file with a particular [[checksum]].  
- A **hash function** maps some data to other data. It is often used to speed up comparisons or create a hash table. Not all hash functions are secure and the hash does not necessarily changes when the data changes.  
- A **cryptographic hash function** (such as SHA1) is a [[checksum]] that is secure against malicious changes. It is pretty hard to create a file with a specific cryptographic hash.  
- To make things more complicated, cryptographic hash functions are sometimes simply referred to as hash functions.

# Algorithms
- [[MD5]]
- [[SHA]]

## Fibonacci Hash
- [Fibonacci Hashing: The Optimization that the World Forgot (or: a Better Alternative to Integer Modulo) | Probably Dance](https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/)

## Naive
```c
unsigned long hash_function(char* str) {
    unsigned long i = 0;
    for (int j=0; str[j]; j++)
        i += str[j];
    return i % CAPACITY;
}
```