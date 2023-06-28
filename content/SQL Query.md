---
aliases: []
date created: Mar 28th, 2022
date modified: Jun 27th, 2023
---
- Related: [[Relational Algebra]]

## Queries
![image.png](https://img.ynchen.me/2023/02/f8db563c163b8aab459bc511c71a40a2.webp)

```sql
SELECT [DISTINCT] <column expression list>  
FROM <single table>  
[WHERE <predicate>]  
[GROUP BY <column list>  
[HAVING <predicate>] ]  
[ORDER BY <column list>]  
[LIMIT <integer>];
```

- [[SQL SELECT]]
- [[SQL WHERE]]
- [[SQL ORDER BY]]
- [[SQL GROUP BY]]

### Aggregate
- `AVG()`
- `COUNT()`
- `SUM()`

## Misc
- `.schema`
- `.tables`
- SQL Null
	- represents an “unknown” or “missing” value.
	- If you do any calculation with NULL, you’ll just get NULL. For instance if x is NULL, then x > 3, 1 = x, and x + 4 all evaluate to NULL. Even x = NULL would evaluate to NULL
	- if you want to check whether x is `NULL`, then write `x IS NULL` or `x IS NOT NULL` instead.
	- when the comparison involves `NULL` values. `UNKNOWN`
	- NULL is **falsey**, meaning that `WHERE NULL` is just like `WHERE FALSE`. The row in question does not get included.
	 - `NULL` column values are ignored by aggregate functions.
  - SQL Set
	  - `UNION`
	  - `INTERSECT`
	  - `EXCEPT`
	  - `<ALL>`: All possible value. (Allow Duplicates, Optional)
- [[SQL View]]
- [[SQL Common Table Expression]]
- [[SQL Testing]]
- [[Query Optimization]]