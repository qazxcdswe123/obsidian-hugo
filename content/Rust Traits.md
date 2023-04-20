---
aliases: [trait]
date created: Mar 2nd, 2023
date modified: Mar 27th, 2023
---

## Traits
A _trait_ defines functionality a particular type has and can share with other types. We can use traits to define shared behavior in an abstract way.

Data types can implement traits. To do so, the methods making up the trait are defined for the data type. For example, the `String` data type implements the `From<&str>` trait. This allows a user to write `String::from("hello")`.

In this way, traits are somewhat similar to [[Java]] interfaces and [[C++]] abstract classes.

Some additional common [[Rust]] traits include:
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

### [Returning Types that Implement Traits](https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-implement-traits)
```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}
```
## Links
- [Traits: Defining Shared Behavior - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html#specifying-multiple-trait-bounds-with-the--syntax)