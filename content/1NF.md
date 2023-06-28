## 1NF
1. **Atomic Values**: Every column of a table should contain only atomic values, which means that a value cannot be divided further
2. **No Repeating Groups**: A table should not contain repeating columns or groups of data

```sql
ID   Name   Courses
------------------
1    A      c1, c2
2    E      c3
3    M      C2, c3
```

This table is not in 1NF because the "Courses" column contains multi-valued attributes, which are not atomic.

```sql
ID   Name   Course
------------------
1    A       c1
1    A       c2
2    E       c3
3    M       c2
3    M       c3
```