---
aliases: []
tags: []
date created: Mar 28th, 2022
date modified: Feb 5th, 2023
---
- Related: [[Relational Algebra]]

# Queries

## SELECT
Declare what data we are looking for  
Given a table of data. we need to **SELECT** columns to read  
- `SELECT column1, column2, FROM mytable;` `SELECT * FROM mytable;`
- `SELECT b_id-100, a_id FROM R WHERE a_id = 'a2';`
- `SELECT * FROM R JOIN S USING (a_id, b_id);`

### DISTINCT
Get distinct result

### JOIN
![image.png](https://img.ynchen.me/2023/01/50c81f83b5e2b89556a392c7e342f476.webp)

## WHERE
Add condition to **SELECT**  
`SELECT * FROM mytable WHERE condition AND/OR condition;`  

| Operator                        | SQL Example                                  |
| ------------------------------- | -------------------------------------------- |
| NOT IN (…)                      | col_name NOT IN (1, 3, 5)                    |
| IN (…)                          | col_name **IN** (2, 4, 6)                    |
| NOT BETWEEN … AND …             | col_name **NOT BETWEEN** 1 **AND** 10        |
| BETWEEN … AND …                 | col_name **BETWEEN** 1.5 **AND** 10.5        |
| cmp                             | col_name **!=** 4                            |
| LIKE (Case Sensetive Exact)     | col_name **LIKE** "ABC"                      |
| NOT LIKE (Case Sensetive Exact) | col_name **NOT LIKE** "ABCD"                 |
| % (With LIKE or NOT LIKE)       | col_name **LIKE** "%AT%"("ATTIC", "CAT", "BATS") |
| _ (With LIKE or NOT LIKE)       | col_name **LIKE** "AN_"("AND", but not "AN")     |

## Ordering Results
sort your results by a given column in ascending or descending order using the `ORDER BY` clause.  
`ORDER BY column ASC/DESC;`  
alpha-numerically based on the specified column's value.

### LIMIT and OFFSET
The `LIMIT` will reduce the number of rows to return, and the optional `OFFSET` will specify where to begin counting the number rows from.  
Using these clauses, the database can then execute queries faster and more efficiently by processing and returning only the requested content.

# Create

## Datatype
- INTERGER
- TEXT NOT NULL

## Grammar

# Misc
- `.schema`
- `.tables`

- [[Database]]
- [https://sqlbolt.com/](https://sqlbolt.com/)