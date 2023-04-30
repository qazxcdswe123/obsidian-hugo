---
aliases: []
date created: Sep 28th, 2022
date modified: Apr 17th, 2023
---
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

`recover` takes effect after `panic`, so put it in `defer`.

## `defer`
The deferred call's arguments are evaluated immediately, but the function call is not executed until the **surrounding function returns**.  
Deferred function calls are pushed onto a [[stack]]. When a function returns, its deferred calls are executed in last-in-first-out order.  
The expression must be a function or method call; it cannot be parenthesized. Calls of built-in functions are restricted as for [expression statements](https://go.dev/ref/spec#Expression_statements).

Good for resources cleanup.

## `sync.WaitGroup`
- [Go by Example: WaitGroups](https://gobyexample.com/waitgroups)  
To wait for multiple [[Goroutine|goroutines]] to finish, we can use a _wait group_.  
A WaitGroup must not be copied after first use.

**_Share [[memory]] by communicating, don't communicate by sharing memory_**

## Links
- [[Goroutine]]
- [[Asynchronous]]