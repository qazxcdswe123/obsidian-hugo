---
aliases: [二项式系数]
date created: Mar 1st, 2022
date modified: Aug 5th, 2022
---
[https://kconrad.math.uconn.edu/blurbs/proofs/binomcoeffintegral.pdf](https://kconrad.math.uconn.edu/blurbs/proofs/binomcoeffintegral.pdf)

写作 $\dbinom{n}{k}$，定义为 ${\displaystyle (1+x)^{n}}$的多项式展开式中，${\displaystyle x^{k}}$ 项的系数，因此一定是非负整数。  (n > k)
定义：$$\dbinom{n}{k} = \frac{n!} {(n-k)! \times k!}$$
理解：从 n 个里面选，k 个为一组，剩下为一组，内部排列


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