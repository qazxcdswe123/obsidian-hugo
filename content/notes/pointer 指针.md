---
title: pointer 指针
---
#Programming/C
[[C语言重点——指针篇（一篇让你完全搞懂指针）]]
# * 在 int 后还是数值前
> As far as C goes they both do the same thing. It is a matter of preference. `int* i` shows clearly that it is an int pointer type. `int *i` shows the fact that the asterisk only affects a single variable. So `int *i, j` and `int* i, j` would both create `i` as an int pointer and `j` as an int.

`int* i` 强调 `i` 是一个指针变量
`int *i` 强调 `*` 只作用与一个数值
`int *i, j` 和 `int* i, j` 效果都一样，一个指针和一个整数
___
- 两指针可以相减，不可相加。若要进行相减运算，则两指针必须指向同一数组，相减结果为相距的数组元素个数