---
aliases: []
date created: Feb 7th, 2023
date modified: May 17th, 2023
---
Lifetime annotations don’t change how long any of the references live. Rather, they **describe** the relationships of the lifetimes of multiple references to each other without affecting the lifetimes.

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {}", result);
}

fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

struct Book<'a> {
    author: &'a str,
    title: &'a str,
}

fn main() {
    let name = String::from("Jill Smith");
    let title = String::from("Fish Flying");
    let book = Book { author: &name, title: &title };

    println!("{} by {}", book.title, book.author);
}
```

## Struct Lifetime
```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

This annotation means an instance of `ImportantExcerpt` can’t outlive the reference it holds in its `part` field.

## `static` Lifetime
The ​`'static`​ lifetime​​ is the longest​​ possible lifetime​​, and it lasts​​ for the entire​​ duration of the​​ running program.
The text of the string is stored directly in the program’s binary, which is always available.

There are two ways to make a variable with a `'static` lifetime, and both are stored in the read-only memory of the binary:
1. Make a constant with the `static` declaration.
2. Make a string literal which has type `&'static str`.

```rust
// A reference with 'static lifetime:
let s: &'static str = "hello world";

// 'static as part of a trait bound:
fn generic<T>(x: T) where T: 'static {}
```

## Elision
- [Validating References with Lifetimes - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-elision)

```rust
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }
```

## Links
- [Validating References with Lifetimes - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html)
- [Lifetimes - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/scope/lifetime.html)