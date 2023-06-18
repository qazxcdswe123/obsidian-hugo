## `format!()`
```rust
let mut s = format!("{} World", input);
```

## `vec![]`
```rust
vec![1, 2, 3]
```

## `dbg!()`
```rust
let a = 2;
let b = dbg!(a * 2) + 1;
//      ^-- prints: [src/main.rs:2] a * 2 = 4
assert_eq!(b, 5);
```

- [[Macros]]