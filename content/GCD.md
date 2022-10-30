---
aliases: [LCF]
tags: [] 
date created: Jul 14th, 2022
date modified: Oct 30th, 2022
---
# Divisor
A divisor of *n*, also called a factor of *n*, is an integer *m* that can be multiplied by some integer to produce *n*.  
and *n* is a multiple of *m*.  
$n = km$ then $m | n$ 

# GCD
Greatest common divisor. It is also termed as the highest common factor (HCF) or the greatest common factor (GCF).  
[Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)

## Properties
- $gcd(a, b) = ar + bs$ [[Bezout's Identity]]
- If $gcd(a, n) = 1$ and $gcd(a, m) = 1$ then $gcd(a, mn) = 1$

## Calculate GCD
### Method 1: Prime Factorizations
to compute $gcd(48, 180)$, we find the [[prime]] factorizations $48 = 2^4 \cdot 3^1$ and $180 = 2^2 \cdot 3^2 \cdot 5^1$; the GCD is then $2^{min(4,2)} · 3^{min(1,2)} · 5^{min(0,1)} = 2^2 · 3^1 · 5^0 = 12$  
[I Do Maths · Prime Numbers and Prime Factorization](https://www.idomaths.com/primefactors.php)

### Method 2: Euclidean Algorithm
The Euclidean [[algorithm]] is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

![](https://img.ynchen.me/2022/07/d10227041ae56557de562a6ac57a315d.jpg)

## Code for GCD

```c
int gcd(int a, int b)
{
	if (b == 0)
		return a;
	else
		return gcd(b, a % b);
}
```

1. gcd(0, _v_) = _v_, because everything divides zero, and _v_ is the largest number that divides _v_. Similarly, gcd(_u_, 0) = _u_.
2. gcd(_2u_, _2v_) = 2 · gcd(_u_, _v_)
3. gcd(_2u_, _v_) = gcd(_u_, _v_), if _v_ is odd (2 is not a common divisor). Similarly, gcd(_u_, _2v_) = gcd(_u_, _v_) if _u_ is odd.
4. gcd(_u_, _v_) = gcd(|_u_ − _v_|, min(_u_, _v_)), if _u_ and _v_ are both odd.  

[[Bezout's Identity]]
