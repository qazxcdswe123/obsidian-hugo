---
aliases: []
date created: May 17th, 2023
date modified: May 18th, 2023
---

## `Box<dyn Error>`
- [Boxing errors - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/error/multiple_error_types/boxing_errors.html)

A way to write simple code while preserving the original errors is to [`Box`](https://doc.rust-lang.org/std/boxed/struct.Box.html) them. The drawback is that the underlying error type is only known at runtime and not [statically determined](https://doc.rust-lang.org/book/ch17-02-trait-objects.html#trait-objects-perform-dynamic-dispatch).