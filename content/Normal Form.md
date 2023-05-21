---
aliases: []
date created: May 9th, 2023
date modified: May 21st, 2023
---

## BNCF
- Definition:
	- α → β is a trivial [[functional dependency]] (i.e., β ⊆ α).
	- **α is a superkey for schema R.**

### Decomposing schemas that are not in BCNF
- (α ∪ β) 
- (R − (β − α))
- In the case of in dep above, α = dept name, β = {building, budget}, and in_dep is replaced by
	- (α ∪ β) = (dept name, building,budget) 
	- (R − (β − α)) = (ID, name, dept name, salary)

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

## 2NF
1. The relation is in 1NF.
2. Every non-prime attribute of the relation is fully functionally dependent on the whole of every candidate key. In other words, there should be no partial dependencies
- non-prime attribute: not part of candidate key
- partial dependencies: non-prime attribute only depend on a part of a candidate key rather than the entire key

```sql
STUD_NO   COURSE_NO   COURSE_FEE
1         C1          1000
2         C2          1500
1         C4          2000
4         C3          1000
4         C1          1000
2         C5          2000
```

This table is in 1NF because it has no repeating groups or nested relations. However, the `COURSE_FEE` attribute is dependent on the `COURSE_NO` attribute, which is only a part of the primary key (`STUD_NO, COURSE_NO`). This violates the 2NF condition.
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

## 3NF
BCNF requires that all nontrivial dependencies be of the form α → β, where α is a superkey. Third normal form (3NF) relaxes this constraint slightly by allowing certain nontrivial functional dependencies whose **left side is not a superkey**

A relation schema R is in third normal form with respect to a set F of functional dependencies if, for all functional dependencies in F+ of the form α → β, where α ⊆ R and β ⊆ R, **at least one** of the following holds:

- α → β is a trivial functional dependency.
- α is a superkey for R.
- **Each attribute A in β − α is contained in a candidate key for R.**

## 4NF
A relation is said to be in 4NF if it is in Boyce Codd Normal Form (BCNF) and has no multi-valued dependency

- example:
R(A,B,C,D) has A →> B and A →> C, then R should be decomposed into R1(A,B) and R2(A,C,D) to eliminate the multivalued dependency