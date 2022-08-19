- 单向版本
  1. 取 Pivot，一般为最左 | 最右 | 或者中间随机后和最左右换位置（中间）取最左为 Pivot
  2. 设置变量 `i = left - 1` 来记录有几个比 Pivot 小（最开始是 0 个小于）
  3. 用循环从左到右遍历除 Pivot 外的所有元素，和 Pivot 进行比较
  4. 如果比 Pivot 大，不动；如果小，则和 `i + 1` 位置调换，因为 `i` 是比 Pivot 小的，完成循环
  5. Pivot 和 `i + 1` 调换，完成左右部分的归纳
  6. 归纳到最后的长度为 1

- 双向版本 类似[[Multi Thread]]
  1. 取 0 为 Pivot；1 为 Left；n-1 为 Right
  2. Left Right 用于记录位置不正确的元素，Left 的值比 Pivot 大，Right 的值比 Pivot 小时，交换并相中靠一步
  3. 直到 Left > Right，交换 Pivot 和 Right（Right 的左边一定比 Pivot 小）

- Dual pivot Quicksort
[dual-pivot quicksort](https://xlinux.nist.gov/dads/HTML/dualPivotQuicksort.html)

**Definition:** Pick two elements from the [_array_](https://xlinux.nist.gov/dads/HTML/array.html) to be sorted (the pivots), partition the remaining elements into (i) those less than the lesser pivot, (ii) those between the pivots, and (iii) those greater than the greater pivot, and recursively sort these partitions.
![](https://s2.loli.net/2022/02/24/F7HtqrQAxLMal9I.png)
![](https://s2.loli.net/2022/02/24/cMhQvrFDpTBiJ2G.png)


***

  *Note: Dual-pivot quicksort is consistently faster than [quicksort*](https://xlinux.nist.gov/dads/HTML/quicksort.html) in practice, although classical analysis suggests that it should be slower. *Why Is Dual-Pivot Quicksort Fast? , [arXiv:1511.01138](https://arxiv.org/pdf/1511.01138.pdf) v2 28 Sep 2016.

  - [ ] Read Why Dual-pivot quicksort is faster [[todo]]

- Quicksearch | Quickselect
  [快速选择](https://www.geeksforgeeks.org/quickselect-algorithm/)

- Why Quicksort is consider faster than Mergesort
  It's "in place sort", there's no need to allocate additional memory to complete the task.
