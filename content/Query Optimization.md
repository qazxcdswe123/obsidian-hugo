---
aliases: []
tags: []
date created: Mar 30th, 2023
date modified: Mar 30th, 2023
---
- [[Optimization]]

## Terms
- selectivity estimation
	- Percentage of pages that will make it through

___

## Common Heuristics
1. Push down projects (π) and selects (σ) before [[SQL Join Algorithm|join]]
2. Only consider left deep plans 
3. Do not consider cross joins (Cartesian products) unless they are the only option

- Note that you can only project away columns that are not used in the rest of the query (i.e. if they are in a SELECT or a WHERE clause that hasn’t yet been evaluated you can’t get rid of the column).
- These plans can be fully pipelined, meaning that we can pass the pages up one at a time to the next join operator – we don’t actually have to write the result of a join to disk.

## First Pass