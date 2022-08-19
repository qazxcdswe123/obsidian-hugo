---
aliases: [二进制]
tags: [] 
date created: Jul 14th, 2022
date modified: Jul 28th, 2022
---
## Law
1. 每个十进制中偶数都在二进制中以 0 结尾
2. 二进制尾巴上加 0 是十进制 x2 , 有几个零就是 2 的几次方

## Calculate
### Bitwise
1. Decimal To Binary
    1. 先判断奇偶，末尾给 01
    2. 数/2 再看奇偶给 01，重复
    3. 重复到 1/2 后为 0
2. Binary To Decimal
    1. 第 n 位 x $2^{n-1}$，相加
3. & 与 and  
    0&0=0; 0&1=0; 1&1=1
4. | 或 or  
	0|0=0; 0|1=1; 1|0=1; 1|1=1
5. ^ 异或 xor  
	0⊕0=0，1⊕0=1，0⊕1=1，1⊕1=0  
	a ^ a = 0; a ^ 0 = a

### Shifting
- **Arithmetic shift** : Preserve sign bit
- **Logical shift** : Shift in 0

[[Set Theorem]]  
[[C++ bitwise operator]]