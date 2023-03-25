---
aliases: []
tags: []
date created: Feb 14th, 2023
date modified: Feb 14th, 2023
---
![image.png](https://img.ynchen.me/2023/02/3e7113fe716e6f0f05c942a9eee35b87.webp)

## Cross Join
Essentially a [[Cross Product]]

```sql
SELECT ∗
FROM courses, enrollment; 
```

## Inner Join
```sql
SELECT column_name(s) 
FROM tablel
INNER JOIN table2
ON table1_column_name = table2_column_name; 
```

The `table1_column.name` = `table2_column.name` is the join condition.  
**The default `JOIN` Method**

## Left Join

## Full Join
The full outer join which guarantees that all rows from each table will appear in the output.

## Natural Join
When the same column name match, the join the table

# Join Algorithm

## Grace Hash Join
Grace hash join is a type of hash join algorithm used in database systems to join two large tables that cannot fit in memory.