CLRS Chapter 6
#Data-structure

# 介绍
主要为 **Binary** Heap，分为 ***max-heap*** 和 ***min-heap***，以 max-heap 为例
从上往下二叉而下，Parent 一定大于 Children，Children 之间不可比
Index 为从上到下，从左到右

# 特性
1. n-element **height** = $\lfloor{\lg n}\rfloor$

和 [[Memory]] 中的 heap 区分
- 维护 Heap 由两部分组成
	 - maxHeapify
		 - recursively find largest among the three and move the largest up, then do the same thing until it fit in the right position
	 - buildMaxHeap
		- bottom up iteration to up
- Usage：[[Heap Sort]]
