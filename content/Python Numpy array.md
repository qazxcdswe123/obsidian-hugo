---
aliases: []
date created: Jun 28th, 2022
date modified: Nov 17th, 2022
---
- ndarray.ndim
	- The number of axes (dimensions) of the array.
- ndarray.shape
	- The dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension
- ndarray.size
	- The total number of elements of the array.
- `ndarray.dtype`
	- An object describing the type of the elements in the array.
	- One can create or specify dtype's using standard Python types.
- `ndarray.data`
	- The buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
- `ndarray.itemsize`
	- The size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

## Calculation
- Dot product  
`@`, `*`, `a.dot(b)`


# Visual Guide
[Medium](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d)  
![](https://miro.medium.com/max/1313/1*ND8LvMjQOX19G-Yg0ANPxw.png)  
NumPy arrays are:
- more compact, especially when there’s more than one dimension
- faster than lists when the operation can be vectorized
- slower than lists when you append elements to the end
- usually homogeneous: can only work fast with elements of one type

## 1. Vectors, the 1D Arrays
![](https://miro.medium.com/max/1313/1*cyN_FxUVbkdDyrULhfTIGw.png)

## Matrices, the 2D Arrays
![](https://miro.medium.com/max/1313/1*aLMuXA81pDXaw0J0QdKvRQ.png)

# The Basics
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers.  
In NumPy dimensions are called _axes_.
