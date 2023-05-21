---
aliases: []
date created: May 17th, 2023
date modified: May 20th, 2023
---
Boxes don’t have performance overhead, other than storing their data on the heap instead of on the stack.

- Use cases
	- When you have a type whose size can’t be known at compile time and you want to use a value of that type in a context that requires an exact size
	- When you have a large amount of data and you want to transfer ownership but ensure the data won’t be copied when you do so
	- When you want to own a value and you care only that it’s a type that implements a particular trait rather than being of a specific type

## `Box<dyn Error>`
- [Boxing errors - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/error/multiple_error_types/boxing_errors.html)

A way to write simple code while preserving the original errors is to [`Box`](https://doc.rust-lang.org/std/boxed/struct.Box.html) them. The drawback is that the underlying error type is only known at runtime and not [statically determined](https://doc.rust-lang.org/book/ch17-02-trait-objects.html#trait-objects-perform-dynamic-dispatch).