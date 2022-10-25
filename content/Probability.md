---
aliases: []
tags: []
date created: Sep 1st, 2022
date modified: Oct 24th, 2022
---
## Total Probability
$P\left( A\right) =P\left( B_{1}\right) P\left( A| B_{1}\right) +\ldots +P\left( B_{n}\right) P\left( A| B_{n}\right)$  
$S=B_{1}\cup \ldots \cup B_{n}$  
$B_{1}\cup \ldots \cup B_{n}$   为划分
=>
$P\left( A\right) =P\left( AS\right) =P\left( A\cap \left( B_{1}\cup \ldots \cup B_{n}\right) \right)$

## Independent
独立与互斥无关
条件：$P\left( AB\right) =P\left( A\right) P\left( B\right)$ or $P\left( \overline{A}\overline{B}\right) =P\left( \overline{A}\right) P\left( \overline{B}\right)$

## 概率密度
![](https://img.ynchen.me/2022/10/3b3fdcccba4b038c99056c908130e7dc.webp)

## N 维随机变量
$P\{x_{1} < X \leq x_{2}, y_{1} < Y \leq y_{2}\} =  F(x2,y2)-F(x2,y1)-F(x1,y2)+F(x1,y1)$ 
连续型：求二重积分
离散型：两次求和
![](https://img.ynchen.me/2022/10/94cf83b310b1cf75235f5f80a5f5d52f.webp)

### 边缘分布函数
- $F_{X}(x), F_{Y}(y)$ 为二维随机变量 (X,Y) 关于 X 和 Y 的边缘分布函数.
___

[[Bayes Theorem]]