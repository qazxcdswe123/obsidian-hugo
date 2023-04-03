---
aliases: []
date created: Jan 30th, 2023
date modified: Feb 14th, 2023
---

## Difference From Standard [[SQL Query]]
- There is support for `LEFT OUTER JOIN` but not `RIGHT OUTER` or `FULL OUTER`.
	- To get equivalent output to `RIGHT OUTER` you can reverse the order of the tables (i.e. `A RIGHT JOIN B` is the same as `B LEFT JOIN A`.
	- While it isn't required to complete this assignment, the equivalent to `FULL OUTER JOIN` can be done by `UNION`ing `RIGHT OUTER` and `LEFT OUTER`
- There is no regex match (`~`) tilde operator. You can use `LIKE` instead.
- There is no `ANY` or `ALL` operator.

## Insert
```sql
INSERT INTO table (column1,column2 ,..) VALUES( value1, value2 ,...);
```

## Links
- [Litestream SQLite Replication](https://litestream.io/how-it-works/)

