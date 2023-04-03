---
aliases: []
date created: Dec 13th, 2022
date modified: Mar 27th, 2023
---

## Borrow Checker
- Each value in [[Rust]] has an _owner_.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.  

[[Rust]] has a special annotation called the `Copy` [[Rust Traits|trait]] that we can place on types that are stored on the stack, as integers are. If a type implements the `Copy` [[Rust Traits|trait]], variables that use it do not move, but rather are trivially copied, making them still valid after assignment to another variable.

So what types implement the `Copy` [[Rust Traits|trait]]? You can check the documentation for the given type to be sure, but as a general rule, any group of simple scalar values can implement `Copy`, and nothing that requires allocation or is some form of resource can implement `Copy`. Here are some of the types that implement `Copy`:

- All the integer types, such as `u32`.
- The Boolean type, `bool`, with values `true` and `false`.
- All the floating point types, such as `f64`.
- The character type, `char`.
- Tuples, if they only contain types that also implement `Copy`. For example, `(i32, i32)` implements `Copy`, but `(i32, String)` does not.

A _data race_ is similar to a race condition and happens when these three behaviors occur:
- Two or more pointers access the same data at the same time.
- At least one of the pointers is being used to write to the data.
- There’s no mechanism being used to synchronize access to the data.

## Links
- [[Rust Lifetime]]
