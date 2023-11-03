---
aliases: []
link: []
date created: Aug 1st, 2023
date modified: Aug 10th, 2023
---
Go programs express error state with `error` values.  
The `error` type is a built-in interface similar to `fmt.Stringer`:

```go
type error interface {
    Error() string
}
```

A nil `error` denotes success; a non-nil `error` denotes failure.

Functions often return an `error` value, and calling code should handle errors by testing whether the error equals `nil`.

```go
i, err := strconv.Atoi("42")
if err != nil {
    fmt.Printf("couldn't convert number: %v\n", err)
    return
}
fmt.Println("Converted integer:", i)
```

## Error Wrapping

```go
var criticalError = errors.New("Serious error")
unwrapped = fmt.Errorf("...%w...", criticalError)
```

## `recover`
Go makes it possible to _recover_ from a panic, by using the `recover` built-in function. A `recover` can stop a `panic` from aborting the program and let it continue with execution instead.

```go
package main

import "fmt"

func mayPanic() {
    panic("a problem")
}

func main() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered. Error:\n", r)
        }
    }()
    mayPanic()
    fmt.Println("After mayPanic()")
}
```

Under the hood, `recover` takes effect after `panic`, so put it in `defer`.