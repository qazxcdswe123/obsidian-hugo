---
aliases: []
date created: Mar 30th, 2023
date modified: Apr 20th, 2023
---
- Idea: Query [[Optimization]] is all about finding the **query plan** that minimizes the number of I/Os it takes to execute the query. A query plan is just a sequence of operations that will get us the correct result for a query. We use [[relational algebra]] to express it.

## Terms
- Selectivity Estimation
	- Percentage of pages that will make it through the final query
- Selinger optimizer

___

## Common Heuristics
1. Push down projects (π) and selects (σ) before [[SQL Join Algorithm|join]]
	- `select` or `project` ASAP
2. Only consider left deep plans 
	- Each node represents a relational operation such as a selection, projection, or join.
	- Each leaf is the actual table.
	- ![image.png](https://img.ynchen.me/2023/04/61006891732ecff3c30500fcce79599e.webp)
3. Avoid cross joins (Cartesian products) unless they are the only option

- Note that you can only project away columns that are not used in the rest of the query (i.e. if they are in a SELECT or a WHERE clause that hasn’t yet been evaluated, you can’t get rid of the column).
- These plans can be fully pipelined, meaning that we can pass the pages up one at a time to the next join operator – we don’t actually have to write the result of a join to disk.

## First Pass of System R
(pass i involves finding the best plans for sets of i tables, so pass 1 involves finding the best plans for sets of 1 table).(pass i involves finding the best plans for sets of i tables, so pass 1 involves finding the best plans for sets of 1 table).

- Only one of these joins **produces** a sorted output - [[Sorting Algorithm|sort]] merge join (SMJ)
- Both simple nested loop join (SNLJ) and index nested loop join (INLJ) can **preserve** a sorted ordering of the left relation.
- Grace Hash Join (GHJ), Page Nested Loop Join (PNLJ), and Block Nested Loop Join (BNLJ) **never** produce an interesting ordering.
- We can’t change the join order, because we are only considering left deep plans, so the base tables must be on the right.

### Volcano model
![image.png](https://img.ynchen.me/2023/04/6c7b45747aaf6bf1694a040ed1773c10.webp)  
The operators are layered atop one another, and each operator requests tuples from the input operator(s) as it needs to generate its next output tuple. Note that each operator only fetches tuples from its input operator(s) as needed, rather than all at once! the operators are layered atop one another, and each operator requests tuples from the input operator(s) as it needs to generate its next output tuple. Note that each operator only fetches tuples from its input operator(s) as needed, rather than all at once!

## Notes
- [Query Optimization | Database Systems](https://cs186berkeley.net/notes/note10/)