---
aliases: []
date created: Sep 27th, 2022
date modified: Sep 27th, 2022
---
- [[Testing]]  
go `testing` package and `go test` command

1. Ending a file's name with `_test.go` tells the `go test` command that this file contains test functions.
2. Use function name like `TestSTH`, pass `t *testing.T` as parameter

- T  
[testing package - testing - Go Packages](https://pkg.go.dev/testing#T)

```go
type T struct {
	// contains filtered or unexported fields
}
```

T is a type passed to Test functions to manage test state and support formatted test logs.

