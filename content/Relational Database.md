---
aliases: []
date created: Jan 29th, 2023
date modified: May 21st, 2023
---

## Relational Model
- A relation's **primary key** uniquely identifies a single tuple.
- A **foreign key** specifies that an attribute from one relation has to map to a tuple in another relation.
- A **candidate key** is a minimal [superkey](https://en.wikipedia.org/wiki/Superkey "Superkey").
- A **super key** is a set of one or more attributes (columns) that can uniquely identify a row in a table
	- $t_{1} \neq t_{2}$ then $t_{1}[K] \neq t_{2}[K]$
	- `t` for tuple and `K` for key

### [[Functional Dependency]]
- Superkey：设 K 为 R< U , F >的属性或属性组，若 K->U，则称 K 为 R 的超码
- Candidate key：设 K 为 R< U , F >的超码，若 K-> when f U，则称 K 为 R 的候选码
- Primary key：若 R(U , F) 有多个候选码，则可以从中选定一个作为 R 的主码

## Relational Databases
- In SQL, we choose the types of data that each column will store.
- check the schema, or design, of our new table with `.schema`
- SQL supports many functions that we can use to count and summarize data:
	- `AVG`
	- `COUNT`
	- `DISTINCT`
	- `LOWER`
	- `MAX`
	- `MIN`
	- `UPPER`
- Since each show may have more than one genre, we can have more than one row per show in our genres table, known as a **one-to-many** relationship.

- Example
	- [[Mysql]]
	- [[Sqlite]]

- database consistency constraints:
	- primary-key constraints
	- functional dependencies
	- check constraints
	- assertions
	- triggers

## Links
- [[Functional Dependency]]