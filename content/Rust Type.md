---
aliases: []
date created: Dec 13th, 2022
date modified: Apr 4th, 2023
---
- Primitive types:
	- [Boolean](https://doc.rust-lang.org/reference/types/boolean.html) — `bool`
	- [Numeric](https://doc.rust-lang.org/reference/types/numeric.html) — integer and float
	- [Textual](https://doc.rust-lang.org/reference/types/textual.html) — `char` and `str`
	- [Never](https://doc.rust-lang.org/reference/types/never.html) — `!` — a type with no values
- Sequence types:
	- [Tuple](https://doc.rust-lang.org/reference/types/tuple.html)
	- [Array](https://doc.rust-lang.org/reference/types/array.html)
	- [Slice](https://doc.rust-lang.org/reference/types/slice.html)
- User-defined types:
	- [Struct](https://doc.rust-lang.org/reference/types/struct.html)
	- [Enum](https://doc.rust-lang.org/reference/types/enum.html)
	- [Union](https://doc.rust-lang.org/reference/types/union.html)
- Function types:
	- [Functions](https://doc.rust-lang.org/reference/types/function-item.html)
	- [Closures](https://doc.rust-lang.org/reference/types/closure.html)
- Pointer types:
	- [References](https://doc.rust-lang.org/reference/types/pointer.html#shared-references-)
	- [Raw pointers](https://doc.rust-lang.org/reference/types/pointer.html#raw-pointers-const-and-mut)
	- [Function pointers](https://doc.rust-lang.org/reference/types/function-pointer.html)
- Trait types:
	- [Trait objects](https://doc.rust-lang.org/reference/types/trait-object.html)
	- [Impl trait](https://doc.rust-lang.org/reference/types/impl-trait.html)
- [[Rust String]]
- `usize`: sizeof pointer
- Owned Types
	- variables that contain the actual values they represent
	- move types
- Borrowed Types
	- addresses of the values they represent

## Type alias
Replace empty `struct` with type alias

```rust
type Kilometers = i32;

let x: i32 = 5;
let y: Kilometers = 5;

println!("x + y = {}", x + y);
```

## Links
[Types - The Rust Reference](https://doc.rust-lang.org/reference/types.html)
