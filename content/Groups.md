---
aliases: []
tags: []
date created: Oct 24th, 2022
date modified: Nov 17th, 2022
---

## 判定
1. 封闭性
2. 结合律
3. 存在单位元 `e`
4. 对任意元素存在逆元

## Properties
- Let G be a group and a and b be any two elements in G. Then the equations $ax = b$ and $xa = b$ have unique solutions in G.
- There is a unique `e` (identity element) => $e \cdot a = a \cdot e = a$ , its order is 1, the inverses in a group are also unique
- The right and left cancellation laws are true in groups

## Definition
[Group theory - Wikiwand](https://www.wikiwand.com/en/Group_theory)  
In mathematics, a group is a set and an operation that combines any two elements of the set to produce a third element of the set, in such a way that the operation is associative, an identity element exists and every element has an inverse.

- abelian or commutative  
A group G with the property that a ◦ b = b ◦ a for all a, b ∈ G is called abelian or commutative.

- the general linear group  
The set of invertible matrices forms a group called the general linear group.

- Order  
	- The order of a finite group is the number of elements it contains. 
	- The order of a element $g \in G$ is the minimum positive number $m$ such that $g^{m} = e$, $ord(g) = m$. If there is no such number, then $g$ has infinite order.

## Notation
If the group is $\mathbb{Z}$ or $\mathbb{Z}_n$ , we write the group operation additively and the exponential operation multiplicatively; that is, we write $ng$ instead of $g^n$.

Groups are essentially a [[Set Theorem|Set]]

[[Subgroups]]

___

[[Discrete Math]]-[[Algebra]]
- 半群：符合二元运算且可结合
	- 设 V = ⟨S, ◦⟩ 是代数系统，◦ 为二元运算，如果 ◦ 是可结合的，则称 V 为半群;
- 幺半群或独异点：有单位元的半群
	- 设 V = ⟨S,◦⟩是半群，如果 e ∈ S 是关于◦运算的单位元，则称 V 是幺半群或独异点。有时也将独异点记 为 V = ⟨S,◦,e⟩;
- 群：有单位元，可结合，有逆元
- 