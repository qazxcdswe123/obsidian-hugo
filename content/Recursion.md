---
aliases: [递归]
tags: []
date created: Jul 8th, 2022
date modified: Sep 1st, 2022
---
原理为 [[Stack Data Structure]]，先进后出，学名 [Call Stack 调用栈](https://en.wikipedia.org/wiki/Call_stack)  
递归要有 Base Case，并且一般是写在函数的最前头来看递归的终止条件

main 函数也是一种函数，也可以递归，  
main 函数的参数 (int argc, char \*\*argv)， 前者为执行时的参数数量，至少为 1 `./ProgramName`，后者为指向指针的指针，即数组内储存字符串。

Work with: [[Divide and Conquer]]

## Hanoi Tower
[Recursion: Towers of Hanoi](https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html)
```
FUNCTION MoveTower(disk, source, dest, spare):
IF disk == 0, THEN:
    move disk from source to dest
ELSE:
    MoveTower(disk - 1, source, spare, dest)   // Step 1 above
    move disk from source to dest              // Step 2 above
    MoveTower(disk - 1, spare, dest, source)   // Step 3 above
END IF
```