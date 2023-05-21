## Rust Arc
Atomically Reference Counted
It is a smart pointer that provides shared ownership of a value of type `T`, allocated in the heap. Invoking `clone` on `Arc` produces a new pointer to the same value in the heap. When the last `Arc` pointer to a given value is destroyed, the pointed-to value is also destroyed

## Links
- [[Rust Box]]
- [[Rust Smart Pointer]]