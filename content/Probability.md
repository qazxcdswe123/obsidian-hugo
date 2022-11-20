---
aliases: [概率论]
tags: []
date created: Sep 1st, 2022
date modified: Nov 16th, 2022
---

## Total Probability
$P\left( A\right) =P\left( B_{1}\right) P\left( A| B_{1}\right) +\ldots +P\left( B_{n}\right) P\left( A| B_{n}\right)$  
$S=B_{1}\cup \ldots \cup B_{n}$  
$B_{1}\cup \ldots \cup B_{n}$ 为划分  
=>  
$P\left( A\right) =P\left( AS\right) =P\left( A\cap \left( B_{1}\cup \ldots \cup B_{n}\right) \right)$

## 概率密度
![](https://img.ynchen.me/2022/10/3b3fdcccba4b038c99056c908130e7dc.webp)

变量大写表示变量本身，变量小写表示取值  
函数小写表示概率密度（概率的取值），大写表示分布函数（概率的累加）
___
- [[N 维随机变量概率]]
- [[Bayes Theorem]]
- [[Series]]
- [[Expectation]]  
- [[Normal Distribution]]
- 方差：D(X) = Var(X) = $E{[X - E(x)]^{2}}$ = $E(X^{2})- E^{2}(X)$ 
- 协方差/标准差：$\sqrt{D(X)}$  
- 相关系数：正态分布，泊松分布

___
[[Python Numpy Random]]