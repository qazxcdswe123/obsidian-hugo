1. The relation is in [[1NF]].
2. Every non-key attribute of the relation is fully functionally dependent on the whole of every candidate key. In other words, there should be no partial dependencies
- non-key attribute: not part of candidate key
- partial dependencies: non-key attribute only depend on a part of a candidate key rather than the entire key

To check is a relation is 2NF, check every non-prime attribute and see if it depend on **part of the** candidate key

- [[3NF]]
## Example

```sql
STUD_NO   COURSE_NO   COURSE_FEE
1         C1          1000
2         C2          1500
1         C4          2000
4         C3          1000
4         C1          1000
2         C5          2000
```

This table is in [[1NF]] because it has no repeating groups or nested relations. However, the `COURSE_FEE` attribute is dependent on the `COURSE_NO` attribute, which is only a part of the primary key (`STUD_NO, COURSE_NO`). This violates the 2NF condition.  
To get a 2NF: eliminate the partial dependencies

```sql
Table 1: Student_Course
STUD_NO   COURSE_NO
1         C1
2         C2
1         C4
4         C3
4         C1
2         C5

Table 2: Course_Fee
COURSE_NO   COURSE_FEE
C1          1000
C2          1500
C4          2000
C3          1000
C5          2000
```
