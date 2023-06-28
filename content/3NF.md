## 3NF
[[BCNF]] requires that all nontrivial dependencies be of the form α → β, where α is a superkey.  
3NF relaxes this constraint slightly by allowing certain nontrivial [[Functional Dependency|functional dependencies]] whose **left side is not a superkey**

- Definition
	- It first need to be in [[2NF]].
	- For all functional dependencies in F+ of the form α → β, **at least one** of the following holds:
		- α → β is a trivial functional dependency.
		- α is a superkey for R.
		- **Each attribute A in β − α is *contained* in a candidate key for R.** (Or , it should only depend on superkey)

![image.png](https://img.ynchen.me/2023/06/0c6a769928ccb2fa6da710b775379662.webp)

- 3NF eliminate transitive dependency because if a non-prime attribute A depend on non-prime attribute B, since B depends on K it leads to (k -> B -> A)
- To check if a relation is 3NF, check every non-prime attribute and see if it only rely on superkey. If a non-prime attribute does not depend on superkey then it's not 3NF.

## 3NF 分解
1. 先求出 [[Canonical Cover]] Fc
2. 对于 Fc 里面的所有函数依赖 a->b,均转化为 Ri=ab
3. 对于所有的模式 Ri
	- 如果包含候选码，进行第 4
	- 如果都不包含候选码， 将任意一个候选码添加到模式 Ri 里面
4. 如果一个模式被另一个模式包含，则去掉此被包含的模式。

例子关系模式 r(A,B,C,D,E,F),[函数依赖](https://so.csdn.net/so/search?q=%E5%87%BD%E6%95%B0%E4%BE%9D%E8%B5%96&spm=1001.2101.3001.7020) 集 F： A->BCD,BC->DE,B->D,D->A  
1. 函数依赖是：A->BC.B->DE,D->A  
2. R1=ABC,R2=BDE,R3=DA,不包含候选码（AF,BF,DF）中任意一个，所以任意添加一个 R4=AF  
3. 3NF 分解为{ABC,BDE,DA,AF}

## 2NF VS 3NF
1. [[2NF]] is concerned with eliminating partial dependencies. This means that if a table has a composite primary key (consisting of multiple columns), no column should be dependent on just a part of the primary key. Every non-key attribute should be fully functionally dependent on the whole primary key.
2. 3NF goes a step further by eliminating transitive dependencies. This means that no non-key attribute should depend on another non-key attribute. Each non-key attribute must be directly dependent on the primary key and only on the primary key.

