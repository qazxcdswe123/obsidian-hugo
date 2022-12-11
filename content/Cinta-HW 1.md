---
aliases: []
tags: []
date created: Aug 29th, 2022
date modified: Sep 3rd, 2022
---
因为博客放的其实是笔记，太多太杂bu，就不放留言了...

第一章课后习题：1、3、4  
选做：2、7

## 1, 2, 3

```cpp
#include <iostream>

using namespace std;

bool isPowerOfTwo(int n)
{
    return (n > 0) && ((n & (n - 1)) == 0);
}

bool isEven(int n)
{
    return (n & 1) == 0;
}

// assuming b >= 0
int simpleMultiplyIterative(int a, int b)
{
    int res = 0;
    int multiplier = 1;
    while (b != 0)
    {
        if (isEven(b))
        {
            multiplier *= 2;
            b /= 2;
        }
        else
        {
            res += a * multiplier;
            multiplier *= 2;
            b /= 2;
        }
    }
    return res;
}

int main()
{
    int notPowerOfTwo = 3;
    int powerOfTwo = 4;

    cout << isPowerOfTwo(notPowerOfTwo) << endl;
    cout << isPowerOfTwo(powerOfTwo) << endl;

    cout << isEven(notPowerOfTwo) << endl;
    cout << isEven(powerOfTwo) << endl;

    cout << simpleMultiplyIterative(-2, 3) << endl;
}

// output
// 0
// 1
// 0
// 1
// -6
```

___

## 4
For the first part  
$\because a | b , b | c$  
$\therefore b = k_1 a, c = k_2 b$  
$\therefore c = k_1 k_2 a$  
$\therefore a | c$

For the next part  
$\because c|a, c|b$  
$\therefore a = k_1 c, b = k_2 c$  
$\therefore (ma+nb) = (m k_1 c + n k_2 c) = c(m k_1 + n k_2)$  
$\therefore c|(ma+nb)$
___

## 7
Suppose $a^2 = 111 \cdots 111$ , clearly it must be a power of odd number, so $a$ is odd.  
Let $a = 2b + 1$, $a^2 = 4b^2 + 4b + 1$  
$4b^2 + 4b + 1 = 1 \pmod 4$  
$111 \cdots 111 = -1 \pmod 4$ (where the number of 1 > 2, aka n > 2)  
QED.