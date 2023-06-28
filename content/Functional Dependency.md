---
aliases: [Functional Dependencies]
date created: Apr 27th, 2023
date modified: May 21st, 2023
---

## Goals
Our goals of database design with functional dependencies are: 
1. BCNF.
2. Losslessness.
3. Dependency preservation

## Definition:
find a = find b, $\alpha \to \beta$,  
In general, a functional dependency of the form α → β is trivial if β ⊆ α

### Trivial
if $\beta$ is a subset of $\alpha$

### 部分函数依赖
对子集函数依赖

## Closure
We shall use the notation $F^+$ to denote the **closure** of the set F, that is, the set of all functional dependencies that can be **inferred** given the set F. $F^+$ contains all of the functional dependencies in F.


## Links
- [[Normal Form]]
- [[Armstrong Axiom]]
- [[Canonical Cover]]
- [[Lossless Decomposition]]
- [[Extraneous]]
- [data structures - Find candidate keys given functional dependencies - Computer Science Stack Exchange](https://cs.stackexchange.com/questions/109975/find-candidate-keys-given-functional-dependencies)