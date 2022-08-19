---
aliases: [LCF]
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

# Bezout's Identity
[Bézout's identity - Wikipedia](https://en.wikipedia.org/wiki/B%C3%A9zout's_identity?utm_source=pocket_mylist#Proof)

**Bézout's identity** — Let _a_ and _b_ be [integers](https://en.wikipedia.org/wiki/Integer "Integer") with [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor "Greatest common divisor") _d_. Then there exist integers _x_ and _y_ such that _ax_ + _by_ = _d_. Moreover, the integers of the form _az_ + _bt_ are exactly the multiples of _d_.
Here the greatest common divisor of 0 and 0 is taken to be 0. The integers _x_ and _y_ are called **Bézout coefficients** for (_a_, _b_); they are not unique. A pair of Bézout coefficients can be computed by the [extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm "Extended Euclidean algorithm")