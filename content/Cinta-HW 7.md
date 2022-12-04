[[Chinese Remainder Theorem|CRT]]
![](https://img.ynchen.me/2022/11/2452a08f00e6deac1ed5cf3054a5ff57.webp)

![](https://img.ynchen.me/2022/12/1db38e80a42a7750bab0abe0ed0fafe1.webp)

- 1
a = 8, b = 3, p = 11, q = 19 p^-1 = 7, q^-1 = 7
x = 8x19x7 + 3x11x7 mod 209
x = 41

- 2
a1 = 1, a2 = 2, a3= 3, a4 = 4, M = 3465
b1  = 693, b2 = 495, b3 =385 , b4 = 315
对应逆记为: 416, 283, 214, 88
x = 1x693x416 + 2x495x283 + 3x385x214 + 4x315x88 mod 3465 = 1731

- 3
221 = 13x17
$Z_{221}^{*} \cong Z_{13}^{*} \times Z_{17}^{*}$
$2000 \leftrightarrow (11, 11)^{2019} = ([11^{2019} \pmod{13}], [11^{2019} \pmod{17}]) = (5, 5) = 5$
- 9
$K = ker\phi = \{0\}$
定义 $\psi$ : $Z_{n} \to Z_{n}/K$ ，显然为标准同态，由第一同构定理，存在唯一同构映射 $\upeta$ : $Z_{n}/k \to \phi(Z_n)$, 且 $\phi = \upeta\psi$
因为后两个均为单射，所以$\phi$ 也为单射
de zheng

- 10
即证明双射和群操作
定义 $Z^{*}_{n} \to Z^{*}_{p} \times Z^{*}_{q}$ 为 $\phi$
$$\phi(x) = ([x \pmod{p}], [x \pmod{q}])$$
证明映射 φ 是一种双射,即证明 φ 是满射且单射。
满射：根据中国剩余定理，任意序对中的两个同余式在模 n 下有k唯一解。
单射：任取正整数a , b < n ，设$\phi(a) = \phi(b)$ ，由 CRT :a = b，为单射
群操作：![](https://img.ynchen.me/2022/12/eeaf911de2e8cd9bc04396bd65d8e73c.webp)
得证