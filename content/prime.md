---
aliases: []
tags: []
date created: Aug 16th, 2022
date modified: Aug 16th, 2022
---
[[modular]]

## Term
### Composite
An integer n > 1 that is not prime is said to be composite

## Properties
### Lemma 2.13 Euclid
Let a and b be integers and p be a prime number. If p | ab, then either p | a or p | b.

## Primality Test
[Primality test - Wikipedia](https://en.wikipedia.org/wiki/Primality_test)

## Mod 6 Prime Test
Observe that all primes greater than 3 are of the form $6k \pm 1$, where _k_ is any integer greater than 0.  
This is because all integers can be expressed as $6k + i$ where $i = -1, 0, 1, 2, 3, 4$ . Note that *2* divides *6k* and *6k + 2* and *6k + 4*, *3* divides *6k + 3*. So, a more efficient method is to test whether _n_ is divisible by 2 or 3, then to check through all numbers of the form $6k \pm 1 \leq \sqrt n$. This is 3 times faster than testing all numbers up to $\sqrt n$

## Miller-Rabin
[Miller–Rabin primality test - Wikipedia](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

## Qsieve
[Quadratic sieve - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_sieve)