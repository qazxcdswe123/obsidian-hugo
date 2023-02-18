## SQL ORDER BY
- `ORDER BY column ASC/DESC;`  
Sort your results by a given column in ascending or descending order using the `ORDER BY` clause, `ASC` by default.  
We first sort on the first column listed, and then break any ties with the second column listed, and then break any remaining ties with the third column listed, and so on.  
alpha-numerically based on the specified column's value.

### LIMIT and OFFSET
`Limit` typically used with `order by`.  
The `LIMIT` will reduce the number of rows to return, and the optional `OFFSET` will specify where to begin counting the number rows from.  
Using these clauses, the database can then execute queries faster and more efficiently by processing and returning only the requested content.