---
aliases: []
date created: Feb 7th, 2023
date modified: Mar 2nd, 2023
---
- [[C++ Iterator]]

## `Collect`
[Iterator in std::iter - Rust](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.collect)

```rust
pub fn capitalize_first(input: &str) -> String {
    let mut c = input.chars();
    match c.next() {
        None => String::new(),
        Some(first) =>  first.to_uppercase().collect::<String>() + c.as_str(),
    }
}

pub fn capitalize_words_string(words: &[&str]) -> String {
    words.iter().map(|word| capitalize_first(word)).collect::<String>()
}
```

## `Fold`
[Iterator in std::iter - Rust](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.fold)

```rust
pub fn factorial(num: u64) -> u64 {
	// Initial of acc (sum in this example), then lambda
    (1..=num).fold(1, |sum, v| sum * v)
    // (1..=num).reduce(|sum, v| sum * v).unwrap()
    // (1..=num).product()
}

```

## `Filter`
[Iterator in std::iter - Rust](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.filter)

```rust
let a = [0i32, 1, 2];
let mut iter = a.iter().filter(|x| x.is_positive());

let a = [0, 1, 2];
let mut iter = a.iter().filter(|&x| *x > 1); // both & and *
```
