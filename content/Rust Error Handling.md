---
aliases: []
date created: Nov 12th, 2022
date modified: Dec 14th, 2022
---
[[Rust Type]]

## `Result` Enum
```rust
fn main() {
enum Result<T, E> {
	    Ok(T),
	    Err(E),
	}
}

pub fn generate_nametag_text(name: String) -> Result<String, String> {
    if name.is_empty() {
        // Empty names aren't allowed.
        Err(String::from("`name` was empty; it must be nonempty."))
    } else {
        Ok(format!("Hi! My name is {}", name))
    }
}
```

### `Ok`
`Ok` variant indicates the operation was successful, and inside `Ok` is the successfully generated value.

### `Err`
`Err` variant means the operation failed, and `Err` contains information about how or why the operation failed.

### `?` Operator
```rust
use std::fs::File;
use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();
    File::open("hello.txt")?.read_to_string(&mut username)?;
    Ok(username)
}
```

The `?` operator can only be used in functions whose return type is compatible with the value the `?` is used on. This is because the `?` operator is defined to perform an early return of a value out of the function, in the same manner as the `match` expression we defined in Listing 9-6. In Listing 9-6, the `match` was using a `Result` value, and the early return arm returned an `Err(e)` value. The return type of the function has to be a `Result` so that it’s compatible with this `return`.

- **Catch-all error**
Under the hood, the `?` operator calls `From::from` on the error value to convert it to a boxed trait object, a `Box<dyn error::Error>`. This boxed trait object is polymorphic, and since all errors implement the `error:Error` trait, we can capture lots of different errors in one "Box" object.

## `Option` Enum
```rust
#![allow(unused)]
fn main() {
	enum Option<T> {
	    None, // NULL Equivalent
	    Some(T),
	}
}

let x = Some("air");
assert_eq!(x.unwrap(), "air");

let maybe_name = Some(String::from("Alice"));
// Using `ref`, the value is borrowed, not moved ...
match maybe_name {
    Some(ref n) => println!("Hello, {n}"),
    _ => println!("Hello, world"),
}
// ... so it's available here!
println!("Hello again, {}", maybe_name.unwrap_or("world".into()));
```

- `Some()`
- `None`

## [`&` vs `ref`](https://doc.rust-lang.org/std/keyword.ref.html#-vs-ref)
- `&` denotes that your pattern expects a reference to an object. Hence `&` is a part of said pattern: `&Foo` matches different objects than `Foo` does.
- `ref` indicates that you want a reference to an unpacked value. It is not matched against: `Foo(ref foo)` matches the same objects as `Foo(foo)`.

## Links
[ref - Rust](https://doc.rust-lang.org/std/keyword.ref.html)
