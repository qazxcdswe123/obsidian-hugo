---
aliases: [指针]
tags: Programming/C 
date created: Feb 13th, 2022
date modified: Jul 28th, 2022
---

2022-07-28 Update  
其实要分辨指针，要（1）分清楚星号所在的地方，是个左值（left value），还是个右值（right value），（2）分清楚指针所指的类型，加上一些内存的通识就能理解了。

___
[[C语言重点——指针篇（一篇让你完全搞懂指针）]]
- `*` 在 int 后还是数值前
> As far as C goes they both do the same thing. It is a matter of preference. `int* i` shows clearly that it is an int pointer type. `int *i` shows the fact that the asterisk only affects a single variable. So `int *i, j` and `int* i, j` would both create `i` as an int pointer and `j` as an int.

效果一样：  
	`int* i` 强调 `i` 是一个指针变量  
	`int *i` 强调 `*` 只作用与一个数值  
	
`int *i, j` 和 `int* i, j` 效果都一样，一个指针和一个整数
___
- 两指针可以相减，不可相加。若要进行相减运算，则两指针必须指向同一数组，相减结果为相距的数组元素个数
