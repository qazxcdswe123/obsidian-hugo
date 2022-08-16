---
aliases: []
tags: [] 
date created: Jul 14th, 2022
date modified: Aug 16th, 2022
---
# Divisor
A divisor of *n*, also called a factor of *n*, is an integer *m* that can be multiplied by some integer to produce *n*.  
and *n* is a multiple of *m*.  
$n = km$ then $m | n$ 

# GCD
greatest common divisor. It is also termed as the highest common factor (HCF) or the greatest common factor (GCF).  
[Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)

## Properties
- relatively prime
	- We say that two integers a and b are relatively prime if gcd(a, b) = 1.
- Let `a` and `b` be two integers that are relatively prime. Then there exist integers `r` and `s` such that $ar + bs = 1$.
- $gcd(a, b) = ar + bs$

## Method 1: [[Prime]] Factorizations
to compute $gcd(48, 180)$, we find the prime factorizations $48 = 2^4 \cdot 3^1$ and $180 = 2^2 \cdot 3^2 \cdot 5^1$; the GCD is then $2^{min(4,2)} · 3^{min(1,2)} · 5^{min(0,1)} = 2^2 · 3^1 · 5^0 = 12$  
[I Do Maths · Prime Numbers and Prime Factorization](https://www.idomaths.com/primefactors.php)

## Method 2: Euclidean Algorithm
The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

## Proof
### Euclid
![](https://img.ynchen.me/2022/07/d10227041ae56557de562a6ac57a315d.jpg)

## Code

```c
int gcd(int a, int b)
{
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
}
```

[[LCM]]
