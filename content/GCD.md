# Divisor
A divisor of *n*, also called a factor of *n*, is an integer *m* that can be multiplied by some integer to produce *n*.
and *n* is a multiple of *m*.
$n = km$ then $m | n$ 

# GCD
greatest common divisor. It is also termed as the highest common factor (HCF) or the greatest common factor (GCF).
[Euclidean algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)

## Method 1: prime factorizations
to compute $gcd(48, 180)$, we find the prime factorizations $48 = 2^4 \cdot 3^1$ and $180 = 2^2 \cdot 3^2 \cdot 5^1$; the GCD is then $2^{min(4,2)} · 3^{min(1,2)} · 5^{min(0,1)} = 2^2 · 3^1 · 5^0 = 12$

## Method 2: Euclidean algorithm
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
