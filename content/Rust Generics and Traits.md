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

## Traits
A trait is a collection of methods.

Data types can implement traits. To do so, the methods making up the trait are defined for the data type. For example, the `String` data type implements the `From<&str>` trait. This allows a user to write `String::from("hello")`.

In this way, traits are somewhat similar to Java interfaces and C++ abstract classes.

Some additional common Rust traits include:
- `Clone` (the `clone` method)
- `Display` (which allows formatted display via `{}`)
- `Debug` (which allows formatted display via `{:?}`)

Because traits indicate shared behavior between data types, they are useful when writing generics.

### Traits as Parameters
```rust
// with trait bound
fn compare_license_types<T: Licensed, U: Licensed>(software: T, software_two: U) -> bool
// without trait bound
fn compare_license_types(software: impl Licensed, software_two: impl Licensed) -> bool
// Multiple trait bound using +
fn some_func(item: impl SomeTrait + OtherTrait) -> bool 
```

## Links
- [Traits: Defining Shared Behavior - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html#specifying-multiple-trait-bounds-with-the--syntax)