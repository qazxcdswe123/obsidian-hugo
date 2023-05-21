**clone-on-write** smart pointer
It can enclose and provide immutable access to borrowed data, and clone the data lazily when mutation or ownership is required.

contain `Cow::Owned` and `Cow::Borrowed`

## Links
- [Cow in std::borrow - Rust](https://doc.rust-lang.org/std/borrow/enum.Cow.html)
- [[Rust Smart Pointer]]