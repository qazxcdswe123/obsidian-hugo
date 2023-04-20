---
aliases: []
date created: Dec 14th, 2022
date modified: Dec 14th, 2022
---

## Match
```rust
match VALUE {
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
}
```

## If Let
```rust
fn main() {
    let config_max = Some(3u8);
    if let Some(max) = config_max {
        println!("The maximum is configured to be {}", max);
    }
}
```

Give the RHS value to the left if there is a value in `Some`. [[Rust Error Handling]]
