A reference created with `ref` is exactly the same as reference taken with `&`.
The difference is where they're allowed in the syntax. `ref` on the left side of an assignment is like adding `&` on the right side.
This redundancy exists because in pattern matching `&` is used to require that a reference exists already, rather than to make a new one:

```rust
let foo = 1;
match foo {
   ref x => {
       /* x == &1 */ 
       match x {
           &y => /* y == 1 */
       }
   },  
}
```


```rust
// A `ref` borrow on the left side of an assignment is equivalent to
// an `&` borrow on the right side.
let ref ref_c1 = c;
let ref_c2 = &c;
```


## Links
- [The ref pattern - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/scope/borrow/ref.html)
- [ref - Rust](https://doc.rust-lang.org/std/keyword.ref.html)
- [rust - What can ref do that references couldn't? - Stack Overflow](https://stackoverflow.com/a/58292917/12614515)