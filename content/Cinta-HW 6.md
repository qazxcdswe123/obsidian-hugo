![](https://img.ynchen.me/2022/11/2c4f066e7be73f2fd464d4c74ef3dcc5.webp)

- 4
设对任意 $g \in G$，$gHg^{-1} \subset H$ ，有任意 $h \in H$ and $h' \in H$ that $ghg^{-1} \subset h'$ ,即 $gh \subset h'g$
即 $gH \subset Hg$, 同理可得 $Hg \subset gh$ 
即是正规子群。
得证子群

- 5
=>
$\phi(g_{1}g_{2}) = g_{1}g_{2}g_{1}g_{2} = \phi(g_{1})\phi(g_{2}) = g_{1}^{2} g_{2}^{2}$
$\therefore$ Abel

<=
$\phi(g_{1}g_{2}) = g_{1}g_{2}g_{1}g_{2} = g_{1}^{2} g_{2}^{2}= \phi(g_{1})\phi(g_{2})$
$\therefore$ [[Isomorphism]]

- 6
1. 设 g 是生成元，$\phi(g)$ 即 H 的生成元，因为对于 H 中每个元素 h = $\phi(g^{k})$ ，都有 $\phi(g^{k}) = \phi(g)^{k}$ ，即可由 $\phi(g)$ 生成 H 的所有元素，即为循环群。
2. $\phi(g_{1}g_{2}) = \phi(g_{1})\phi(g_{2}) = \phi(g_{2}g_{1}) = \phi(g_{2})\phi(g_{1})$ 既得 Abel

- 7
index 为 2，即 $[G:H] = 2$ , 即 G 只有两个子群 $H_{1}, H_{2}$，
假设 g 和 h 在同一个 H 中，显然成立
假设不在同一个 H 中, 设 $g \in H_{1}, h \in H_{2}$, $gh \notin H_{2}$ , $hg \notin H_{2}$
$\therefore$ $gh = hg = H_{1}$
得证