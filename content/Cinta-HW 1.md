---
aliases: []
tags: []
date created: Aug 29th, 2022
date modified: Aug 29th, 2022
---
第一章课后习题：1、3、4  
选做：2、7

## 2
**dnf**
```cpp
#include <iostream>

using namespace std;

bool isPowerOfTwo(int n)
{
    return (n & (n - 1)) == 0;
}

int main()
{
    // use bitwise operators to check if there is only a 1 in the binary representation of the number
    int notPowerOfTwo = 3;
    int powerOfTwo = 4;

    cout << isPowerOfTwo(notPowerOfTwo) << endl;
    cout << isPowerOfTwo(powerOfTwo) << endl;
}
```

## 4
$\because a | b , b | c$  
$\therefore b = k_1 a, c = k_2 b$
$\therefore c = k_1 k_2 a$
$\therefore a | c$
___
dnf

## 7
Suppose $a^2 = 111 \cdots 111$ , clearly it must be a power of odd number, so $a$ is odd.
Let $a = 2b + 1$, $a^2 = 4b^2 + 4b + 1$
$4b^2 + 4b + 1 = 1 \pmod 4$
$111 \cdots 111 = -1 \pmod 4$ (where the number of 1 > 2, aka n > 2)
QED.