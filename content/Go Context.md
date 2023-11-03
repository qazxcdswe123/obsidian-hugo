Package context defines the Context type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes.

Do not store Contexts inside a struct type; instead, **pass a Context explicitly to each function** that needs it. The Context should be the first parameter, typically named `ctx`:

## `Done`


## Links
- [Go Concurrency Patterns: Context - The Go Programming Language](https://go.dev/blog/context)
- [Go Context](https://pkg.go.dev/context)
- [Digital Ocean: How to Use Contexts in Go](https://www.digitalocean.com/community/tutorials/how-to-use-contexts-in-go)