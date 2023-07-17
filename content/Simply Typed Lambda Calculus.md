---
aliases: [STLC]
date created: Jul 1st, 2023
date modified: Jul 3rd, 2023
---

## Judgement
- Premise
- Conclusion  
$$\frac{\text{Premise}_{1} ~ \text{Premise}_{2}..n}{\text{Conclusion}} (\text{Name})$$

## Context
$$\Gamma ~ \text{ctx}$$

## Term
$$\Gamma \vdash M : A$$  
$M$ is the term under context $\Gamma$ with type $A$  
M 是语境 $\Gamma$ 下类型为 A 的项

## Reduction
- Beta rule
$$
\frac{x: A \vdash M: B \quad N: A}{(\lambda x . M) N \equiv M[x \mapsto N]: B} \beta \text { rule }
$$

## Typing Rules

## Links
- [Alonzo Church - Wikipedia](https://en.wikipedia.org/wiki/Alonzo_Church)
- [Haskell Curry - Wikipedia](https://en.wikipedia.org/wiki/Haskell_Curry)
- [Curry–Howard correspondence - Wikipedia](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
- [[Lambda and Anonymous Function]]