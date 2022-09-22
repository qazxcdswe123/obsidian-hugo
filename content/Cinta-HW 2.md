![](https://img.ynchen.me/2022/09/ece0e99236b53cce4eafda40fb668bdd.webp)


11. 编程题：编写一个 Python 程序计算乘法逆元，即输入互素的正整数 c 和 m，返回 c ，使得 $cc^{−1} \equiv 1 \pmod{m}$。要求:只返回为正整数的 $c^{-1}$。

## 7
a. -2
b. 28
c. 265

## 8
```c++
#include <iostream>

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

int main()
{
    int res = rec_mod_exp(7, 10, 11);
    std::cout << res << std::endl;
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
因为互质，由 Bezout 定理得，一定存在 $cs + mt = 1$, 此时有无数多个 s
两边取 mod m, 得 $cs \equiv 1 \pmod{m}$
此时，因为 c 确定，由 mod 的定义得，s 确定。
所以，在 mod m 的意义上存在唯一确定的整数值 $c^{-1}$ 使得 $cc^{-1} \equiv 1 \pmod{m}$

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