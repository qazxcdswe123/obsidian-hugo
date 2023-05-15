---
aliases: []
date created: Sep 29th, 2022
date modified: May 12th, 2023
---

# Slice
The slice type is an abstraction built on top of Go’s array type

## Slices Are Like References to Arrays
A slice does not store any data, it just describes a section of an underlying array.  
Changing the elements of a slice modifies the corresponding elements of its underlying array.  
Other slices that share the same underlying array will see those changes.

## `len()` And `cap()`
A slice has both a _length_ and a _capacity_.  
The length of a slice is the number of elements it contains.  
The capacity of a slice is the number of elements in the underlying array, counting from the first element in the slice.  
The length and capacity of a slice `s` can be obtained using the expressions `len(s)` and `cap(s)`.  
You can extend a slice's length by re-slicing it, provided it has sufficient capacity. 

## Creating a Slice with Make
Slices can be created with the built-in `make` function; this is how you create dynamically-sized arrays.  
The `make` function allocates a zeroed array and returns a slice that refers to that array:

```go
sz := 5
a := make([]int, sz)  // len(a)=5
```

To specify a capacity, pass a third argument to `make`:

```go
b := make([]int, 0, 5) // len(b)=0, cap(b)=5

b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4
```

# Map
- Map  

```go
// map[key-type]value-type  
messages := make(map[string]string)

// Literal
var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

// insert or update
m[key] = elem
```

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

### Empty Interface
Empty interfaces are used by code that handles values of unknown type. For example, `fmt.Print` takes any number of arguments of type `interface{}`.

### Type Assertion
In Go, a type assertion is used to extract the underlying concrete value of an interface value.

```go
value.(typeName)
```