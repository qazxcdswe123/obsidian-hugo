---
aliases: []
date created: May 22nd, 2023
date modified: May 22nd, 2023
---

## Rust RefCell
RefCell is a mutable memory location with dynamically checked borrow rules. It is used to change values without declaring mut and is like a Cell but uses references instead of copies. However, it checks borrows at runtime and not at compile-time, so it is essential to compile and run to check. The borrow rules are enforced at runtime, so if they are broken, the program will panic and exit.

### RefCell Methods
- `borrow()` method immutably borrows the wrapped value, returning an error if the value is currently mutably borrowed.
- `borrow_mut()` method mutably borrows the wrapped value, returning an error if the value is currently borrowed.

### Example
```rust
use std::cell::RefCell;
let c = RefCell::new(5);
{
    let m = c.borrow();
    assert!(c.try_borrow_mut().is_err());
}
{
    let m = c.borrow();
    assert!(c.try_borrow_mut().is_ok());
}
```

