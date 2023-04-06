---
aliases: []
date created: Mar 30th, 2023
date modified: Apr 6th, 2023
---
- Other [[Optimization]]
- Query Optimization is all about finding the **query plan** that minimizes the number of I/Os it takes to execute the query. A query plan is just a sequence of operations that will get us the correct result for a query. We use relational algebra to express it.

## Terms
- Selectivity Estimation
	- Percentage of pages that will make it through the final query

___

## Common Heuristics
1. Push down projects (π) and selects (σ) before [[SQL Join Algorithm|join]]
	- `select` or `project` ASAP
2. Only consider left deep plans 
	- A left deep plan is a plan where all of the right tables in a join are the base tables (in other words, the right side is never the result of a join itself, it can only be one of the original tables).
	- ![image.png](https://img.ynchen.me/2023/04/61006891732ecff3c30500fcce79599e.webp)
3. Avoid cross joins (Cartesian products) unless they are the only option

- Note that you can only project away columns that are not used in the rest of the query (i.e. if they are in a SELECT or a WHERE clause that hasn’t yet been evaluated you can’t get rid of the column).
- These plans can be fully pipelined, meaning that we can pass the pages up one at a time to the next join operator – we don’t actually have to write the result of a join to disk.

## First Pass of System R

- Only one of these joins **produces** a sorted output - sort merge join (SMJ)
- Both simple nested loop join (SNLJ) and index nested loop join (INLJ) can **preserve** a sorted ordering of the left relation.
- Grace Hash Join (GHJ), Page Nested Loop Join (PNLJ), and Block Nested Loop Join (BNLJ) **never** produce an interesting ordering.
- We can’t change the join order, because we are only considering left deep plans, so the base tables must be on the right.

## Notes
- [Query Optimization | Database Systems](https://cs186berkeley.net/notes/note10/)