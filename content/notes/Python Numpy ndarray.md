- ndarray.ndim
	- The number of axes (dimensions) of the array.
- ndarray.shape
	- The dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension
- ndarray.size
	- The total number of elements of the array.
- ndarray.dtype
	- An object describing the type of the elements in the array.
	- One can create or specify dtype's using standard Python types.
- ndarray.data
	- The buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
- ndarray.itemsize
	- The size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

## Calculation
- Dot product
`@`, `*`, `a.dot(b)`