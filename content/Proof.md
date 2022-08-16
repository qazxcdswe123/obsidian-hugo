---
aliases: [证明]
tags: [] 
date created: Mar 28th, 2022
date modified: Aug 16th, 2022
---
## Term
### Axiom
> In studying abstract mathematics, we take what is called an axiomatic approach; that is, we take a collection of objects S and assume some rules about their structure. These rules are called axioms.

### Proposition
> If we can prove a statement true, then that statement is called a proposition.

### Theorem
> A proposition of major importance is called a theorem

### Lemmas
> Sometimes instead of proving a theorem or proposition all at once, we break the proof down into modules; that is, we prove several supporting propositions, which are called lemmas, and use the results of these propositions to prove the main result.

### Corollaries
> If we can prove a proposition or a theorem, we will often, with very little effort, be able to derive other related propositions called corollaries

## General Method
Suppose you wish to show that an object **exists** and is **unique**. First show that there actually is such an object. To show that it is unique, assume that there are two such objects, say r and s, and then show that r = s.  

We use examples to give insight into existing theorems and to foster intuitions as to what new theorems might be true. Applications, examples, and proofs are tightly interconnected—much more so than they may seem at first appearance.


## Proving an Implication
1. Method 1 正向证明
	1. Assume P
	2. Show Q logically with P

2. Method 2 证明逆否命题
	1. Write, “We prove the **contrapositive**:” and then state the contrapositive.
	2. Proceed as in Method 1
	3. ![](https://s2.loli.net/2022/03/28/x6RUnPLKTEsyXl4.png)


## Proving an “If and Only If”
1. Method 1 证明两个语句相互蕴涵
	1. 证明 P 蕴含 Q
	2. 证明 Q 蕴含 P

2. Method 2 构建逻辑链
	1. 证明 P 等价于第二个语句，
	2. 然后第二个语句等价于第三个语句，
	3. 以此类推，直到等价于 Q。
	4. ![](https://s2.loli.net/2022/03/28/IYwDVHkvyhzAS51.png)

- Proof by case 分类讨论
- Proof by contradiction 反证法
	1. 写 假设 P 是假的。
	2. 推导得出错误，逻辑矛盾
	3. 写“得出矛盾。因此，P 一定是真的。
	4. ![](https://s2.loli.net/2022/03/28/7c6Q8CvxXKu9woz.png)
