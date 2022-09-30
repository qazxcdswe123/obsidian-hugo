---
aliases: []
tags: []
date created: Sep 29th, 2022
date modified: Sep 29th, 2022
---
# Slice
## Slices Are Like References to Arrays
A slice does not store any data, it just describes a section of an underlying array.

Changing the elements of a slice modifies the corresponding elements of its underlying array.

Other slices that share the same underlying array will see those changes.

## `len()` And `cap()`
A slice has both a _length_ and a _capacity_.

The length of a slice is the number of elements it contains.

The capacity of a slice is the number of elements in the underlying array, counting from the first element in the slice.

The length and capacity of a slice `s` can be obtained using the expressions `len(s)` and `cap(s)`.

You can extend a slice's length by re-slicing it, provided it has sufficient capacity. Try changing one of the slice operations in the example program to extend it beyond its capacity and see what happens.

## Creating a Slice with Make
Slices can be created with the built-in `make` function; this is how you create dynamically-sized arrays.

The `make` function allocates a zeroed array and returns a slice that refers to that array:

```go
a := make([]int, 5)  // len(a)=5
```

To specify a capacity, pass a third argument to `make`:

```go
b := make([]int, 0, 5) // len(b)=0, cap(b)=5

b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4
```

# Map
- Map  
`map[key-type]value-type`  
`messages := make(map[string]string)`

- Delete an element:  
`delete(m, key)`

- Test that a key is present with a two-value assignment:  
`elem, ok = m[key]`

# Interfaces
An _interface type_ is defined as a set of method signatures.

A value of interface type can hold any value that implements those methods.

Under the hood, interface values can be thought of as a tuple of a value and a concrete type:

```
(value, type)
```
