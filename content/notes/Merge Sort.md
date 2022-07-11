---
title: Merge Sort
---
- 原理
  先 Divide 到最小再 Conquer，所以调用方式中的 Merge 在最后
  Divide 无脑二分，Conquer 合并

```cpp
void merge(int *ar, int l, int m, int r)
{
    int n1 = m - l + 1, n2 = r - m;
    int *L = (int *)malloc(sizeof(int) * n1);
    int *R = (int *)malloc(sizeof(int) * n2);

    for (int i = 0; i < n1; i++)
    {
        L[i] = ar[l + i];
    }
    for (int j = 0; j < n2; j++)
    {
        R[j] = ar[m + j + 1];
    }

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            ar[k] = L[i];
            i++;
        }
        else
        {
            ar[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        ar[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        ar[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int *ar, int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;
        mergeSort(ar, l, m);
        mergeSort(ar, m + 1, r);
        merge(ar, l, m, r);
    }
}
```
