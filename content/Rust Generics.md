---
aliases: []
date created: Dec 15th, 2022
date modified: Jul 28th, 2023
---

```rust
struct Wrapper<T> {
    value: T,
}

impl<T> Wrapper<T> {
    pub fn new(value: T) -> Self {
        Wrapper { value }
    }
}
```

By declaring `T` as a generic type after `impl`, Rust can identify that the type in the angle brackets in `Point` is a generic type rather than a concrete type.

## Bound

```rust
// Define a function `printer` that takes a generic type `T` which
// must implement trait `Display`.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

- [[Rust Traits]]