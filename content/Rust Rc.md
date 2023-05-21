abbreviation for _reference counting_

- Cloning an `Rc<T>` Increases the Reference Count

Example 

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::rc::Rc;

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
	 println!("count after creating a = {}", Rc::strong_count(&a)); // 1
    let b = Cons(3, Rc::clone(&a));
	println!("count after creating b = {}", Rc::strong_count(&a)); // 2
    let c = Cons(4, Rc::clone(&a));
}
```