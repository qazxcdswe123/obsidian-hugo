## What
1. Publicly transport a large [[prime]] number `p` and it's [[primitive root]] `g`
2. Alice chooses a secret `a` and compute `A = g^a mod p`
3. Bob chooses a secret `b` and compute `B = g^b mod p`
4. Publicly trnasport `A` and `B`
5. Now $A^b$ and $B^a$ are the same after $\mod p$, this is the secret key.

## Why
Eve only know $g^a$ and $g^b$, to know $g^{ab}$ we need to solve the [[Discrete Logarithm]] problem

## Implementation
```python
import random

def generate_key(p, g, a):
    A = pow(g, a, p)
    return A

def compute_secret_key(p, B, a):
    s = pow(B, a, p)
    return s

# Example usage
p = 23
g = 5
a = random.randint(1, p-1)
b = random.randint(1, p-1)

A = generate_key(p, g, a)
B = generate_key(p, g, b)

s1 = compute_secret_key(p, B, a)
s2 = compute_secret_key(p, A, b)

assert s1 == s2
print("Shared secret key:", s1)
```