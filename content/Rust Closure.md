---
aliases: []
date created: Apr 11th, 2023
date modified: May 18th, 2023
---

## Capturing
1. `FnOnce` applies to closures that can be called once. All closures implement at least this trait, because all closures can be called. A closure that moves captured values out of its body will only implement `FnOnce` and none of the other `Fn` traits, because it can only be called once.
2. `FnMut` applies to closures that don’t move captured values out of their body, but that might mutate the captured values. These closures can be called more than once.
3. `Fn` applies to closures that don’t move captured values out of their body and that don’t mutate captured values, as well as closures that capture nothing from their environment. These closures can be called more than once without mutating their environment, which is important in cases such as calling a closure multiple times concurrently.

## Links
- [Closures](https://doc.rust-lang.org/reference/types/closure.html)
- [Closures - Rust By Example](https://doc.rust-lang.org/rust-by-example/fn/closures.html)