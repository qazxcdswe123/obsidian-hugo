---
aliases: []
tags: []
date created: Sep 20th, 2022
date modified: Oct 5th, 2022
---
![](https://img.ynchen.me/2022/09/ece0e99236b53cce4eafda40fb668bdd.webp)  
## 7
a. -2  
b. 28  
c. 265

## 8

```c
// calculate x^y mod m
int rec_mod_exp(int x, int y, int m)
{
    if (y == 0)
    {
        return 1;
    }
    int z = rec_mod_exp(x, y / 2, m);
    if ((y & 1) == 0)
    {
        return z * z % m;
    }
    else
    {
        return x * z * z % m;
    }
}
```

## 9

```python
def matrix_multiply(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return C


def matrix_power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return matrix
    elif n % 2 == 0:
        return matrix_power(matrix_multiply(matrix, matrix), n // 2)
    elif n % 2 == 1:
        return matrix_multiply(matrix, matrix_power(matrix_multiply(matrix, matrix), n // 2))


fibonacci_matrix = [[1, 1], [1, 0]]
print(matrix_power(fibonacci_matrix, 10)[0][1]) # 55
```

## 10
- 存在性  
因为互质，由 Bezout 定理得，一定存在 $cs + mt = 1$, 此时有无数多个 s  
两边取 mod m, 得 $cs \equiv 1 \pmod{m}$  
即存在 $c^{-1} = s$

- 唯一性  
假设存在 $c_2^{-1} \neq c^{-1}$ , 并且 $c_2^{-1}c \equiv 1 \pmod{m}$, $c^{-1}c \equiv 1 \pmod{m}$  
即 $c^{-1} \equiv c_2^{-1} \pmod{m}$  
即在 mod m 意义下， $c^{-1} = c_2^{-1} = s$  
唯一性得证

## 11

```python
def egcd(a, b):
    if (a == 0):
        return (0, 1, b)
    else:
        x, y, gcd = egcd(b % a, a)
        return (y - (b // a) * x, x, gcd)

# Calculate Modular Multiplicative Inverse
def get_modular_inverse(a, m):
    s, t, gcd = egcd(a, m)
    if (gcd != 1):
        return None
    else:
        return s % m

print(get_modular_inverse(5, 11))
print(get_modular_inverse(13, 121))
print(get_modular_inverse(131, 1021))
```
