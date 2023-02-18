---
aliases: []
tags: []
date created: Dec 21st, 2022
date modified: Feb 13th, 2023
---
- [[Probability]]

## What
> A **randomized algorithm** is an [algorithm](https://en.wikipedia.org/wiki/Algorithm "Algorithm") that employs a degree of [randomness](https://en.wikipedia.org/wiki/Randomness "Randomness") as part of its logic or procedure. The algorithm typically uses [uniformly random](https://en.wikipedia.org/wiki/Uniform_distribution_(discrete) "Uniform distribution (discrete)") bits as an auxiliary input to guide its behavior, in the hope of achieving good performance in the "average case" over all possible choices of random determined by the random bits; thus either the running time, or the output (or both) are random variables.

## Fisher–Yates Shuffle
[Fisher–Yates shuffle - Wikipedia](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)  
![image.png](https://img.ynchen.me/2023/02/7c7ccf4c9400ec0fdaac7094697fb510.webp)

### The Original Method
1. Pick a random number _k_ between one and the number of unstruck numbers remaining (inclusive). (Choose an unused number)
2. Counting from the low end, strike out the _k_ th number not yet struck out, and write it down at the end of a separate list. (Shuffle it)
3. Repeat from step 2 until all the numbers have been struck out. (Get result)

### Knuth Method
```
-- To shuffle an array a of n elements (indices 0..n-1):
for i from n−1 downto 1 do
     j ← random integer such that 0 ≤ j ≤ i
     exchange a[j] and a[i]
```

## Las Vegas Algorithm
[Las Vegas algorithm - Wikipedia](https://en.wikipedia.org/wiki/Las_Vegas_algorithm)  
It always gives [correct](https://en.wikipedia.org/wiki/Correctness_(computer_science) "Correctness (computer science)") results; that is, it always produces the correct result or it informs about the failure.