This declaration means that `s` is a slice of any type `T` that fulfills the built-in constraint `comparable`. `x` is also a value of the same type.
```go
func Index[T comparable](s []T, x T) int
```

