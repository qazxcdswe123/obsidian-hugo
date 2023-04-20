---
aliases: []
date created: Sep 28th, 2022
date modified: Sep 28th, 2022
---
## Function [[Closure]]

```go
package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	f2, f1 := 0, 1
	// return a function
	return func() int {
		f := f2
		f2, f1 = f1, f+f1
		return f
	}
}

func main() {
	f := fibonacci() // assign
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
```

## Methods
A method is just a function with a receiver argument.  

```go
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
// (v Vertex) is a receiver
```

You can only declare a method with a receiver whose type is defined in the same package as the method. You cannot declare a method with a receiver whose type is defined in another package (which includes the built-in types such as `int`).

You can declare methods with pointer receivers.

```go
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
```

Go interprets the statement `v.Scale(5)` as `(&v).Scale(5)` since the `Scale` method has a pointer receiver.
