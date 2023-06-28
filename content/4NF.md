## 4NF
A relation is said to be in 4NF if it is in Boyce Codd [[Normal Form]] ([[BCNF]]) and has no multi-valued dependency

- example:  
R(A,B,C,D) has A →> B and A →> C, then R should be decomposed into R1(A,B) and R2(A,C,D) to eliminate the multivalued dependency

