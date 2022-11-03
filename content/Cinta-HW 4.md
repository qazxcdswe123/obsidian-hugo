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


- 11


## 7
