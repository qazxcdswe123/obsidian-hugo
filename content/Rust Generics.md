---
aliases: []
tags: []
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

[[Rust Traits]]