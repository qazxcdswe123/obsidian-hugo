# HW 0
```c
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void insertionSort(int arr[], int size)
{
    for (int i = 1; i < size; i++)
    {
        int j = i - 1;
        int temp = arr[i];
        while (j >= 0 && arr[j] > temp)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
}

void decimalToBinary(int number)
{
    if (number == 0)
        return;
    else
    {
        decimalToBinary(number / 2);
        printf("%d", number % 2);
    }
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

bool isPrimeNaive(int number)
{
    if (number == 1)
        return false;
    for (int i = 2; i * i <= number; i++)
    {
        if (number % i == 0)
            return false;
    }
    return true;
}

bool isPrimeMod6(int number)
{
    if (number == 2 || number == 3)
        return true;
    else if (number <= 1 || number % 2 == 0 || number % 3 == 0)
        return false;
    else
    {
        for (int i = 5; i * i <= number; i += 6)
        {
            if (number % i == 0 || number % (i + 2) == 0) // +5 +1
                return false;
        }
    }
}

int main(void)
{
    int arr[] = {5, 2, 4, 6, 1, 3};
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("Before sorting:\n");
    printArray(arr, size);

    insertionSort(arr, size);

    printf("After sorting:\n");
    printArray(arr, size);

    printf("Convert decimal 12345 to binary:\n");
    decimalToBinary(12345);
    printf("\n");

    // benchmarking prime test function
    clock_t start, end;
    int numToTest[10000];
    for (int i = 0; i < 10000; i++)
        numToTest[i] = rand() % 1000000 + 1;
    printf("Benchmarking isPrimeNaive()\n");
    int check = 0;
    start = clock();
    for (int i = 0; i < 10000; i++)
    {
        if (isPrimeNaive(numToTest[i]))
            check += 1;
    }
    end = clock();
    printf("%d prime numbers found\n", check);
    printf("Time taken: %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    printf("Benchmarking isPrimeMod6()\n");
    check = 0;
    start = clock();
    for (int i = 0; i < 10000; i++)
    {
        if (isPrimeMod6(numToTest[i]))
            check += 1;
    }
    end = clock();
    printf("%d prime numbers found\n", check);
    printf("Time taken: %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);
    /*
    Before sorting:
    5 2 4 6 1 3
    After sorting:
    1 2 3 4 5 6
    Convert decimal 12345 to binary:
    11000000111001
    Benchmarking isPrmeNaive()
    776 prime numbers found
    Time taken: 0.001129 seconds
    Benchmarking isPrimeMod6()
    776 prime numbers found
    Time taken: 0.000443 seconds
    */
}
```

$a^n + b^n \neq c^n$