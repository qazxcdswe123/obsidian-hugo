---
aliases: []
date created: Jun 27th, 2023
date modified: Jun 27th, 2023
---

## BCNF
- Definition:
	- α → β is a trivial [[functional dependency]] (i.e., β ⊆ α).
	- **α is a superkey for schema R.** ([[3NF]] Implied)

To test BCNF, check every non-trivial FD to see if the left side is a superkey.

### Decomposing schemas that are not in BCNF
- (α ∪ β) 
- (R − (β − α))
- In the case of in dep above, α = dept name, β = {building, budget}, and in_dep is replaced by
	- (α ∪ β) = (dept name, building,budget) 
	- (R − (β − α)) = (ID, name, dept name, salary)
 

## BCNF 分解
1. 求出候选码
2. 观察函数依赖集，如果左边不是超码（候选码），则不满足条件
3. 用不满足条件的函数依赖（A->B）进行分解，这样分解之后就满足了
	- R1=AB（这样就满足了）
	- R2=（R-R1)∪A
	- F2={…}去掉 B 的所有函数依赖，尽可能写全
4. 对 F2 进行步骤 1 的计算。
5. 重复直到所有的满足条件

6. 只在左边的出现的节点一定存在于中候选键。（也就是候选键的一个一部分或者全部）  
7. 只在右边出现的节点一定不是候选键。（啥都不是，它只能被候选键推导出来 。是个铁废物）  
8. 两边都没有出现的节点，一点存在于候选键中。  
9. 在左边出现的节点（除了只在左边出现的节点，也就是它可能在右边也出现过）这样的节点呢？有待观察。
