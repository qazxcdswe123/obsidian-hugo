---
aliases: [CRT]
tags: [] 
date created: Nov 21st, 2022
date modified: Nov 21st, 2022
---
## 数论视角
设 p 和 q 是互素的两个正整数, n = pq。对任意的 a ∈ Zp和 b ∈ Zq,存在唯一解x,0 ≤ x < n 使得: 
- x ≡a (mod p) 
- x ≡b (mod q)
且 $x = aqq^{-1} + bpp^{-1} \pmod{n}$

推广：有 n 个互素的模数 $m_{0} \cdots m_{n-1}$, 解为 $x = \Sigma_{i=0}^{n-1} ab_{i}b_{i}^{-1} \pmod{M}$
Where $b = \frac{M}{m}$, $M = \prod_{i=0}^{n-1} m_{i}$

## 代数视角
$n = pq$, p and q coprime, $\mathbb{Z_{n}} \cong \mathbb{Z_{p}} \times \mathbb{Z_{q}}$ and $\mathbb{Z_{n}^*} \cong \mathbb{Z_{p}^*} \times \mathbb{Z_{q}^*}$

![](https://img.ynchen.me/2022/11/402c5561bd3d7bd5697314176c30bec7.webp)
