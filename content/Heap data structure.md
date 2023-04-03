---
aliases: []
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
		 - recursively find largest among the three and move the largest up, then do the same thing to make sure it fit in the right position
		 - Top down 
	 - `buildMaxHeap`
		- bottom up iteration to up, starting from the leaf's parent.
		- Bottom up
- Used in heap [[Sorting Algorithm|sort]]


```cpp
void heapify(int arr[], int N, int i)
{
    // Initialize largest as root
    int largest = i;
 
    // left = 2*i + 1
    int l = 2 * i + 1;
 
    // right = 2*i + 2
    int r = 2 * i + 2;
 
    // If left child is larger than root
    if (l < N && arr[l] > arr[largest])
        largest = l;
 
    // If right child is larger than largest
    // so far
    if (r < N && arr[r] > arr[largest])
        largest = r;
 
    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
 
        // Recursively heapify the affected sub-tree
        heapify(arr, N, largest);
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
