## What
A way to represent a periodic function as the sum of simple sine and cosine waves.
These sine and cosine functions, also known as harmonics, have frequencies that are integer multiples of a fundamental frequency.

## How
Let's denote the function we want to represent as $f(x)$ and the Fourier series as $F(x)$. If the function $f(x)$ is periodic and integrable over the interval $[-L, L]$, then the Fourier series representation of $f(x)$ is given by:

$$F(x) = a_0 + \displaystyle\sum_{n=1}^{\infty}[a_n\cos(\frac{n\pi x}{L}) + b_n\sin(\frac{n\pi x}{L})]$$
where: 
- $a_0 = \frac{1}{2L} \int_{-L}^{L} f(x) dx$,
- $a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos(\frac{n\pi x}{L}) dx$,
- $b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin(\frac{n\pi x}{L}) dx$.

## Links
- [[Series]]