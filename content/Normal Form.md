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

___

1NF：属性不可分割。

例如 关系模式：学生（姓名，住址），而住址又包含（区，街道），所以该模式不符合 1NF

2NF：不存在非主属性对候选码的部分依赖。

例如 已知候选码是 BC，非主属性是 D，函数依赖中除了 BC->D，还有 B->D 或者 C->D，该模式不符合 2NF

3NF：不存在非主属性对候选码的传递依赖。

例如 已知候选码是 AB，非主属性是 D，函数依赖中有 AB->C 和 C->D，所以该模式不符合 3NF

BCNF：不存在主属性对候选码的部分依赖和传递依赖。

1.检查 R 中元素的 [闭包](https://so.csdn.net/so/search?q=%E9%97%AD%E5%8C%85&spm=1001.2101.3001.7020)，也就是哪些元素或者元素组合可以根据 F 中函数依赖关系得到完整的 R，这些元素或者元素组合就是候选码。这里 AB 的闭包是 ABC，记作 (AB)+=ABC，所以 AB 是候选码。

2.通过候选码确定主属性和非主属性。这里 A，B 是主属性，剩下的 C 就是非主属性。

3.判断范式标准：1NF，2NF，3NF，BCNF，4NF

## 3NF 分解
1. 先求出 [[Canonical Cover]] Fc
2. 对于 Fc 里面的所有函数依赖 a->b,均转化为 Ri=ab
3. 对于所有的模式 Ri
	- 如果包含候选码，进行第 4
	- 如果都不包含候选码， 将任意一个候选码添加到模式 Ri 里面
4. 如果一个模式被另一个模式包含，则去掉此被包含的模式。

例子关系模式r(A,B,C,D,E,F),[函数依赖](https://so.csdn.net/so/search?q=%E5%87%BD%E6%95%B0%E4%BE%9D%E8%B5%96&spm=1001.2101.3001.7020)集F： A->BCD,BC->DE,B->D,D->A  
1.函数依赖是：A->BC.B->DE,D->A  
2.R1=ABC,R2=BDE,R3=DA,不包含候选码（AF,BF,DF）中任意一个，所以任意添加一个R4=AF  
3. 3NF分解为{ABC,BDE,DA,AF}

## BCNF 分解
1. 求出候选码
2. 观察函数依赖集，如果左边不是超码（候选码），则不满足条件
3. 用不满足条件的函数依赖（A->B）进行分解，这样分解之后就满足了
	- R1=AB（这样就满足了）
	- R2=（R-R1)∪A
	- F2={…}去掉 B 的所有函数依赖，尽可能写全
1. 对 F2 进行步骤 1 的计算。
2. 重复直到所有的满足条件

1. 只在左边的出现的节点一定存在于中候选键。（也就是候选键的一个一部分或者全部）  
2. 只在右边出现的节点一定不是候选键。（啥都不是，它只能被候选键推导出来 。是个铁废物）  
3. 两边都没有出现的节点，一点存在于候选键中。  
4. 在左边出现的节点（除了只在左边出现的节点，也就是它可能在右边也出现过）这样的节点呢？有待观察。

- [范式判断的三个步骤以及各个范式标准(1NF,2NF,3NF,BCNF,4NF)\_怎么判断是否为bcnf范式\_土豆面包的博客-CSDN博客](https://blog.csdn.net/qq_40177015/article/details/111590534)
- [3NF分解与BCNF分解\_WKP9418的博客-CSDN博客](https://blog.csdn.net/qq_43179428/article/details/105596526)