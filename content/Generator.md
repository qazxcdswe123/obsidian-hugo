---
aliases: [生成元]
date created: Jul 2nd, 2023
date modified: Jul 2nd, 2023
---

- |g| = |G|

### 寻找生成元
寻找 Zp* 的生成元  
给定一个素数 p 和一个正整数 a，判断 a 是否是[[Primitive Root|原根]]，是[[Primitive Root|原根]]即为生成元  
过程：判断 a 是否有整除 p-1 的阶，找 p-1 的所有素因子 f，如果有 $f<p-1$ , $a^{f} = e$ ,说明不是[[Primitive Root|原根]]/生成元

