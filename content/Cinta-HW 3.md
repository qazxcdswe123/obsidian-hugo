---
aliases: []
tags: []
date created: Oct 5th, 2022
date modified: Oct 5th, 2022
---
![](https://img.ynchen.me/2022/10/fd35f759d7fa5fce50de074918633e1e.webp)

1. Since 23 is a prime and $2019 = 22 * 91 + 17$, we have $3^{2019} \pmod {23} \equiv 3^{17} \pmod {23}$  
Calculate the multiplication inverse(which is 8), we then have $3^{17} *3^{5} *8^{5} \pmod {23} \equiv 8^{5} \pmod {23} \equiv 16$

2. Since 17 is a prime, and $50 = 3 * 16 + 2$, we have $x^{2} \equiv 2 \pmod {17}$, then $17 | x^{2} - 2$, $x = 6$

5. To show $13 | 2^{70} + 3^{70}$, we can calculate $2^{70} \pmod {13}$ and $3^{70} \pmod {13}$ first.  
$2^{70} \equiv 2^{5 * 12 + 10} \equiv 2^{10} \equiv 10 \pmod {13}$  
$3^{70} \equiv 3^{5 * 12 + 10} \equiv 3^{10} \equiv 3 \pmod {13}$  
So $13 | 2^{70} + 3^{70}$

6. $\phi(55) = 40$  
$gcd(2, 55) = 1$  
$2^{100000} \equiv 2^{\phi(55) * 2500} \equiv 1 \pmod {55}$

8. Same as $7^{1000} \pmod {100}$  
$gcd(7, 100) = 1$,  
$\phi(100) = 40$  
$7^{1000} \equiv 7^{\phi(100) * 25} \equiv 1 \pmod {100}$  
So last two digit are 0 and 1

9. Code

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def euler_phi(n):
    result = n
    for i in range(2, n + 1):
        if gcd(i, n) != 1:
            result -= 1
    return result


def print_phi_table(n):
    for i in range(1, n + 1):
        print(i, euler_phi(i))
```

10. $(p - 1)! \pmod p = -1$  
For $\forall x \in [1, p-1]$, since $gcd(x, p) = 1$ , there is always one and only one(proofed in [[Cinta-HW 2]]) $x^{-1}$ that satisfy $x * x^{-1} \equiv 1 \pmod p$
- When p is 2 and 3, it is trivially true
- When $p > 3$  
We can guarantee $x^{2} = 1$ iff $x = \pm1$, so we can find a match for every element from p-2 to 2.
Now we have $\prod_{i = 2}^{p - 2} i \equiv 1$, as a result,
$1 * \prod_{i = 2}^{p - 2} i * (p-1) \equiv -1 \pmod p$
