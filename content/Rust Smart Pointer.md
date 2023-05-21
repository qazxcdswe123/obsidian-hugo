---
aliases: []
date created: May 20th, 2023
date modified: May 20th, 2023
---
data structures that act like a [[pointer]] but also have additional metadata and capabilities.  
while references only borrow data, in many cases, smart pointers _own_ the data they point to.  
smart pointers implement the `Deref` and `Drop` traits.

- Most common
	- `Box<T>` for allocating values on the heap
		- [[Rust Box]]
	- `Rc<T>`, a reference counting type that enables multiple ownership
		- [[Rust Rc]]
	- `Ref<T>` and `RefMut<T>`, accessed through `RefCell<T>`, a type that enforces the borrowing rules at runtime instead of compile time
 