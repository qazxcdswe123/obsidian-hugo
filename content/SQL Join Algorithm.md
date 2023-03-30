---
aliases: []
tags: []
date created: Mar 25th, 2023
date modified: Mar 25th, 2023
---

- Notations:
	- $[T]$: Number of pages in table T
	- $\rho_T$: The number of records on each page of T
	- $|T|$: The total number of records in table T, $|T| = [T] \times \rho_T$

# Nested Loop Join

## Simple Nested Loop Join
- [[IO]] Count: $[R] + |R|[S]$  
![](https://img.ynchen.me/2023/03/c77e2b1649c4f28e8313e0fa2c437d92.gif)

## Page Nested Loop Join
- [[IO]] Count: $[R] + [R][S]$
	- $S$ should be the smaller table to minimize the [[IO]] cost.
- Read in every single page in $S$ for every single page of $R$  
![](https://img.ynchen.me/2023/03/48c72e2d32f3b9e0a280149d29c198b3.gif)

## Block Nested Loop Join
We have $B$ buffer pages, give $B-2$ pages for $R$ and match $S$ against every record in the buffer.
- [[IO]] Count: $[R] + \frac{[R]}{B-2}[S]$  
![B=4](https://img.ynchen.me/2023/03/075f638f1fe558ca40d928612b34dcbc.gif)

# Hash Join

## Grace Hash Join
Grace hash join is a type of hash join [[algorithm]] used in database systems to join two large tables that cannot fit in [[memory]].
Repeatedly hash $R$ and $S$ into $B-1$ buffers so that we can get partitions that are $\leq B - 2$ pages big.

# [[Sorting Algorithm|Sort]] Merge Join
- [[IO]] Count: Cost to sort $R$ and $S$ $+ ([R] + [S])$
- [[External Sort]]
- If first input is smaller than second input, advance
- advance second input till end
- advance first input till end
![](https://img.ynchen.me/2023/03/9385d58b46c5d0e4d16bd388577255a8.gif)

## Links
- [Category:Join algorithms - Wikipedia](https://en.wikipedia.org/wiki/Category:Join_algorithms)
- [[Hashtable]]