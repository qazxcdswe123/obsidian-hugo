## Thread
`use std::thread;`
By default, when the main thread of a Rust program completes, all spawned threads are shut down, whether or not they have finished running.

### Waiting for All Threads to Finish Using `join` Handles
```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

	handle.join().unwrap(); // put it here like waitGroup

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

## Links
- [Fearless Concurrency - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-00-concurrency.html)
- [[Concurrency]]
- [[Thread]]