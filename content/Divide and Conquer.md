---
aliases: [分治法]
date created: Mar 3rd, 2022
date modified: Jul 31st, 2022
---
- Definition  
Divide: subproblem that are smaller instances of the **same problem**  
Conquer: Solve subproblems **recursively**, "bottoms out" at the smallest subproblem  
Combine the solution to the subproblems into the solution for the original problem

General form: creates *a* subproblems each of which is *1/b* the size of the original problem

一般在参数上做文章，用 [[Recursion]] 解决问题  
有一个负责调用的函数和一个负责处理的函数  
相信自己每一步都是对的来调用处理函数

[[Master Theorem for Divide and Conquer]]

Example: [[Merge Sort]] | [[Quicksort]]  
Work with [[Dynamic Programming]] (Find maximum subarray)
