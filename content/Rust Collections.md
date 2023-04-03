---
aliases: []
date created: Dec 13th, 2022
date modified: Dec 13th, 2022
---

## Struct

### Classic Struct
```rust
struct ColorClassicStruct {
    red: u8,
    green: u8,
    blue: u8,
}

fn classic_c_structs() {
    let green = ColorClassicStruct {
        red: 0,
        green: 255,
        blue: 0,
	};
}
```

### Tuple Like Struct
```rust
struct ColorTupleStruct(u8, u8, u8);

fn tuple_structs() {
    let green = ColorTupleStruct(0, 255, 255);

    assert_eq!(green.0, 0);
    assert_eq!(green.1, 255);
    assert_eq!(green.2, 0);
}
```

### Unit Like Struct
```rust
struct UnitStruct;
fn unit_structs() {
	let unit_struct = UnitStruct;
	let message = format!("{:?}s are fun!", unit_struct);
	assert_eq!(message, "UnitStructs are fun!");
}
```

### Creating Instances From Other Instances With Struct Update Syntax
Make sure you put the `..` at the end of the struct.

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn main() {
    // --snip--

    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };
}
```

## Enum
```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn process(&mut self, message: Message) {
    match message {
        Message::ChangeColor((r, g, b)) => self.change_color((r, g, b)),
        Message::Echo(s) => self.echo(s),
        Message::Move(p) => self.move_position(p),
        Message::Quit => self.quit()
    }
}

```

- `Quit` has no data associated with it at all.
- `Move` has named fields like a struct does.
- `Write` includes a single `String`.
- `ChangeColor` includes three `i32` values.

## Vector
```rust
let v: Vec<i32> = Vec::new(); //empty
let v = vec![1, 2, 3]; // or
v.push(5);
v.push(6);
v.push(7);
v.push(8);
```

## Strings

## Hash Maps
```rust
use std::collections::HashMap
basket.entry(Fruit::Banana).or_insert(50); // Adding a Key and Value Only If a Key Isn’t Present
```


## `Box`
```rust
pub enum List {
    Cons(i32, Box<List>),
    Nil,
}

List::Cons(1, Box::new(List::Nil))
```
