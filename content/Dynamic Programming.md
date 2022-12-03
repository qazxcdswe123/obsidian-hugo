---
aliases: [DP, 动态规划]
tags: [] 
date created: Aug 15th, 2022
date modified: Aug 15th, 2022
---
## What
Dynamic programming typically applies to optimization problems in which we make a set of choices in order to arrive at an optimal solution. As we make each choice, subproblems of the same form often arise. 
Dynamic programming is effective when a given subproblem may arise from more than one partial set of choices; **the key technique is to store the solution to each such subproblem in case it should reappear.**

## How
Store a DP table  for value that have been computed, in case it will we need to lookup it later.
One trick is to first determine how big the table should be, in some cases we only need $O(1)$ memory not $O(n)$

## Examples
Longest common subsequence.

## Links
