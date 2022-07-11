For $a,b \geq 1$ and equation $T(n) = aT(n/b) + f(n)$
1. If $f(n) = O(n^ {\log_b {a} -\epsilon })$ , then $T(n) = \Theta(n^{\log_b a})$ for constant $\epsilon > 0$
2. If $f(n) = \Theta(n^{log_b a})$ , then $T(n) = \Theta(n^{\log_b a} \lg n)$
3. If $f(n) = \Omega(n^{\log_b a +\epsilon} )$ for constant $\epsilon > 0$ , and $af(n/b) \leq cf(n)$ for some constant $c < 1$  and large $n$ , then the answer is $T(n)  = \Theta(f(n))$

Limitation:
1. In the first case, $f(n)$ must be Polynomially Smaller 多项式小于 than $n^{log_b a}$
2. In the third case, $f(n)$ must be Polynomially larger 多项式大于 than $n^{log_b a}$
3. $f(n)$ may be smaller than $n^{log_b a}$ but not polynomially smaller.