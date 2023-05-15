## Relational Model
- A relation's **primary key** uniquely identifies a single tuple.
- A **foreign key** specifies that an attribute from one relation has to map to a tuple in another relation.
- A **candidate key** is a minimal [superkey](https://en.wikipedia.org/wiki/Superkey "Superkey").
- A **super key** is a set of one or more attributes (columns) that can uniquely identify a row in a table
	- $t_{1} \neq t_{2}$ then $t_{1}[K] \neq t_{2}[K]$
	- `t` for tuple and `K` for key

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

## Links
- [[Functional Dependency]]