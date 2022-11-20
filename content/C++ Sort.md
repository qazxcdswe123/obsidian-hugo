---
aliases: []
tags: []
date created: Jul 10th, 2022
date modified: Nov 17th, 2022
---

# STL Sort

## sort()
`algorithm` header

### Usage
```cpp
int main()
{
	int arr[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };
	int n = sizeof(arr) / sizeof(arr[0]);

	/*Here we take two parameters, the beginning of the
	array and the length n upto which we want the array to
	be sorted*/
	sort(arr, arr + n);
}
```

### Reverse
Use `<functional>` header and `std::greater` [Src](https://en.cppreference.com/w/cpp/utility/functional/greater)  
`sort( &arr[0], &arr[n], greater<int>() )`  
or any boolean return function [[Queue]]

## qsort()
`stdlib.h` header

### Usage
`void qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void*))`
- **base** − This is the **pointer** to the **first** element of the array to be sorted.
- **nitems** − This is the **number of elements** in the array pointed by base.
- **size** − This is the **size in bytes** of each element in the array.
- **compar** − This is the function that compares two elements. Return `INT`

- example

```cpp
#include <stdio.h>
#include <stdlib.h>

int values[] = { 88, 56, 100, 2, 25 };

int cmpfunc (const void *a, const void *b) {
   return ( *(int*)a - *(int*)b );
}

int main () {
   printf("Before sorting the list is: \n");
   for(int n = 0 ; n < 5; n++ ) {
      printf("%d ", values[n]);
   }

   qsort(values, 5, sizeof(int), cmpfunc);

   printf("\nAfter sorting the list is: \n");
   for(int n = 0 ; n < 5; n++ ) {   
      printf("%d ", values[n]);
   }
}
```