---
aliases: [Functional Dependencies]
date created: Apr 27th, 2023
date modified: May 9th, 2023
---

# Functional Dependencies
> Functional dependency is a constraint that exists between two attributes in a database management system ([[DBMS]]) where one attribute determines another attribute.  
> There are mainly four types of functional dependencies in DBMS: multivalued, trivial, non-trivial, and transitive.  
> A non-trivial functional dependency occurs when **A->B** holds true where B is not a subset of A

$\alpha \to \beta$ for all pairs of tuples $t_{1}$ and $t_{2}$ in the instance such that they are the same.  
In general, a functional dependency of the form α → β is trivial if β ⊆ α

## Closure
We shall use the notation $F^+$ to denote the closure of the set F, that is, the set of all functional dependencies that can be inferred given the set F. $F^+$ contains all of the functional dependencies in F.

## Lossless Decomposition
if $R1 \cap R2$ forms a superkey for either R1 or R2, the decomposition of R is a lossless decomposition

## Links
- [[Normal Form]]

## Dependency Preserving

# Armstrong Axiom