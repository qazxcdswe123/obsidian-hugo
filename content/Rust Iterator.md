---
aliases: []
tags: []
date created: Feb 7th, 2023
date modified: Feb 7th, 2023
---
- [[C++ Iterator]]

## `Collect`
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