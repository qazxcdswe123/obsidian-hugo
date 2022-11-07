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
这个有些奇怪。。

```python
def prime_factors_list(number):
    """Returns a list of prime factors of a number"""
    prime_factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            prime_factors.append(i)
            number /= i
    return prime_factors


def gcd(a, b):
    """Returns the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def is_prime(number):
    """Returns True if number is a prime number"""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def is_primitive_root(number, prime):
    """Returns True if number is a primitive root of the prime factors"""
    prime_factors = prime_factors_list(prime - 1)
    for factor in prime_factors:
        if pow(number, (prime - 1) // factor, prime) == 1:
            return False
    return True
```

## 8
- 3
由于 index 为2，G 被分成了两个部分，由于 Hg 不在 gH内，所以两部分为 gH 和 Hg
gH 会被射到 gH 之外，即 Hg
即 gH = Hg

- 4
对任意G的真子群 H，有 $|G|/|H| = [G : H]$
由于 G 的阶为pq，所以 |H| = p or q
由7-6得，素数阶群是循环群

- 5
By definition, index >= 2
$\frac{|G|}{|H|} = [G : H] \geq 2$
$|H| \leq \frac{|G|}{2}$