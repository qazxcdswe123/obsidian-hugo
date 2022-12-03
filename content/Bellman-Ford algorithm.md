---
aliases: []
tags: [Algorithm/Graph, ] 
date created: Nov 24th, 2022
date modified: Nov 24th, 2022
---

## What
The Bellman-Ford algorithm solves the single-source shortest-paths problem in the general case in which edge weights may be negative. It returns a boolean value indicating whether there is a negative-weight cycle that is reachable from the source. **If there is such a cycle, the algorithm indicates that no solution exists. If there is no such cycle, the algorithm produces the shortest paths and their weights.**  
Takes $O(n^{3})$ time.  
Works like [[BFS]]  
![](https://img.ynchen.me/2022/11/b47ea8e6cc568208abac7ed690350868.webp)

## How
Use [[Graph Relax]] Method, call [[Graph Relax|Relax]] on every edge `n-1` times (n = number of vertex)

## Find Negative Weight Cycle
It can also be used to find whether the graph has negative weight cycle.  
![](https://img.ynchen.me/2022/11/b5dab1fef08af5689cd1ac9da5ed64c6.webp)

## Links