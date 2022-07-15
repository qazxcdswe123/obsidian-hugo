- 原理
	- 从第 1 个开始
	- 暂存第 j 个，i = j - 1, i 不停往上覆盖
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
![](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)