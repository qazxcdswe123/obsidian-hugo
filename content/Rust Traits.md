---
aliases: [trait]
date created: Mar 2nd, 2023
date modified: May 18th, 2023
---
Note: Traits are similar to a feature often called _interfaces_ in other languages, although with some differences.

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
// or use where T: SomeTrait + OtherTrait
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

## `Clone`
- [Clone in std::clone - Rust](https://doc.rust-lang.org/std/clone/trait.Clone.html)  
The `Clone` trait is a trait in Rust that allows you to create a copy of an object.

## `Error`
- [Error in std::error - Rust](https://doc.rust-lang.org/std/error/trait.Error.html)  
The `Error` trait is a trait in Rust that represents the basic expectations for error values, i.e., values of type `E` in `Result<T, E>`.  
Errors must describe themselves through the `Display` and `Debug` traits

## `PartialEq`
- [PartialEq in std::cmp - Rust](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)
- `x.eq(y)` can also be written `x == y`, and `x.ne(y)` can be written `x != y`.
- `a != b` if and only if `!(a == b)`.

## `ToOwned`
- [ToOwned in alloc::borrow - Rust](https://doc.rust-lang.org/alloc/borrow/trait.ToOwned.html)  
`Clone` works only for going from `&T` to `T`. The `ToOwned` trait generalizes `Clone` to construct owned data from any borrow of a given type.

## `Debug`
- [Debug in std::fmt - Rust](https://doc.rust-lang.org/std/fmt/trait.Debug.html)  
Used in `{:?}`

## Links
- [Traits: Defining Shared Behavior - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html#specifying-multiple-trait-bounds-with-the--syntax)