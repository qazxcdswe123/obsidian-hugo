- 原理
  1. 从左往右排序
  2. 通过比较找位置，在比较途中向右平移较大的元素
  3. 因为平移，会有两个相同元素，替换左边的元素
  4. 如果是交换，本质上是冒泡？
```cpp
void insertSort(int array[], int length)
{
    for (int j = 1; j < length; j++)
    {
        int key = array[j];
        int i = j - 1;
        while (i >= 0 && array[i] > key)
        {
            array[i + 1] = array[i];
            i--;
        }
        array[i + 1] = key;
    }
}
```
