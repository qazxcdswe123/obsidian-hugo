---
aliases: []
date created: Dec 15th, 2022
date modified: Dec 15th, 2022
---

## Generics
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

- [[Rust Traits]]
