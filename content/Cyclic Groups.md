---
aliases: [循环群]
date created: Oct 24th, 2022
date modified: Jul 2nd, 2023
---

$S=\{g, g^ {2} ,\cdots ,  g^ {i} ,  \cdots \}$  
[[Set Theory|Set]] $<g> = \{g^{k}: k\in Z\}$ is a subgroup of G, `<g>` is a subgroup, `g` is the [[generator]]

## Properties
- 任取正整数 n, 设 `G = <g>` 是阶为 n 的循环群,则 $g^k= e$ 当且仅当 n 整除 k。
- 设群 `G = <g>` 是阶为 n 的循环群。 如果 $h = g^k$, 则 h 的阶为 n/d, 其中 d = gcd(k, n)。
	- 设群 G = `<g>` 是阶为 n 的循环群,则群 G 中恰有 φ(n) 个生成元。
	- 设群 G = `<g>` 是阶为 p 的循环群,p 是素数,则 G 中的元素除了 e 之外都是生成元。
- 循环群 $G = <g>$ 的每一个子群都是循环群。
- 所有的循环群都是阿贝尔群。

> 已知 2 是群 Z∗11 的生成元, 群 Z∗11 的阶是 10, 2^**3**= **8**, 且 gcd(**3**, 10) = 1, 所以 8 的阶是 10, 即 8 也是一个 [[Generator|生成元]]。 5 不是 [[Generator|生成元]], 因为 5 = 2^**4** mod 11, gcd(**4**, 10) = 2。  
> $g^{k}$ 的阶是 $\frac{n}{gcd(n, k)}$  
> 这告诉我们,在知道某个元是生成元时,如何找到另一个生成元