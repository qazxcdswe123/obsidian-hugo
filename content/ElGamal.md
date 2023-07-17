## What
1. Alice has a secret key $x$ and a public key $X = g^{x}, g, p$
2. Bob has a secret key $r$ and $K = X^{r} = g^{xr} \pmod p$, calculate the cipher $c_{1} = g^{r}$ and $c_{2} = m*K$
3. With the cipher, Alice knows $K = c_{1}^{x} = g^{rx}$ and thus can decrypt the text but Eve won't know $K$ since Eve don't know both $x$ and $r$

Note that $m = c_{2}*K^{-1} \pmod p$([[egcd]])

## How


## Why
- A two way [[Diffie Hellman]]

## Links
- [ElGamal encryption - Wikipedia](https://en.wikipedia.org/wiki/ElGamal_encryption)
- [[Asymmetric Cryptography]]