---
aliases: []
tags: []
date created: Jul 8th, 2022
date modified: Nov 2nd, 2022
---
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
	 - `maxHeapify`
		 - 
		 - recursively find largest among the three and move the largest up, then do the same thing to make sure it fit in the right position
	 - `buildMaxHeap`
		- bottom up iteration to up, starting from the leaf's parent.
- Used in heap [[Sorting Algorithm|sort]]

```cpp
// heap[0] is the size of heap
void maxHeapify(int heap[], int index)
{
    int left = index * 2;
    int right = index * 2 + 1;
    int largest = index;
    if (left <= heap[0] && heap[left] > heap[index])
    {
        largest = left;
    }
    if (right <= heap[0] && heap[right] > heap[largest])
    {
        largest = right;
    }
    if (largest != index)
    {
        swapElement(&heap[index], &heap[largest]);
        maxHeapify(heap, largest);
    }
}

void buildMaxHeap(int heap[])
{
	int length = sizeof(heap) / sizeof(heap[0]);
	for (int i = length / 2; i > -1; i--)
	{
		maxHeapify(heap, i);
	}
}
```