## BNCF
- α → β is a trivial [[functional dependency]] (i.e., β ⊆ α).
- α is a superkey for schema R.

### Decomposing schemas that are not in BCNF
- (α ∪ β) 
- (R − (β − α))
- In the case of in dep above, α = dept name, β = {building, budget}, and in_dep is replaced by
	- (α ∪ β) = (dept name, building,budget) 
	- (R − (β − α)) = (ID, name, dept name, salary)

## 3NF
BCNF requires that all nontrivial dependencies be of the form α → β, where α is a superkey. Third normal form (3NF) relaxes this constraint slightly by allowing certain nontrivial functional dependencies whose **left side is not a superkey**

A relation schema R is in third normal form with respect to a set F of functional dependencies if, for all functional dependencies in F+of the form α → β, where α ⊆ R and β ⊆ R, at least one of the following holds:

- α → β is a trivial functional dependency.
- α is a superkey for R.
- Each attribute A in β − α is contained in a candidate key for R.