## SQL WHERE
Add condition to **SELECT**, use boolean algebra.  
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