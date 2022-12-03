---
aliases: []
tags: []
date created: Aug 5th, 2022
date modified: Nov 23rd, 2022
---
[Modular arithmetic - Wikipedia](https://en.wikipedia.org/wiki/Modular_arithmetic)

## Congruence
[Congruence modulo (article) | Cryptography | Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo)  
$A \equiv B \pmod{C}$
1. $\equiv$ is the symbol for congruence, which means the values **A** and **B** are in the same **equivalence class**.
2. (mod C) tells us what operation we applied to **A** and **B**.
3. when we have both of these, we call $\equiv$ **congruence modulo C**.

We say that r is congruent to s modulo n, or r is congruent to s mod n, if r − s is evenly divisible by n;

### From Set
[[Set Theorem]]

## Modular Power
[[Complexity]]: $O(log(y))$ for $x^y$  
Use [[Divide and Conquer]] Algorithm, $x^{y}=(x^{\lfloor{y/2}\rfloor})^{2}$, like fast multiply algorithm.
