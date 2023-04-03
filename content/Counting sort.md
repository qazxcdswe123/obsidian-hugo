---
aliases: []
date: Jul 25th, 2022
---
- 原理
  已知: 待排序数组 _A_ 的取值范围，创建大小为 `max - min + 1` 的新数组 _C_，从而直接将值作为 index 访问
  记录值的出现次数，在对应 index 上++
  递推得出值是第几大，记录在 _C_ 中
  创建新数组 _B_ ，访问 `B[ C[ A[i]]] = A[i]`，同时 `C[A[i]]--`
  可选：复制数组回 _A_

- 用于 Radix sort 很好，因为确定只有 10 个元素
  Radix sort 额外再 Counting sort 的基础上记录一个 exp，达到计算每位数的目的。
  每次结束前将 Counting sort 原数组都进行一次排序（复制回去）

