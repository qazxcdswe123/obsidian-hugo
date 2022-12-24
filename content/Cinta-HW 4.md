> 第六章：7、8、10、11
> 第七章：6、7、8
> 第八章：3、4、5

```tex
第六章习题的LaTex代码：

\item 设$\mathbb{G}$是群，对任意$n\in \N$, $i \in [0, n]$，$g_i \in \mathbb{G}$。证明$g_0 g_1 \cdots g_n$的逆元是$g_n^{-1} \cdots g_1^{-1} g_0^{-1}$。

\item 证明：任意群$\mathbb{G}$的两个子群的交集也是群$\mathbb{G}$的子群。

\item $\mathbb{G}$是阿贝尔群，$\mathbb{H}$和 $\mathbb{K}$是$\mathbb{G}$的子群。  
请证明$\mathbb{H} \mathbb{K} = \{hk: h \in \mathbb{H}, k \in \mathbb{K}\}$是群$\mathbb{G}$的子群。  
如果$\mathbb{G}$不是阿贝尔群，结论是否依然成立？

\item 设$\mathbb{G}$是阿贝尔群，$m$是任意整数，记$\mathbb{G}^m = \{ g^m: g\in \mathbb{G}\}$。请证明$\mathbb{G}^m$是$\mathbb{G}$的一个子群。

第7章习题LaTex代码：

\item 证明：如果群$\mathbb{G}$没有非平凡子群，则群$\mathbb{G}$是循环群。  
          
\item 证明推论\ref{cor:ord_div_n}，即循环群$\mathbb{G}$中任意元素的阶都整除群$\mathbb{G}$的阶。  
          
\item 编程完成以下工作：给定一个素数$p$，找出$\Z_p^*$的最小生成元。对于素数$1< p < 10000$，哪一个素数$p$使得$\Z_p^*$的最小生成元最大？

第8章习题LaTex代码：

 \item 如果$\mathbb{G}$是群，$\mathbb{H}$是群$\mathbb{G}$的子群，且$\lbrack \mathbb{G} : \mathbb{H}\rbrack =2$，请证明对任意的$g\in \mathbb{G}$，$g \mathbb{H} = \mathbb{H}g$。

 \item 设$\mathbb{G}$是阶为$pq$的群，其中$p$和$q$是素数。请证明$\mathbb{G}$的任意真子群是循环群。  
    
 \item 如果群$\mathbb{H}$是有限群$\mathbb{G}$的真子群，即存在$g\in \mathbb{G}$但是$g \not \in \mathbb{H}$。请证明$\vert \mathbb{H} \vert  \leq \vert \mathbb{G} \vert \ /2$。
```

## 6
- 7
$\because$ G 是群
$\therefore$ $g_{i}$ 逆元是 $g_{i}^{-1}$  (for $i \in [0,n]$)
$\therefore g_0 g_1 \cdots g_n$ x $g_n^{-1} \cdots g_1^{-1} g_0^{-1}$ = e
$\therefore$ $g_n^{-1} \cdots g_1^{-1} g_0^{-1}$ x $g_0 g_1 \cdots g_n$ = e
得证

- 8
设子集为 $G_{1}, G_{2}$
易得 e 在交集中
任取 $a \in G_{1}$, if $a \in G_{2}$, then $a^{-1}$  必然在交集中, else a and $a^{-1}$ 不在交集中
由于交集的元素均为子群的元素，所以满足结合律和封闭性
得证

- 10
易得 $e \in H$ and $e \in K$ => $e \in HK$
对任意元素 hk ，均有$h^{-1}k^{-1}$ 在群中，因为是阿贝尔群，所以 $k^{-1}h^{-1}$ 也在群中，所以有逆元。
因为 H，K 是 G 子群，所以封闭性，结合律满足	
所以 HK 是群
若不是阿贝尔群，则不满足逆元，不是群。

- 11
由定义得，$G^{m}$一定存在单位元 e
对群中任意元素 $g^{a}$，$g^{b}$ ，它们运算后是 $c = g^{a+b}$ 在群中，满足封闭性，由定义，$g^{-a}$ and $g^{-b}$ 也在群中，存在逆元
因为元素都在G中，所以也满足结合律
所以 $G^{m}$ 是群


## 7
- 6
由拉格朗日定理得，子群的阶必然整除群的阶，所以群的阶是质数，子群只能是 e 和自身
设 G 阶是 p， $\forall g \in G$ ，因为没有其他子群，所以 $|g| = p$
所以G是循环群

- 7
设 G 阶为 n
对任意 $h = g^{k}$, 由定理得，其阶为 $\frac{n}{gcd(n, k)}$
因此有限循环群G中任意元素的阶都整除群G的阶

或由[[Lagrange's theorem]]易得

- 8
最小生成元最大是31，是5881
- 2161 [23]
- 8761 [23]
- 5881 [31]

```python
import math


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_prime(number):
    """Returns True if number is a prime number"""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_min_generator(p):
    # Find the prime factors of p - 1
    factors = prime_factors(p - 1)
    # Initialize a list to store the generators
    generators = []
    # Iterate through the integers from 2 to p - 1
    for g in range(2, p):
        # Assume that g is a generator
        is_generator = True
        # Check if g is a generator
        for factor in factors:
            # If g^((p - 1) / factor) is equal to 1 mod p, then g is not a generator
            if pow(g, (p - 1) // factor, p) == 1:
                is_generator = False
                break
        # If g is a generator, add it to the list of generators
        if is_generator:
            generators.append(g)
    # Return the minimum generator
    return min(generators)


# Get all prime under 10000
prime_list = []
for i in range(3, 10000):
    if is_prime(i):
        prime_list.append(i)


dict_of_primitive_roots = {}


for p in prime_list:
    dict_of_primitive_roots[p] = find_min_generator(p)


dict_of_primitive_roots = dict(
    sorted(dict_of_primitive_roots.items(), key=lambda x: x[1]))
for key, value in dict_of_primitive_roots.items():
    print(key, value)
```

## 8
- 3
由于 index 为2，G 被分成了两个部分，H 和 G-H
1. When $g \in H$: 由群的性质得，gH = Hg = H
2. When $g \in (G-H)$: gH = Hg = (G-H) 因为被划分成两个部分，gH 不在 G 中就会在 G-H 中
得证

- 4
对任意G的真子群 H，有 $|G|/|H| = [G : H]$
由于 G 的阶为pq，所以 |H| = p or q
由7-6得，素数阶群是循环群

- 5
By definition, index >= 2
$\frac{|G|}{|H|} = [G : H] \geq 2$
$|H| \leq \frac{|G|}{2}$