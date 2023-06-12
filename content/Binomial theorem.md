---
aliases: [二项式定理]
date created: Mar 1st, 2022
date modified: Jun 11th, 2023
---
## Use [[Mathematical Induction]] to prove
1. $$(a+b)^n = a^n + \dbinom{n}{1}a^{n-1}b +  
\dbinom{n}{2}a^{n-2}b^2+\dots+\dbinom{n}{r}a^{n-r}b^r+\dots+ \dbinom{n}{n-1}ab^{n-1} + b^n$$  
	is trivially true for n = 1, 2  
2. Let k > 2 $$\begin{align*}  
&(a+b)^{k+1}\\  
&= (a+b)(a+b)^k\\  
&= (a+b)\Bigg(a^k + \dbinom{k}{1}a^{k-1}b + \dbinom{k}{2}a^{k-2}b^2+\dots  
  +\dbinom{k}{r}a^{k-r}b^r +\dots+ \dbinom{k}{k-1}ab^{k-1} + b^k \Bigg)\\  
&\begin{aligned}[t]  
&= a^{k+1} + \Bigg[1+\dbinom{k}{1}\Bigg]a^kb + \Bigg[\dbinom{k}{1}+\dbinom{k}{2}\Bigg]a^{k-1}b^2 + \dotsb\\  
&\dotsb + \Bigg[\dbinom{k}{r-1} + \dbinom{k}{r}\Bigg]a^{k-r + 1}b^r + \dotsb + \Bigg[\dbinom{k}{k-1} + 1\Bigg]ab^{k} + b^{k+1}.  
 \end{aligned}  
\end{align*}$$  
3. Use $\dbinom{n}{r-1} + \dbinom{n}{r} = \dbinom{n+1}{r}, \qquad\text{for}\quad 0 < r \leq n$  
4. QED.

## Links
- [Binomial theorem - Wikipedia](https://en.wikipedia.org/wiki/Binomial_theorem)  
- [Proof of the binomial theorem by mathematical induction](https://amsi.org.au/ESA_Senior_Years/SeniorTopic1/1c/1c_2content_6.html)
- [[Binomial Coefficient]]