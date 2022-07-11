---
title: recursion 递归
---
原理为 [[Stack Data Structure]]，先进后出，学名 [Call Stack 调用栈](https://en.wikipedia.org/wiki/Call_stack)
递归要有 Base Case，并且一般是写在函数的最前头来看递归的终止条件

main 函数也是一种函数，也可以递归，
main 函数的参数 (int argc, char \*\*argv)， 前者为执行时的参数数量，至少为1 `./ProgramName`，后者为指向指针的指针，即数组内储存字符串。

Work with: [[Divide and Conquer 分治法]]