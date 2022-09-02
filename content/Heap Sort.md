[Optimized heap sort](https://stackoverflow.com/questions/35821661/finding-a-more-efficient-heap-sort)
Using [[Heap data structure]]
```cpp
void maxHeapify(int heap[], int index)
{
	if (index < heap[0])
	{
		int largest = 0;
		int left = index << 1;
		int right = (index << 1) + 1;
		if (left < heap[0] + 1 && heap[left] > heap[index]) // heap[0]+1 -> <=
		{
			largest = left;
		}
		else
		{
			largest = index;
		}

		if (right <= heap[0] && heap[right] > heap[largest]) // heap[0]+1 -> <=
		{
			largest = right;
		}

		if (largest != index)
		{
			swapElement(&heap[index], &heap[largest]);
			maxHeapify(heap, largest);
		}
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

void heapSort(int heap[])
{
	int length = sizeof(heap) / sizeof(heap[0]);
	for (int i = length; i > 0; i--)
	{
		swapElement(&heap[0], &heap[i]);
	}
}
```