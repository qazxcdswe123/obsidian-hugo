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

## Lossless Decomposition
if $R1 \cap R2$ forms a superkey for either R1 or R2, the decomposition of R is a lossless decomposition
关系模式R(U)的分解r={R1，R2}，则r是一个无损连接分解的充要条件是 R1∩R2->R1-R2（或R1∩R2->R2-R1）成立

## Extraneous
- Removal from the left side: Attribute A is extraneous in α if A ∈ α and F logically implies (F − {α → β}) ∪ {(α − A) → β}.
- Removal from the right side: Attribute A is extraneous in β if A ∈ β and the set of functional dependencies (F − {α → β}) ∪ {α → (β − A)} logically implies F.

## Links
- [[Normal Form]]
- [[Armstrong Axiom]]
- [[Canonical Cover]]
- [data structures - Find candidate keys given functional dependencies - Computer Science Stack Exchange](https://cs.stackexchange.com/questions/109975/find-candidate-keys-given-functional-dependencies)