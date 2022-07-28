---
aliases: []
tags: [] 
date created: Jul 11th, 2022
date modified: Jul 28th, 2022
---
[Rounding - Wikipedia](https://en.wikipedia.org/wiki/Rounding)

The IEEE floating-point format defines four different rounding modes.

## Round-to-even (round-to-nearest)
- **It's the default mode**
It **first** attempts to find a closest match. Thus, it rounds 1.40 to 1 and 1.60 to 2,  
If it falls halfway, it rounds the number either upward or downward such that the **least significant digit** of the result is **even** (Which in most case means even).
- Why?
	- It will round upward about 50% of the time and round downward about 50% of the time.
	
## Round-toward-zero
Round-toward-zero mode rounds positive numbers **downward** and negative numbers **upward**  
giving $|\hat{x}| \leq |x|$

## Round-down
Round-down mode rounds both positive and negative numbers **downward**  
giving $x^- \leq x$

## Round-up
Round-up mode rounds both positive and negative numbers **upward**  
giving $x^+ \geq x$

## Example
![](https://s2.loli.net/2022/07/11/7H4FQ5IOdZfEDGP.png)

![](https://s2.loli.net/2022/07/11/LdT6MWOxjyGkmhN.png)
