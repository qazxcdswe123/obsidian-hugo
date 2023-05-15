---
aliases: [Goroutines]
date created: Apr 9th, 2023
date modified: May 12th, 2023
---

## Channels
```go
ch := make(chan int)
ch <- v    // Send v to channel ch.
v, ok := <-ch  // Receive from ch, and assign value to v, test whether a channel has been closed
ch := make(chan int, 100) // Provide the buffer length as the second argument to `make` to initialize a buffered channel:

// The loop `for i := range c` receives values from the channel repeatedly until it is closed.
func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func main() {
	c := make(chan int, 10)
	go fibonacci(cap(c), c)
	for i := range c {
		fmt.Println(i)
	}
}
```

By default, sends and receives block until the other side is ready. This allows goroutines to synchronize without explicit [[locks]] or condition variables.
- **Note:** Only the sender should close a channel, never the receiver. Sending on a closed channel will cause a panic.
- **Note:** Channels aren't like files; you don't usually need to close them. Closing is only necessary when the receiver must be told there are no more values coming, such as to terminate a `range` loop.

### Buffered vs Unbuffered
- Unbuffered channels combine communication—the exchange of a value—with synchronization—guaranteeing that two calculations (goroutines) are in a known state.
- Unbuffered channels block the sender until the receiver receives the data, and vice versa.
- Buffered channels, on the other hand, are non-blocking for the sender as long as there is still room in the buffer.

Un-buffered channels are only writable when there's someone blocking to read from it, which means you shall have some [[Coroutine]] to work with -- instead of this single one.

### Select
The `select` statement lets a goroutine wait on multiple communication operations.  
A `select` blocks until one of its cases can run, then it executes that case. It chooses one at random if multiple are ready.  
The `default` case in a `select` is run if no other case is ready.

```go
func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c)
		}
		quit <- 0
	}()
	fibonacci(c, quit)
}

select {
case i := <-c:
    // use i
default:
    // receiving from c would block
}
```

### Channel VS Mutex
- Channel: 
	- passing ownership of data
	- distributing units of work
	- communicating async results
 - Mutex
	- caches
	- state

## Links
- [sync package - sync - Go Packages](http://golang.org/pkg/sync/#WaitGroup)
- [[Go Async]]
- [golang atomic maps](https://go.dev/doc/faq#atomic_maps)
- [GitHub - orcaman/concurrent-map: a thread-safe concurrent map for go](https://github.com/orcaman/concurrent-map)