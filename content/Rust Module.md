---
aliases: []
date created: Dec 13th, 2022
date modified: Dec 13th, 2022
---
- **Packages:** A Cargo feature that lets you build, test, and share crates
- **Crates:** A tree of modules that produces a library or executable
- **Modules** and **use:** Let you control the organization, scope, and privacy of paths
- **Paths:** A way of naming an item, such as a struct, function, or module

member inside `mod` is private by default, need a explicit `pub` to make it public accessible.

```
src
    utils
        bar.rs
        foo.rs
    utils.rs
    main.rs
```

## Links
- [Defining Modules to Control Scope and Privacy - The Rust Programming Language](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)
- [Visibility - Rust By Example](https://doc.rust-lang.org/rust-by-example/mod/visibility.html)