---
aliases: []
tags: []
date created: Dec 3rd, 2022
date modified: Dec 11th, 2022
---
- 6 设 p 是奇素数,请证明 Z∗p 的所有生成元都是模 p 的二次非剩余。  
反证：假设生成元都是 QR，任取一个设为 g， 有 $g^{\frac{p-1}{2}} = 1$  
生成元阶要为 p-1，所以 g 不会是生成元，矛盾。所以都是 QNR

- 7 使用抽象代数的语言重新证明欧拉准则。  
定义 $\phi$ : $\phi(a) = a^{\frac{p-1}{2}}$ , $a \in Z_{p}^{*}$ , $gcd(a, p) = 1$  
For $a,b \in Z_{p}^{*}$ ， $\phi(ab) = a^{\frac{p-1}{2}}b^{\frac{p-1}{2}} = \phi(a)\phi(b)$ , 所以是群同态  
$\because a^{\frac{p-1}{2}} \pmod{p} = \pm1$ , a 有 1 和 -1, 所以是满同态  
因为勒让德符号 $\psi$ 也是满同态，所以若 $Ker \phi = Ker \psi$ 即得证
1. $Ker \phi \subset Ker \psi$  
对 $\psi(a) = 1$, $a^{\frac{p-1}{2}} = x^{p-1}= 1 \pmod{p}$ ,  
aka $\phi(a) = 1$  
得证

2. $Ker \psi \subset Ker \phi$  
对 $\phi(a) = 1$, $a^{\frac{p-1}{2}} = 1 \pmod{p}$  
$a = (a^\frac{p+1}{4})^2$  
$\psi(a) = 1$  
得证  
即 $Ker \phi = Ker \psi$ 