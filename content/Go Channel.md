---
link:
  - "[[Go sync]]"
  - "[[Lock|Lock]]"
aliases: []
date created: Apr 9th, 2023
date modified: Aug 12th, 2023
---
A channel in Go provides a connection between two goroutines, allowing them to communicate.

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

By default (unbuffered), sends and receives **block** until the other side is ready. This allows goroutines to synchronize without explicit [[Lock]] or condition variables. ([[Go sync]])
- **Note:** Only the sender should close a channel, never the receiver. Sending on a closed channel will cause a panic.
- **Note:** Channels aren't like files; you don't usually need to close them. Closing is only necessary when the receiver must be told there are no more values coming, such as to terminate a `range` loop.

## Buffered vs Unbuffered
- Unbuffered channels block the sender until the receiver receives the data, and vice versa. So you need another [[Goroutine]] to cooperate with.
- Buffered channels, on the other hand, are non-blocking for the sender as long as there is still room in the buffer.

## Select
The `select` statement lets a [[goroutine]] wait on multiple communication operations (handle multiple channels).

A `select` blocks until one of its cases can run, then it executes that case. It chooses one at random if multiple are ready.  

The `default` case in a `select` is run if no other case is ready.

Set timeout by `time.After`

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

## Channel VS Mutex
- Channel: 
	- passing ownership of data
	- distributing units of work
	- communicating async results
 - Mutex
	- caches
	- state

## Examples

### Merge Channel

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// the boring function return a channel to communicate with it.
func boring(msg string) <-chan string { // <-chan string means receives-only channel of string.
	c := make(chan string)
	go func() { // we launch goroutine inside a function.
		for i := 0; ; i++ {
			c <- fmt.Sprintf("%s %d", msg, i)
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
		}

	}()
	return c // return a channel to caller.
}

// <-chan string only get the receive value
// fanIn spawns 2 goroutines to reads the value from 2 channels
// then it sends to value to result channel( `c` channel)
func fanIn(c1, c2 <-chan string) <-chan string {
	c := make(chan string)
	go func() {
		for { // infinite loop to read value from channel.
			v1 := <-c1 // read value from c2. This line will wait when receiving value.
			c <- v1
		}
	}()
	go func() {
		for {
			c <- <-c2 // read value from c2 and send it to c
		}
	}()
	return c
}

func fanInSimple(cs ...<-chan string) <-chan string {
	c := make(chan string)
	for _, ci := range cs { // spawn channel based on the number of input channel

		go func(cv <-chan string) { // cv is a channel value
			for {
				c <- <-cv
			}
		}(ci) // send each channel to

	}
	return c
}

func main() {
	// merge 2 channels into 1 channel
	// c := fanIn(boring("Joe"), boring("Ahn"))
	c := fanInSimple(boring("Joe"), boring("Ahn"))

	for i := 0; i < 5; i++ {
		fmt.Println(<-c) // now we can read from 1 channel
	}
	fmt.Println("You're both boring. I'm leaving")
}
```

## Links
- [[Go Thread Pool]]
- [sync package - sync - Go Packages](http://golang.org/pkg/sync/#WaitGroup)
- [golang atomic maps](https://go.dev/doc/faq#atomic_maps)
- [GitHub - orcaman/concurrent-map: a thread-safe concurrent map for go](https://github.com/orcaman/concurrent-map)